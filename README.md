# Muse-Sounds

The Muse Sounds soundfont in sf2 and sf3 format only for research purpose

Extraction status:

[Progress - Instruments ![](https://util.muse-sounds.work/progress/91/91?color=70afea&width=150)](status.md) 91 / 91

[Progress - Files ![](https://util.muse-sounds.work/progress/1256/1256?color=a953ff&width=150)](status.md) 1256 / 1256

**Up until now, all SFZ fils have been extracted and uploaded. Current status is converting into standard formats including SF2 (and SF3) for simple instruments (like Upright Piano), SFZ for complex instruments (like Grand Piano), and VST (Kontakt) for more complex instruments (like Muse Strings). For convertion status and download links, see [instruments](instruments.md).**

**We are migrating hosted files to Cloudflare from GitHub Releases for better performance, and also due to the fact that GitHub limits the maximum file size. However, Cloudflare is not free and approximately costs $50 every year to host the files. If you like this project, please consider [donating](https://paypal.me/CarlGao4).**

## Why this repo

The Muse Sounds library was released along with MuseScore Studio 4 and is a very high-quality soundfont. However, the library can only be used in MuseScore Studio 4 as it is distributed under internal format and could only be rendered with the "MuseSamplerCoreLib" (Actually, you can use Muse Sounds as long as you can load the MuseSampler API, which is undocumented but you can retrieve it by reading MuseScore Studio source code). This audio backend is not perfect yet, like it doesn't support per-note velocity. So converting the internal format into general soundfont formats without causing quality loss is the mission of this project. With this project, it will also be easier to edit the soundfont and use it in other software.

Besides, the Muse Sounds library is too large and contains too many files. For those who would like to compose epic music but not so familiar with all the instruments, it is hard to differentiate the features of each. By showing the structure of the soundfont, it will be easier to make your music more vivid.

**This repository DOES NOT contain any license and is only for research purpose. You must follow the license of the original Muse Sounds library.**

## Difficulties converting Muse Sounds into general soundfont formats

From the extracted metadata file, we can see that maybe more than one SFZ is used even when playing a single note. Besides, a lot of functions of MuseScore Studio haven't been implemented yet (Until now, the latest version is `4.3.2`). For example, I've found three presets (Studio, Pop, Orchestral) in the Grand Piano soundfont, but at that time (MuseScore `4.2.1`) there was no way to switch between them. This function was added in `4.3.0`.

The SFZ files extracted from the `spx` files are not standard. They contain a lot of arguments which normal SFZ files don't have. Besides, it also has "closing brackets". e.g.: normal SFZ file only has `<group>` and all the contents below it are in the group, but the extracted SFZ file has `<group>`, `</group>`, and all the contents between them are in the group. This is not supported by most software.

What's more, the metadata file also defined a series of effects, we even need to guess what it means.

## Help needed

I'm not so familiar with sfz and soundfont formats, so my output SF2 and SF3 sounds may not be perfect. If you find any problems, please open an issue or pull request.

Besides, I also noticed that sf2 and sf3 files are too simple to contain all the features of Muse Sounds. Even sfz format is not enough. I'm now considering using VST format (like Kontakt) for more complex soundfonts (like Muse Strings). If you have any ideas, please let me know.

## Downloads

See [status](status.md) for the status of this project and more information about the soundfonts.

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

Until now, there are some soundfonts having different folder structures, which only have spx file (which means that they share samples with other soundfonts).

And this is an example of the folder structure of the converted soundfont:

```plaintext
SFZ
├── Muse Keys
│   ├── Piano
│   │   ├── Piano.spx.files.txt  # A file containing file list of Piano.spx
│   │   ├── metadata.xml  # A file in XML format, I haven't retrieved its name yet
│   │  (├── drum_notes.xml  # Another XML file defining drum notes, only exists in drum soundfonts)
│   │   └── SFZ
│   │       ├── Piano.sts.7z  # The compressed opus files, uploaded for download
│   │       ├── files.txt  # A file to tell you that you should download and extract the 7-Zip file here
│   │       └── Piano - Studio.sfz  # The extracted sfz file, no longer in the "Piano.spx" folder
│   └── ...
└── ...
```

### Decoded files explanation

- `Piano.spx` folder: As the original file is an encrypted archive, it actually contains more than one file. So I will extract the archive into the folder keeping the original file name and structure.
- `Piano - Studio.sfz`: This is the extracted sfz file. It is a text file and can be opened with any text editor. However, it is not a standard sfz file.
- The opus files in the `Piano.sts` archive will be compressed into 7-Zip format and uploaded for download. For download list, please refer to [instruments](instruments.md).

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

You can download SF2 and SF3 soundfonts from [instruments list](instruments.md).

## How I extract the soundfont

### `sts`

See [sts](sts.md) for more information.

### `spx`

Actually, I didn't find out how this file is encrypted. Instead, I used [frida](https://frida.re/) and other deassemblers to trace the MuseSamplerCoreLib and read the memory.

I've created a demo Python script ([read-decrypted-sfz.py](read-decrypted-sfz.py)) to capture all decrypted chunks by reading the memory. The script is only designed for Windows and some MuseSampler versions may fail (e.g. reading from `0.99.5` will cause MuseScore to crash, while `0.100.0` doesn't). To use it, you will need to start MuseScore Studio 4 and run the script (You may need to install `frida-tools`).

If your MuseSampler version is different, you can download from [release](https://github.com/CarlGao4/Muse-Sounds/releases/tag/MuseSamplerCoreLib) for some versions and replace the `MuseSamplerCoreLib.dll` file (usually located at `C:\Windows\System32\` if you are using Muse Hub 1, `%LOCALAPPDATA%\MuseSampler\lib\` for Muse Hub 2).
