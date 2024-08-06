# create-sts.py
# A demo script to create a sts archive from a list of files
# Visit https://github.com/CarlGao4/Muse-Sounds for more information

import os
import pathlib
import struct
import sys

if len(sys.argv) != 3:
    print("Usage: python create-sts.py <list.txt> <output.sts>", file=sys.stderr)
    print("list.txt: A list of files to be archived, must be relative paths to the txt", file=sys.stderr)
    print("output.sts: The output sts archive", file=sys.stderr)
    sys.exit(1)

list_file = pathlib.Path(sys.argv[1]).resolve()
out_file = pathlib.Path(sys.argv[2]).resolve()
os.chdir(os.path.dirname(list_file))
with open(list_file, mode="r", encoding="utf-8") as f:
    files = [line.strip().replace("\\", "/") for line in f.read().strip().splitlines()]

if len(set(files)) != len(files):
    print("Duplicate files in the list", file=sys.stderr)
    sys.exit(1)

file_lengths = []
for file in files:
    if ".." in file:
        print(f"Invalid file path: {file}", file=sys.stderr)
        sys.exit(1)
    if sys.platform == "win32":
        if len(file) >= 2 and file[1] == ":":
            print(f"Must use relative paths: {file}", file=sys.stderr)
            sys.exit(1)
    else:
        if file.startswith("/"):
            print(f"Must use relative paths: {file}", file=sys.stderr)
            sys.exit(1)
    if not os.path.exists(file):
        print(f"File not found: {file}", file=sys.stderr)
        sys.exit(1)
    file_lengths.append(os.path.getsize(file))

header_length = 24 + 4 + sum(map(len, files)) + len(files) * (4 + 8 + 8)
begins = [header_length]
for length in file_lengths:
    begins.append(begins[-1] + length)

with open(out_file, mode="wb") as f:
    f.write(b"\x14\x00\x00\x00StaffPad Sample File")
    f.write(struct.pack("<i", len(files)))
    for i in range(len(files)):
        f.write(struct.pack("<i", len(files[i])))
        f.write(files[i].encode("utf-8"))
        f.write(struct.pack("<qq", begins[i], begins[i + 1]))
    last_len = 0
    for i in files:
        print(" " * last_len, end="\r", flush=True, file=sys.stderr)
        print(i, end="\r", flush=True, file=sys.stderr)
        last_len = len(i)
        with open(i, mode="rb") as g:
            f.write(g.read())
print(" " * last_len, end="\r", flush=True, file=sys.stderr)
print(f"Done. File size: {begins[-1]}", file=sys.stderr)
