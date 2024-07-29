# Project Status

## Extracted versions

Up until now, I've extracted the following versions:
- Muse Strings `0.4.14`
- Muse Harp `0.2.7`
- Muse Choir `0.3.19`
- Muse Guitars Vol. 1 `0.9.8`
- Muse Keys `0.4.11`
- Muse Percussion `0.5.10`
- Muse Brass `0.4.4`
- Muse Woodwinds `0.5.23`

### Muse Sounds Bugs I've found

Muse Choir `0.3.18` has a problem that Women soundfont doesn't have any sound if the note belongs to Soprano range because Soprano has been renamed from Sopranos but the sfz file still uses Sopranos. It has been renamed back in `0.3.19` version.

Muse Percussion `0.5.10` Mark Tree has a problem that `SFZ\Mark Tree - Rolls - Gliss Down.sfz` takes higher priority than `SFZ\Mark Tree - Hits - Gliss Down.sfz` when adding "ArpgeggioDown"

## About the uploaded files

Up until now, I've uploaded all the metadata file to this repo (See [SFZ folder](SFZ)), and their sample file (`*.sts`) has been extracted and rearchived to 7-Zip format, which is uploaded to the release page. To see the full list, see [instruments](instruments.md).

Some of the soundfonts have been converted to SF2 and SF3 format, and uploaded to the release page. I don't guarantee that the converted soundfonts can sound exactly the same as the original soundfonts. To see the full list, see [instruments](instruments.md).

I've also extracted some of the soundfonts in SFZ format, and uploaded to this repo. These are the "non-standard" SFZ files, which means that they may not be supported by some software. See [SFZ folder](SFZ) for theses files.

### Uploaded original SFZ files

- Muse Keys `0.4.11`
  - All
- Muse Percussion `0.5.10`
  - All
- Muse Harp `0.2.7`
  - All
- Muse Choir `0.3.19`
  - Altos

## SFZ files failed to extract or convert

Some of the soundfonts have failed to extract or convert. Here is the list of them. Instruments which haven't been extracted is not listed.

### Muse Choir

#### Altos

- `SFZ\Altos - Ahh - Staccato.sfz`: Could not activate this file by adding "Staccato" symbol, it will activate `SFZ\Altos - Ahh - Staccatissimo.sfz`
- `SFZ\Altos - Ooh - Staccato.sfz`: Could not activate this file by adding "Staccato" symbol, it will activate `SFZ\Altos - Ooh - Staccatissimo.sfz`
- `SFZ\Altos - Mmm - Staccato.sfz`: Could not activate this file by adding "Staccato" symbol, it will activate `SFZ\Altos - Mmm - Staccatissimo.sfz`
- `SFZ\Altos - Realtime.sfz`: Could not activate this file. I guess that this should require a MIDI keyboard to activate.

### Muse Harp

#### Harp

- `SFZ\Harp - Harmonics.sfz`: Could not activate this file by adding "Harmonics" symbol

### Muse Keys

#### Grand Piano

- `SFZ\Piano - Realtime.sfz`: Could not activate this file by using "Orchestral" preset

### Muse Percussion

#### Mark Tree

- `SFZ\Mark Tree - Hits - Gliss Down.sfz`: When trying to activate this file by adding "ArpeggioDown", `SFZ\Mark Tree - Rolls - Gliss Down.sfz` takes higher priority so this file can't be activated.
