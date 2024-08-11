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
print_output = True
# TODO: Output file name, set this to empty string if you don't want to save the output
out_name = "decrypted.out"
# TODO: Set this to False if you don't want to replace separator (\x00) with newline and a line of dashes
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
    var replace_bytes = new Uint8Array();
    var register_replace = msg => {
        var new_replace_bytes = new Uint8Array(msg.payload.length + replace_bytes.length);
        new_replace_bytes.set(replace_bytes, 0);
        new_replace_bytes.set(msg.payload, replace_bytes.length);
        replace_bytes = new_replace_bytes;
        recv('replace_bytes', register_replace);
    };
    recv('replace_bytes', register_replace);
    var last_addr = ptr("0x0");
    var injected = Interceptor.attach(Module.findBaseAddress("MuseSamplerCoreLib.dll").add(%s), {
        onEnter: function (args) {
            var addr = ptr(this.context.rbx);
            if (replace_bytes.length > 0) {
                if (replace_bytes.length < 16) {
                    var replace_bytes_16 = new Uint8Array(16);
                    replace_bytes_16.set(replace_bytes, 0);
                    replace_bytes = replace_bytes_16;
                }
                addr.writeByteArray(replace_bytes.slice(0, 16));
                replace_bytes = replace_bytes.slice(16);
            }
            const buf = addr.readByteArray(16);
            if (last_addr.equals(0x0) || last_addr.add(0x10).equals(addr) || addr.add(0xf0).equals(last_addr)) {
                send("decode", buf);
            }
            else {
                send("decode_new", buf);
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
""" % addr_auto
out = b""
has_end = True
read_lock = threading.RLock()


def on_message(message, data):
    global out, has_end, step_by_step_waiting
    with read_lock:
        if message["type"] == "send" and message["payload"].startswith("decode"):
            if message["payload"] == "decode_new":
                if not has_end:
                    out += b"\x00"
                    print("\n" + "-" * 20)
            out += data
            if print_output:
                print(data.rstrip(b"\x00").decode("utf-8"), end="", flush=True)
                if data.endswith(b"\x00"):
                    print("\n" + "-" * 20, flush=True)
                    has_end = True
                else:
                    has_end = False
        elif message["type"] == "send" and message["payload"] == "step_by_step_waiting":
            step_by_step_waiting = True
        elif message["type"] == "send" and message["payload"] == "step_by_step_true":
            print("Step-by-step mode enabled")
        elif message["type"] == "send" and message["payload"] == "step_by_step_false":
            print("Step-by-step mode disabled")
        else:
            print(message, data, sep="\n", file=sys.stderr)


script = session.create_script(script_code)
script.on("message", on_message)
script.load()

step_by_step = False
step_by_step_waiting = False


def input_with_getch(prompt=""):
    print(prompt, end="", flush=True)
    r = b""
    while True:
        r += msvcrt.getch()
        if r.endswith(b"\r") or r.endswith(b"\n"):
            return r[:-1]
        if r.endswith(b"\x03"):
            raise KeyboardInterrupt


print("Press '?' for help, 'q' to quit", file=sys.stderr)
while True:
    r = msvcrt.getch()
    if r == b"q" or r == b"\x03":
        break
    elif r == b"?":
        print("'?' - help", file=sys.stderr)
        print("'q' - quit", file=sys.stderr)
        print("'w' - write output to file", file=sys.stderr)
        print("'s' - Switch step-by-step mode", file=sys.stderr)
        print("'r' - Overwrite decrypted data with file content", file=sys.stderr)
        print("'Enter' - Continue (step-by-step mode)", file=sys.stderr)
    elif r == b"w":
        if out_name:
            with read_lock:
                if replace_separator:
                    out = re.sub(b"\\x00+", b"\n" + b"-" * 20 + b"\n", out)
                with open(out_name, mode="wb") as f:
                    f.write(out)
                out = b""
                has_end = True
            print(f"Output saved to {out_name}")
    elif r == b"s":
        step_by_step = not step_by_step
        script.post({"type": "step_by_step", "payload": step_by_step})
    elif r == b"\r" or r == b"\n":
        if step_by_step_waiting:
            step_by_step_waiting = False
            script.post({"type": "continue"})
    elif r == b"r":
        print("Input a file name to overwrite decrypted data with file content", file=sys.stderr)
        print("File length should be a multiple of 16, or it will be padded with \\x00", file=sys.stderr)
        file_name = input()
        try:
            with open(file_name, mode="rb") as f:
                replace_bytes = f.read()
                script.post({"type": "replace_bytes", "payload": list(replace_bytes)})
        except FileNotFoundError:
            print("File not found", file=sys.stderr)
    else:
        print("Unknown command", file=sys.stderr)

script.post({"type": "quit"})
script.unload()
session.detach()
