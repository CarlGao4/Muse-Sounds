# Muse Sounds SHA1 List

This folder contains the SHA1 list of the original Muse Sounds library. The list is used to check the updated files in the library.

Besides, in many cases, Muse Hub seems do not check the integrity of downloaded soundfonts, so I think it would also be convenient to check the integrity by running the scripts below and view differences of this folder.

This folder is generated like this (Please fill in versions and folder paths before running):

```python
import glob
import hashlib
import itertools
import json
import os
import pathlib

os.chdir("Your Muse Sounds folder")  # TODO: Fill this
hashes = {
    i: list(j)
    for i, j in itertools.groupby(
        (
            (
                i[2:].replace("\\", "/"),
                (os.path.getsize(i), hashlib.sha1(pathlib.Path(i).read_bytes(), usedforsecurity=False).hexdigest()),
            )
            for i in glob.glob("./*/**/*.*", recursive=True)
        ),
        lambda x: x[0].split("/")[0],
    )
}
# TODO: Uncomment this and fill the version number
"""
versions = {
    "Muse Brass": "xxx",
    "Muse Choir": "xxx",
    "Muse Drumline": "xxx",
    "Muse Guitars Vol 1": "xxx",
    "Muse Harp": "xxx",
    "Muse Keys": "xxx",
    "Muse Percussion": "xxx",
    "Muse Strings": "xxx",
    "Muse Woodwinds": "xxx"
}
"""

os.chdir("Your Muse Sounds SHA1 List folder")  # TODO: Fill this

for k, v in hashes.items():
    pathlib.Path(k).mkdir(exist_ok=True)
    with open(f"{k}/{versions[k]}.txt", "wt", encoding="utf-8") as f:
        for n, (s, h) in v:
            f.write(f'{json.dumps(n) + ":":80} {s:10} {h:32}\n')
```
