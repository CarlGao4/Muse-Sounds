# Project Status

## Extracted versions

Up until now, I've extracted the following versions:
- Muse Brass `0.4.4`
- Muse Choir `0.3.19`
- Muse Guitars Vol. 1 `0.9.8`
- Muse Harp `0.2.7`
- Muse Keys `0.4.11`
- Muse Percussion `0.5.10`
- Muse Strings `0.4.17`
- Muse Woodwinds `0.5.23`

### Muse Sounds Bugs I've found

Many instruments have different SFZ files for trills of different intervals, but currently MuseScore Studio 4 (4.3.2) will only load the SFZ file for the first note of trill if the staff has more than one trill symbol and the intervals are different. For example, if you added a trill symbol first to C5 (Which should load SFZ of Major Trill) and then to E5 (Which should load SFZ of Minor Trill), only the SFZ of Major Trill will be loaded. Then the trill of E5 will be simulated with a series of fast notes of E5 and F5.

Muse Brass instruments including Bass Trombone, Cimbasso, Horn in F have different SFZ files for accented notes of different duration. However, the last SFZ file in metadata doesn't have a duration specified, so it will override the previous SFZ files.

Muse Choir `0.3.18` has a problem that Women soundfont doesn't have any sound if the note belongs to Soprano range because Soprano has been renamed from Sopranos but the sfz file still uses Sopranos. It has been renamed back in `0.3.19` version.

Muse Guitars Vol. 1 Electric SC has different presets for dynamics less than 64 and greater than or equal to 64, but currently MuseScore Studio 4 (4.3.2) doesn't support this feature. It only uses the preset for dynamics greater than or equal to 64.

Muse Percussion `0.5.10` Mark Tree has a problem that `SFZ\Mark Tree - Rolls - Gliss Down.sfz` takes higher priority than `SFZ\Mark Tree - Hits - Gliss Down.sfz` when adding "ArpgeggioDown"

Muse Strings `0.4.14` Violins 1 `SFZ\Violins 1 - Sustain Fall.sfz` should only be activated `ForDuration="|4"` according to the metadata file, which I guess means that the note should have a duration equals to or less than 4 16th notes. But all notes added "Fall" symbol will activate `SFZ\Violins 1 - Sustain Fall.sfz` instead of `SFZ\Violins 1 - Fall.sfz` even if the note has a duration more than 4 16th notes.

Muse Woodwinds instruments including Bass Clarinet contains SFZ for harmonics, however MuseScore Studio 4 (4.3.2) currently does not pass harmonics to MuseSampler, so the harmonics SFZ files are not used. To use them, you need to use instruments like violins but apply Muse Woodwinds soundfonts.

## About the uploaded files

Up until now, I've uploaded all the metadata file to this repo (See [SFZ folder](SFZ)), and their sample file (`*.sts`) has been extracted and rearchived to 7-Zip format, which is uploaded to the release page. To see the full list, see [instruments](instruments.md).

Some of the soundfonts have been converted to SF2 and SF3 format, and uploaded to the release page. I don't guarantee that the converted soundfonts can sound exactly the same as the original soundfonts. To see the full list, see [instruments](instruments.md).

I've also extracted some of the soundfonts in SFZ format, and uploaded to this repo. These are the "non-standard" SFZ files, which means that they may not be supported by some software. See [SFZ folder](SFZ) for theses files.

### Uploaded original SFZ files

If an instrument is not listed here, it means that it doesn't have its own SFZ file or I haven't noticied that instrument.

These SFZ files are **NOT** standard and should be modified before using in other software.

Instruments in *italic* means that some SFZ files are not extracted. See below [SFZ files failed to extract or convert](#sfz-files-failed-to-extract-or-convert) for more information. The number comes after the instrument name is the the count of unextracted SFZ files.

If an instrument contains `Realtime` preset, I guess that it should require a MIDI keyboard to activate, so currently I can't extract them. They are not listed in the "SFZ files failed to extract or convert" section, but a star symbol is added to the instrument name in the list. The number indicating the count of unextracted SFZ files includes these Realtime presets.

- [ ] Muse Brass `0.4.4`
  - [x] Bass Trombone
  - [x] Cimbasso
  - [x] Horn in F
  - [x] Horns a6
  - [ ] Trombone
  - [ ] Trombones a3
  - [ ] Trumpet
  - [ ] Trumpets a4
  - [ ] Tuba
- [x] Muse Choir `0.3.19`
  - [x] Altos
  - [x] Basses
  - [x] Sopranos
  - [x] Tenors
- [x] Muse Guitars Vol. 1 `0.9.8`
  - [x] Acoustic Nylon
  - [x] Acoustic Steel Picked
  - [x] Acoustic Steel Plucked
  - [x] Electric Bass
  - [x] Electric LP - Clean
  - [x] Electric SC - Clean
- [x] Muse Harp `0.2.7`
  - [x] Harp
- [x] Muse Keys `0.4.11`
  - [x] Celesta
  - [x] Dream Piano
  - [x] Grand Piano
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
  - [x] Crotales
  - [x] Drum Kit
  - [x] Field Drum
  - [x] Glockenspiel
  - [x] Gong
  - [x] Marimba
  - [x] Mark Tree
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
- [ ] Muse Strings `0.4.17`
  - [ ] Contrabasses
  - [ ] Viola (Solo)
  - [ ] Violas
  - [ ] Violin 1 (Solo)
  - [ ] Violin 2 (Solo)
  - [ ] Violins 1
  - [ ] Violins 2
  - [ ] Violoncello (Solo)
  - [ ] Violoncellos
- [x] Muse Woodwinds `0.5.23`
  - [x] Alto Flute
  - [x] Alto Sax
  - [x] Baritone Sax
  - [x] Bass Clarinet
  - [x] Bass Flute
  - [x] Bassoon
  - [x] Clarinet in Bb
  - [x] Clarinet in Eb
  - [x] Contrabass Flute
  - [x] Contrabassoon
  - [x] English Horn
  - [x] Flute 1
  - [x] Flute 2
  - [x] Oboe
  - [x] Piccolo
  - [x] Soprano Sax
  - [x] Tenor Sax

## SFZ files failed to extract or convert

Some of the soundfonts have failed to extract or convert. Here is the list of them. Instruments which haven't been extracted is not listed.

`Realtime` SFZ files are not listed here.
