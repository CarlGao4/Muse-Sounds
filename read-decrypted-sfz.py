# read-decrypted-sfz.py
# A demo script to read decrypted spx from MuseScore4 memory
# Designed for Windows only
# Visit https://github.com/CarlGao4/Muse-Sounds for more information

import frida
import msvcrt
import re
import sys
import threading

assert sys.platform == "win32", "This script is for Windows only"


# TODO: Set this to False if you don't want to print the output to console
# At this time, the script will only print a dot each time a decrypted data is retrieved
print_output = True

# TODO: Output file name, set this to empty string if you don't want to save the output
out_name = "decrypted.out"

# TODO: Set this to False if you don't want to replace separator (\x00) with newline and a line of dashes
# In fact, the script will automatically add \x00 to the beginning of a file
# Which means that I've assumed that all decrypted files do not start with \x00
replace_separator = True


# Search for "F3 0F7F 0B" in MuseSamplerCoreLib.dll which follows "48 83 C3 10"
# I found 3 addresses in MuseSamplerCoreLib.dll that match the above pattern
# The first one is the correct one

session = frida.attach("MuseScore4.exe")

script_code_find_addr = """
var modules = Process.enumerateModulesSync();
function toUTF16(inputString) {
    const utf16CodeUnits = [];
    for (let i = 0; i < inputString.length; i++) {
        const charCode = inputString.charCodeAt(i);
        utf16CodeUnits.push(charCode & 0xff);
        utf16CodeUnits.push((charCode >> 8) & 0xff);
    }
    return new Uint8Array(utf16CodeUnits);
}
for (var i = 0; i < modules.length; i++) {
    var module = modules[i];
    if (module.name === "MuseSamplerCoreLib.dll") {
        var base = module.base;
        var pattern = "F3 0F 7F 0B 48 83 C3 10";
        var matches = Memory.scanSync(base, module.size, pattern);
        for (var j = 0; j < matches.length; j++) {
            send("match", toUTF16(matches[j].address.sub(module.base).add(4).toString()));
        }
        break;
    }
}
send("find_done");
"""
found_event = threading.Event()
addr_auto = ""
def on_message_find_addr(message, data):
    if message["type"] == "send" and message["payload"] == "match":
        print(f"Found address: MuseSamplerCoreLib.dll+{data.decode('utf-16')[2:]}")
        global addr_auto
        if not addr_auto:
            addr_auto = data.decode("utf-16")
    if message["type"] == "send" and message["payload"] == "find_done":
        found_event.set()
script_find_addr = session.create_script(script_code_find_addr)
script_find_addr.on("message", on_message_find_addr)
script_find_addr.load()
found_event.wait()
script_find_addr.unload()
if not addr_auto:
    print("Failed to find address automatically")
    sys.exit(1)
print(f"Using address: MuseSamplerCoreLib.dll+{addr_auto[2:]}")


script_code = """
var create_ui8array = () => {
    var data = new Object();
    data.array = new Uint8Array(0);
    data.length = 0;
    data.append_ui8arr = function (ui8arr) {
        if (this.array.length < this.length + ui8arr.length) {
            var new_array = new Uint8Array(Math.ceil((this.length + ui8arr.length) / 8192) * 8192);
            new_array.set(this.array);
            new_array.set(ui8arr, this.length);
            this.array = new_array;
            this.length += ui8arr.length;
        }
        else {
            this.array.set(ui8arr, this.length);
            this.length += ui8arr.length;
        }
    };
    data.get_ui8arr = function () {
        return this.array.slice(0, this.length);
    };
    return data;
};
var is_xml_start = (arrbuf) => {
    const xml_start = new Uint8Array([0x3c, 0x3f, 0x78, 0x6d, 0x6c, 0x20, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x3d, 0x22, 0x31]);
    // <?xml version="1
    return (new Uint8Array(arrbuf)).slice(0, 16).every((v, i) => v === xml_start[i]);
};
(function () {
    var step_by_step = false;
    var register_sbs = msg => {
        step_by_step = msg.payload;
        if (step_by_step)
            send("step_by_step_true");
        else
            send("step_by_step_false");
        recv('step_by_step', register_sbs);
    };
    recv('step_by_step', register_sbs);

    var fast_mode = false;
    var register_fm = msg => {
        fast_mode = msg.payload;
        if (fast_mode)
            send("fast_mode_true");
        else
            send("fast_mode_false");
        recv('fast_mode', register_fm);
    };
    recv('fast_mode', register_fm);

    var read_bytes = create_ui8array();
    var sending_latest = false;
    var register_rl = msg => {
        sending_latest = true;
        send("decode", read_bytes.get_ui8arr());
        read_bytes = create_ui8array();
        sending_latest = false;
        recv('get_latest', register_rl);
    };
    recv('get_latest', register_rl);

    var replace_bytes = new Uint8Array();
    var register_replace = msg => {
        var new_replace_bytes = new Uint8Array(Math.ceil((replace_bytes.length + msg.payload.length) / 16) * 16);
        new_replace_bytes.set(replace_bytes, 0);
        new_replace_bytes.set(msg.payload, replace_bytes.length);
        replace_bytes = new_replace_bytes;
        recv('replace_bytes', register_replace);
    };
    recv('replace_bytes', register_replace);

    var replace_xml = new Uint8Array();
    var replacing_xml = false;
    var register_replace_xml = msg => {
        var new_replace_xml = new Uint8Array(Math.ceil((replace_xml.length + msg.payload.length) / 16) * 16);
        new_replace_xml.set(replace_xml, 0);
        new_replace_xml.set(msg.payload, replace_xml.length);
        replace_xml = new_replace_xml;
        recv('replace_xml', register_replace_xml);
    };
    recv('replace_xml', register_replace_xml);

    var fast_mode_timeout = null;
    var last_addr = ptr("0x0");

    var injected = Interceptor.attach(Module.findBaseAddress("MuseSamplerCoreLib.dll").add(%s), {
        onEnter: function (args) {
            var addr = ptr(this.context.rbx);

            if (!replacing_xml && replace_xml.length > 0 && is_xml_start(addr.readByteArray(16)))
                replacing_xml = true;
            if (replace_xml.length < 16 && replace_xml.length > 0) {
                var replace_xml_16 = new Uint8Array(16);
                replace_xml_16.set(replace_xml, 0);
                replace_xml = replace_xml_16;
            }
            else if (replace_xml.length === 0 && replacing_xml)
                replacing_xml = false;

            if (replacing_xml) {
                addr.writeByteArray(replace_xml.slice(0, 16));
                replace_xml = replace_xml.slice(16);
            }
            else if (replace_bytes.length > 0) {
                if (replace_bytes.length < 16) {
                    var replace_bytes_16 = new Uint8Array(16);
                    replace_bytes_16.set(replace_bytes, 0);
                    replace_bytes = replace_bytes_16;
                }
                addr.writeByteArray(replace_bytes.slice(0, 16));
                replace_bytes = replace_bytes.slice(16);
            }

            var buf = new Uint8Array(addr.readByteArray(16));
%s
            while (sending_latest) {}

            if (fast_mode) {
                read_bytes.append_ui8arr(buf);

                if (!step_by_step) {
                    if (fast_mode_timeout !== null) {
                        clearTimeout(fast_mode_timeout);
                    }
                    fast_mode_timeout = setTimeout(() => {
                        if (read_bytes.length > 0) {
                            send("decode", read_bytes.get_ui8arr());
                            read_bytes = create_ui8array();
                        }
                        send("no_new_data");
                    }, 1000);
                }
            }
            else {
                if (read_bytes.length > 0) {
                    sending_latest = true;
                    send("decode", read_bytes.get_ui8arr());
                    read_bytes = create_ui8array();
                    sending_latest = false;
                }
                send("decode", buf);
            }

            last_addr = addr;

            if (step_by_step) {
                send("step_by_step_waiting");
                recv('continue', () => {}).wait();
            }
        }
    });
    recv('quit', msg => injected.detach());
})();
""" % (
    addr_auto,
    """
            if (!last_addr.equals(0x0) && !last_addr.add(0x10).equals(addr) && !addr.add(0xf0).equals(last_addr)) {
                buf = Uint8Array.from(Array.prototype.concat([0], Array.from(buf)));
            }
    """ if replace_separator else ""
)
out = b""
has_end = True
read_lock = threading.RLock()


def on_message(message, data):
    global out, has_end, step_by_step_waiting
    with read_lock:
        if message["type"] == "send" and message["payload"] == "decode":
            if has_end:
                data = data.lstrip(b"\x00")
            out += data
            if print_output:
                print(re.sub(b"\\x00+", b"\n" + b"-" * 20 + b"\n", data).decode("utf-8"), end="", flush=True)
                if data.endswith(b"\x00"):
                    has_end = True
                else:
                    has_end = False
            else:
                print(".", end="", flush=True)
        elif message["type"] == "send" and message["payload"] == "step_by_step_waiting":
            step_by_step_waiting = True
        elif message["type"] == "send" and message["payload"] == "step_by_step_true":
            print("Step-by-step mode enabled", file=sys.stderr)
        elif message["type"] == "send" and message["payload"] == "step_by_step_false":
            print("Step-by-step mode disabled", file=sys.stderr)
        elif message["type"] == "send" and message["payload"] == "fast_mode_true":
            print("Fast mode enabled", file=sys.stderr)
        elif message["type"] == "send" and message["payload"] == "fast_mode_false":
            print("Fast mode disabled", file=sys.stderr)
        elif message["type"] == "send" and message["payload"] == "no_new_data":
            print("No new decrypted data in 1s", file=sys.stderr)
        else:
            print(message, data, sep="\n", file=sys.stderr)


script = session.create_script(script_code, runtime="v8")
script.on("message", on_message)
script.load()

step_by_step = False
step_by_step_waiting = False
fast_mode = False


help_msg = """\
'?' - help
'q' - quit
'w' - write output to file
's' - Switch step-by-step mode
'f' - Switch fast mode (Only retrieve decrypted data when user requests)
'g' - Retrieve latest decrypted data (fast mode)
'r' - Overwrite decrypted data with file content
'x' - Overwrite next decrypted xml with file content
'e' - Manually add a separator
'Enter' - Continue (step-by-step mode)
"""
print("Press the following keys for respective actions", file=sys.stderr)
print(help_msg, file=sys.stderr)
while True:
    r = msvcrt.getwch()
    if r == "q" or r == "\x03":
        break
    elif r == "?":
        print(help_msg, file=sys.stderr)
    elif r == "w":
        if out_name:
            with read_lock:
                if replace_separator:
                    out = re.sub(b"\\x00+", b"\n" + b"-" * 20 + b"\n", out)
                with open(out_name, mode="wb") as f:
                    f.write(out)
                out = b""
                has_end = True
            print(f"Output saved to {out_name}")
    elif r == "s":
        step_by_step = not step_by_step
        script.post({"type": "step_by_step", "payload": step_by_step})
    elif r == "f":
        fast_mode = not fast_mode
        script.post({"type": "fast_mode", "payload": fast_mode})
    elif r == "g":
        if fast_mode:
            script.post({"type": "get_latest"})
    elif r == "\r" or r == "\n":
        if step_by_step_waiting:
            step_by_step_waiting = False
            script.post({"type": "continue"})
    elif r == "r":
        print("Input a file name to overwrite decrypted data with file content", file=sys.stderr)
        print("File length should be a multiple of 16, or it will be padded with \\x00", file=sys.stderr)
        file_name = input()
        try:
            with open(file_name, mode="rb") as f:
                replace_bytes = f.read()
                script.post({"type": "replace_bytes", "payload": list(replace_bytes)})
        except FileNotFoundError:
            print("File not found", file=sys.stderr)
    elif r == "x":
        print("Input a file name to overwrite next decrypted xml with file content", file=sys.stderr)
        print("File length should be a multiple of 16, or it will be padded with \\x00", file=sys.stderr)
        print("The next decrypted xml (starting with '<?xml version=\"1') will be replaced", file=sys.stderr)
        print("This takes higher priority than 'r' command", file=sys.stderr)
        file_name = input()
        try:
            with open(file_name, mode="rb") as f:
                replace_xml = f.read()
                script.post({"type": "replace_xml", "payload": list(replace_xml)})
        except FileNotFoundError:
            print("File not found", file=sys.stderr)
    elif r == "e":
        if out and out[-1] != b"\x00":
            out += b"\x00"
            print("\n" + "-" * 20, flush=True)
    else:
        print("Unknown command", file=sys.stderr)

script.post({"type": "quit"})
script.unload()
session.detach()
