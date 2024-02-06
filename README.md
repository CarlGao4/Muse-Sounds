# Muse-Sounds

The Muse Sounds soundfont only for research purpose

## Why this repo

The Muse Sounds library was released along with MuseScore Studio 4 and is a very high-quality soundfont. However, the library can only be used in MuseScore Studio 4 as it is distributed under internal format and could only be rendered with the "MuseSamplerCoreLib" (Actually, you can use Muse Sounds as long as you can load the MuseSampler API, which is undocumented but you can retrieve it by reading MuseScore Studio source code). This audio backend is not perfect yet, like it doesn't support per-note velocity. So converting the internal format into general soundfont formats without causing quality loss is the mission of this project. With this project, it will also be easier to edit the soundfont and use it in other software.

**This repository DOES NOT contain any license and is only for research purpose. You must follow the license of the original Muse Sounds library.**

## Help needed

I'm not so familiar with sfz and soundfont formats, so my output SF2 and SF3 sounds may not be perfect. If you find any problems, please open an issue or pull request.

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

And this is an example of the folder structure of the converted soundfont:

```plaintext
SFZ
├── Muse Keys
│   ├── Piano
│   │   ├── Piano.spx  # This is a folder now
│   │   │   └── SFZ
│   │   │       └── Piano - Studio.sfz  # The extracted sfz file
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

I will also convert the soundfont into SF2 and SF3 formats as they are more common and can be used in more software. However, these formats will be lossy but the loss can be ignored in most cases.

The loss of SF2 format comes from conversion from opus to 24-bit wav. Though both Muse Sounds and SF3 use opus as the audio format, I can't find a way to directly use opus in SF3, but have to compress the SF2 into SF3.

I will keep only one instrument in each SF2 or SF3 file. The reason is that the original Muse Sounds library is too large and contains too many files, exceeding the limit of SF2 and SF3 formats.

You can download SF2 and SF3 soundfonts from [release](https://github.com/CarlGao4/Muse-Sounds/releases).

## How I extract the soundfont

### `sts`

See [sts](sts.md) for more information.

### `spx`

**TODO**
