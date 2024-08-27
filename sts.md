# `sts` format

**This is not official documentation.** This is a reverse-engineered documentation of the `sts` format used in the Muse Sounds library. The original documentation is not available.

**`Muse Drumline` uses a new format which haven't been decrypted**. It seems that the new format stores its TOC in the corresponding `spx` file, and the `sts` file only contains encrypted data. I haven't found a way to decrypt the new format yet.

## Structure

The file has three parts:

```
+--------+-------+--------+
| Header |  TOC  |  Data  |
+--------+-------+--------+
```

All numbers mentioned below are little-endian encoded.

### Header

A fixed 24-byte binary string. In hex:

```
14 00 00 00 53 41 61 66 66 50 61 64 20 53 61 6D
70 6C 65 20 46 69 6C 65
```

My understanding of the string:

1. An `int32` number showing that the string after this number is `0x14` (18) bytes long
2. The human-readable text (`StaffPad Sample File`)

### TOC (Table of contents)

This part is concatenated from a number of units. Before the units, there is a `int32` number showing how many units are there.

The structure of each unit looks like this:

1. An `int32` number showing the length of the file name.
2. File name, without a delimiter
3. An `int64` number showing the begin byte of the file (inclusive) in this sts file
4. An `int64` number showing the end byte of the file (exclusive) in this sts file

Example extracted from `Piano.sts` (hex):
```
1C 00 00 00 53 74 65 69 6E 77 61 79 5F 4D 69 78
65 64 5F 66 5F 75 70 5F 41 23 30 2E 6F 70 75 73
40 74 00 00 00 00 00 00 85 9D 05 00 00 00 00 00
```

### Data

All files concatenated without a delimiter

## Example extractor (Python)

```Python
#!/bin/python3
# sts-extractor.py
# Muse Sounds sts extractor
# See https://github.com/CarlGao4/Muse-Sounds

import pathlib
import struct
import sys

if len(sys.argv) != 2:
    print("Muse Sounds sts extractor", file=sys.stderr)
    print("Usage: sts-extractor.py [sts file]")
    sys.exit(1)

sts = pathlib.Path(sys.argv[1])
out_folder = sts.resolve().parent
f = open(sts, mode="rb")
assert f.read(24) == b"\x14\x00\x00\x00StaffPad Sample File"
last_len = 0
for _ in range(struct.unpack("<i", f.read(4))[0]):
    name_len = struct.unpack("<i", f.read(4))[0]
    name = f.read(name_len).decode()
    print(name, end="", file=sys.stderr)
    print(" " * max(0, last_len - len(name)), end="\r", file=sys.stderr)
    last_len = len(name)
    out = out_folder / name
    out.parent.mkdir(parents=True, exist_ok=True)
    begin, end = struct.unpack("<qq", f.read(16))
    back = f.tell()
    f.seek(begin)
    out.write_bytes(f.read(end - begin))
    f.seek(back)
f.close()
```

## Example script to archive

See [create-sts.py](create-sts.py) for an example script to archive files into `sts` format.
