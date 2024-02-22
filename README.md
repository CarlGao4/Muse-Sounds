# Muse-Sounds

The Muse Sounds soundfont in sf2 and sf3 format only for research purpose

## Why this repo

The Muse Sounds library was released along with MuseScore Studio 4 and is a very high-quality soundfont. However, the library can only be used in MuseScore Studio 4 as it is distributed under internal format and could only be rendered with the "MuseSamplerCoreLib" (Actually, you can use Muse Sounds as long as you can load the MuseSampler API, which is undocumented but you can retrieve it by reading MuseScore Studio source code). This audio backend is not perfect yet, like it doesn't support per-note velocity. So converting the internal format into general soundfont formats without causing quality loss is the mission of this project. With this project, it will also be easier to edit the soundfont and use it in other software.

**This repository DOES NOT contain any license and is only for research purpose. You must follow the license of the original Muse Sounds library.**

## Help needed

I'm not so familiar with sfz and soundfont formats, so my output SF2 and SF3 sounds may not be perfect. If you find any problems, please open an issue or pull request.

## Downloads

See [instruments](instruments.md) for the list of instruments and download links.

### Release files

I use different versions to upload different instruments. Until now, each version contains only one instrument and each instrument may contain multiple files. Here is an explanation of the files:

- `*.sts.7z`: The compressed opus files. See [Folder structure](#folder-structure) for more information.
- `*.sf2`: The soundfont in SF2 format. See [SF2 and SF3](#sf2-and-sf3) for more information.
- `*.sf3`: The soundfont in SF3 format. See [SF2 and SF3](#sf2-and-sf3) for more information.
- `*_sfz+flac.zip`: Converted sfz file and flac files. I add this file because the original sfz file is not standard and may not be supported by some software, and not all software supports opus files. This file is ready-to-use, which means that you can directly unpack it (with the folder structure) and load it with a sfz player. The zip is not compressed at all.

## Folder structure

This is an example of the folder structure of original Muse Sounds library:

```plaintext
Instruments
├── .instrument  # A SQLite database file containing instrument metadata.
│                # TODO: I don't know how to read SQLite databases. 
│                # Waiting for someone to decode it.
├── Muse Keys
│   ├── Piano
│   │   ├── Piano.spx  # Encrypted, archive of sfz files
│   │   └── SFZ
│   │       └── Piano.sts  # Archive of opus files
│   ├── Celesta
│   │   ├── ...
│   └── ...
├── Muse Strings
│   ├── Violins 1
│   │   ├── ...
│   └── ...
└── ...
```

Until now, there are 4 soundfonts has different folder structures. `Electric LP - Heavy` `Electric LP - Lead` `Electric SC - Heavy` `Electric SC - Lead` only have spx file (which means that they share samples with other soundfonts).

And this is an example of the folder structure of the converted soundfont:

```plaintext
SFZ
├── Muse Keys
│   ├── Piano
│   │   ├── Piano.spx  # This is a folder now
│   │   │   └── SFZ
│   │   │       └── Piano - Studio.sfz  # The extracted sfz file
│   │   ├── Piano.spx.files.txt  # A file containing file list of Piano.spx
│   │   ├── metadata.xml  # I found this file inside spx, but I don't know what it is
│   │   └── SFZ
│   │       ├── Piano.sts.7z  # The compressed opus files, uploaded to the release page
│   │       └── files.txt  # A file to tell you that you should download and extract the 7-Zip file here
│   └── ...
└── ...
```

### Decoded files explanation

- `Piano.spx` folder: As the original file is an encrypted archive, it actually contains more than one file. So I will extract the archive into the folder keeping the original file name and structure.
- `Piano - Studio.sfz`: This is the extracted sfz file. It is a text file and can be opened with any text editor. However, it is not a standard sfz file.
- The opus files in the `Piano.sts` archive will be compressed into 7-Zip format and uploaded to [release](https://github.com/CarlGao4/Muse-Sounds/releases).

In fact, if you want to use a soundfont, you should save all files under `SFZ` in the same folder (like the diagram below). I keep the original folder structure to make it easier to match the original files.

```plaintext
Piano
└── SFZ
    ├── Piano - Studio.sfz
    ├── Steinway_Mixed_ff_up_A#0.opus
    ├── Steinway_Mixed_ff_up_A#1.opus
    ├── ...
    └── Steinway_Mixed_ppp_up_C8.opus
```

## SF2 and SF3

I will also convert the soundfont into SF2 and SF3 formats as they are more common and can be used in more software. However, these formats will be lossy but the loss can be ignored in most cases. I'll use 24-bit wav as the audio format in SF2.

The loss of SF2 format comes from conversion from opus to 24-bit wav. Though both Muse Sounds and SF3 use opus as the audio format, I can't find a way to directly use opus in SF3, but have to compress the SF2 into SF3.

I will keep only one instrument in each SF2 or SF3 file. The reason is that the original Muse Sounds library is too large and contains too many files, exceeding the limit of SF2 and SF3 formats.

You can download SF2 and SF3 soundfonts from [release](https://github.com/CarlGao4/Muse-Sounds/releases), though you may prefer a table of contents: [instruments](instruments.md).

## How I extract the soundfont

### `sts`

See [sts](sts.md) for more information.

### `spx`

Actually, I didn't find out how this file is encrypted. Instead, I used [frida](https://frida.re/) and other deassemblers to trace the MuseSamplerCoreLib and read the memory.

I've created a demo Python script ([read-decrypted-sfz.py](read-decrypted-sfz.py)) to capture all decrypted chunks by reading the memory. The script is only designed for Windows and MuseSampler version `0.5.1`. To use it, you will need to start MuseScore Studio 4 and run the script (You may need to install `frida-tools`).

If your MuseSampler version is different, you can download version `0.5.1` from [release](https://github.com/CarlGao4/Muse-Sounds/releases/tag/MuseSamplerCoreLib) and replace the MuseSamplerCoreLib.dll file (usually located at `C:\Windows\System32\`).
