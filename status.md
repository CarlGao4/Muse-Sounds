# Project Status

## Extracted versions

Up until now, I've extracted the following versions:
- Muse Brass `0.4.4`
- Muse Choir `0.3.19`
- Muse Guitars Vol. 1 `0.9.8`
- Muse Harp `0.2.7`
- Muse Keys `0.4.11`
- Muse Percussion `0.5.10`
- Muse Strings `0.4.14`
- Muse Woodwinds `0.5.23`

### Muse Sounds Bugs I've found

Muse Choir `0.3.18` has a problem that Women soundfont doesn't have any sound if the note belongs to Soprano range because Soprano has been renamed from Sopranos but the sfz file still uses Sopranos. It has been renamed back in `0.3.19` version.

Muse Percussion `0.5.10` Mark Tree has a problem that `SFZ\Mark Tree - Rolls - Gliss Down.sfz` takes higher priority than `SFZ\Mark Tree - Hits - Gliss Down.sfz` when adding "ArpgeggioDown"

## About the uploaded files

Up until now, I've uploaded all the metadata file to this repo (See [SFZ folder](SFZ)), and their sample file (`*.sts`) has been extracted and rearchived to 7-Zip format, which is uploaded to the release page. To see the full list, see [instruments](instruments.md).

Some of the soundfonts have been converted to SF2 and SF3 format, and uploaded to the release page. I don't guarantee that the converted soundfonts can sound exactly the same as the original soundfonts. To see the full list, see [instruments](instruments.md).

I've also extracted some of the soundfonts in SFZ format, and uploaded to this repo. These are the "non-standard" SFZ files, which means that they may not be supported by some software. See [SFZ folder](SFZ) for theses files.

### Uploaded original SFZ files

If an instrument is not listed here, it means that it doesn't have its own SFZ file or I haven't noticied that instrument.

These SFZ files are **NOT** standard and should be modified before using in other software.

Instruments in *italic* means that some SFZ files are not extracted. See below [SFZ files failed to extract or convert](#sfz-files-failed-to-extract-or-convert) for more information. The number comes after the instrument name is the the count of unextracted SFZ files.

- [ ] Muse Brass `0.4.4`
  - [ ] Bass Trombone
  - [ ] Cimbasso
  - [ ] Horn in F
  - [ ] Horns a6
  - [ ] Trombone
  - [ ] Trombones a3
  - [ ] Trumpet
  - [ ] Trumpets a4
  - [ ] Tuba
- [x] Muse Choir `0.3.19`
  - [x] *Altos* (4)
  - [x] *Basses* (4)
  - [x] *Sopranos* (4)
  - [x] *Tenors* (4)
- [ ] Muse Guitars Vol. 1 `0.9.8`
  - [ ] Acoustic Nylon
  - [ ] Acoustic Steel Picked
  - [ ] Acoustic Steel Plucked
  - [ ] Electric Bass
  - [ ] Electric LP - Clean
  - [ ] Electric SC - Clean
- [x] Muse Harp `0.2.7`
  - [x] Harp
- [x] Muse Keys `0.4.11`
  - [x] Celesta
  - [x] Crotales
  - [x] Dream Piano
  - [x] *Grand Piano* (1)
  - [x] Hammond Organ
  - [x] Harpsichord
  - [x] Soft Piano
  - [x] Suitcase Piano
  - [x] Upright Piano
  - [x] Wurly 200A
- [x] Muse Percussion `0.5.10`
  - [x] Bass Drum
  - [x] Bell Tree
  - [x] Bongos
  - [x] Cabasa
  - [x] Castanets
  - [x] Claves
  - [x] Cowbell
  - [x] Field Drum
  - [x] Glockenspiel
  - [x] Gong
  - [x] Marimba
  - [x] *Mark Tree* (1)
  - [x] Metronome
  - [x] Piatti
  - [x] Shaker
  - [x] Sleigh Bells
  - [x] Snare Drum
  - [x] Sus. Cymbal
  - [x] Taikos
  - [x] Tam-tam
  - [x] Tambourine
  - [x] Timbales
  - [x] Timpani
  - [x] Toms
  - [x] Triangle
  - [x] Tubular Bells
  - [x] Vibraphone
  - [x] Wood Blocks
  - [x] Xylophone
- [ ] Muse Strings `0.4.14`
  - [ ] Contrabasses
  - [ ] Viola (Solo)
  - [ ] Violas
  - [ ] Violin 1 (Solo)
  - [ ] Violin 2 (Solo)
  - [x] *Violins 1* (2)
  - [ ] Violins 2
  - [ ] Violoncello (Solo)
  - [ ] Violoncellos
- [ ] Muse Woodwinds `0.5.23`
  - [ ] Alto Flute
  - [ ] Alto Sax
  - [ ] Baritone Sax
  - [ ] Bass Clarinet
  - [ ] Bass Flute
  - [ ] Bassoon
  - [ ] Clarinet in Bb
  - [ ] Clarinet in Eb
  - [ ] Contrabass Flute
  - [ ] Contrabassoon
  - [ ] English Horn
  - [ ] Flute 1
  - [ ] Flute 2
  - [ ] Oboe
  - [ ] Piccolo
  - [ ] Soprano Sax
  - [ ] Tenor Sax

## SFZ files failed to extract or convert

Some of the soundfonts have failed to extract or convert. Here is the list of them. Instruments which haven't been extracted is not listed.

### Muse Choir

#### Altos

- `SFZ\Altos - Ahh - Staccato.sfz`: Could not activate this file by adding "Staccato" symbol, it will activate `SFZ\Altos - Ahh - Staccatissimo.sfz`.
- `SFZ\Altos - Mmm - Staccato.sfz`: Could not activate this file by adding "Staccato" symbol, it will activate `SFZ\Altos - Mmm - Staccatissimo.sfz`.
- `SFZ\Altos - Ooh - Staccato.sfz`: Could not activate this file by adding "Staccato" symbol, it will activate `SFZ\Altos - Ooh - Staccatissimo.sfz`.
- `SFZ\Altos - Realtime.sfz`: Could not activate this file. I guess that this should require a MIDI keyboard to activate.

#### Basses

- `SFZ\Basses - Ahh - Staccato.sfz`: Could not activate this file by adding "Staccato" symbol, it will activate `SFZ\Basses - Ahh - Staccatissimo.sfz`.
- `SFZ\Basses - Mmm - Staccato.sfz`: Could not activate this file by adding "Staccato" symbol, it will activate `SFZ\Basses - Mmm - Staccatissimo.sfz`.
- `SFZ\Basses - Ooh - Staccato.sfz`: Could not activate this file by adding "Staccato" symbol, it will activate `SFZ\Basses - Ooh - Staccatissimo.sfz`.
- `SFZ\Basses - Realtime.sfz`: Could not activate this file. I guess that this should require a MIDI keyboard to activate.

#### Sopranos

- `SFZ\Sopranos - Ahh - Staccato.sfz`: Could not activate this file by adding "Staccato" symbol, it will activate `SFZ\Sopranos - Ahh - Staccatissimo.sfz`.
- `SFZ\Sopranos - Mmm - Staccato.sfz`: Could not activate this file by adding "Staccato" symbol, it will activate `SFZ\Sopranos - Mmm - Staccatissimo.sfz`.
- `SFZ\Sopranos - Ooh - Staccato.sfz`: Could not activate this file by adding "Staccato" symbol, it will activate `SFZ\Sopranos - Ooh - Staccatissimo.sfz`.
- `SFZ\Sopranos - Realtime.sfz`: Could not activate this file. I guess that this should require a MIDI keyboard to activate.

#### Tenors

- `SFZ\Tenors - Ahh - Staccato.sfz`: Could not activate this file by adding "Staccato" symbol, it will activate `SFZ\Tenors - Ahh - Staccatissimo.sfz`.
- `SFZ\Tenors - Mmm - Staccato.sfz`: Could not activate this file by adding "Staccato" symbol, it will activate `SFZ\Tenors - Mmm - Staccatissimo.sfz`.
- `SFZ\Tenors - Ooh - Staccato.sfz`: Could not activate this file by adding "Staccato" symbol, it will activate `SFZ\Tenors - Ooh - Staccatissimo.sfz`.
- `SFZ\Tenors - Realtime.sfz`: Could not activate this file. I guess that this should require a MIDI keyboard to activate.

### Muse Keys

#### Grand Piano

- `SFZ\Piano - Realtime.sfz`: Could not activate this file by using "Orchestral" preset.

### Muse Percussion

#### Mark Tree

- `SFZ\Mark Tree - Hits - Gliss Down.sfz`: When trying to activate this file by adding "ArpeggioDown", `SFZ\Mark Tree - Rolls - Gliss Down.sfz` takes higher priority so this file can't be activated.

### Muse Strings

#### Violins 1

- `SFZ\Violins 1 - Fall.sfz` I know that this file could be activated (As I've activated `SFZ\Violins 1 - Sustain Falls.sfz` by opening another mscz file), but I haven't successfully activated these two files by adding "Fall" symbol myself.
- `SFZ\Violins 1 - Realtime.sfz`: Could not activate this file. I guess that this should require a MIDI keyboard to activate.
