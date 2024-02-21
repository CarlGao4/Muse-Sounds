# read-decrypted-sfz.py
# A demo script to read decrypted spx from MuseScore4 memory
# Designed for Windows only, MuseSampler version 0.5.1
# Visit https://github.com/CarlGao4/Muse-Sounds for more information

import frida
import sys

assert sys.platform == "win32", "This script is for Windows only"

script_code = """
Interceptor.attach(Module.findBaseAddress("MuseSamplerCoreLib.dll").add(0x205772), {
    onEnter: function (args) {
        const buf = ptr(this.context.rbx).readByteArray(16);
        send("decode", buf);
    }
});
"""
session = frida.attach("MuseScore4.exe")
out = b""


def on_message(message, data):
    global out
    if message["type"] == "send" and message["payload"] == "decode":
        out += data


script = session.create_script(script_code)
script.on("message", on_message)
script.load()

input("Press Enter to stop monitoring and save captured outputs to decrypted.out (overwrite)")
with open("decrypted.out", mode="wb") as f:
    f.write(out)
