# read-decrypted-sfz.py
# A demo script to read decrypted spx from MuseScore4 memory
# Designed for Windows only
# Visit https://github.com/CarlGao4/Muse-Sounds for more information

import frida
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
    var last_addr = ptr("0x0");
    Interceptor.attach(Module.findBaseAddress("MuseSamplerCoreLib.dll").add(%s), {
        onEnter: function (args) {
            var addr = ptr(this.context.rbx);
            const buf = addr.readByteArray(16);
            if (last_addr.equals(0x0) || last_addr.add(0x10).equals(addr) || addr.add(0xf0).equals(last_addr)) {
                send("decode", buf);
            }
            else {
                send("decode_new", buf);
            }
            last_addr = addr;
        }
    });
})();
""" % addr_auto
out = b""
has_end = True
read_lock = threading.RLock()


def on_message(message, data):
    global out, has_end
    with read_lock:
        if message["type"] == "send" and message["payload"].startswith("decode"):
            if message["payload"] == "decode_new":
                if not has_end:
                    out += b"\x00"
                    print("\n" + "-" * 20)
            out += data
            if print_output:
                print(data.rstrip(b"\x00").decode("utf-8"), end="")
                if data.endswith(b"\x00"):
                    print("\n" + "-" * 20)
                    has_end = True
                else:
                    has_end = False
        else:
            print(message, data, sep="\n", file=sys.stderr)


script = session.create_script(script_code)
script.on("message", on_message)
script.load()

while True:
    r = input("Press Enter to write out file, enter q to stop monitoring")
    if r == "q":
        break
    if out_name:
        with read_lock:
            if replace_separator:
                out = re.sub(b"\\x00+", b"\n" + b"-" * 20 + b"\n", out)
            with open(out_name, mode="wb") as f:
                f.write(out)
            out = b""
            has_end = True

script.unload()
session.detach()
