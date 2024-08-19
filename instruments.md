# Instrument List

For Chinese users: CloudFlare only has CDN nodes in Mainland China for business users. If your download speed is slow, you can manually change the domain name in the download link from `dl.muse-sounds.work` to `dl-cn.muse-sounds.work`, which may uses better CDN nodes and routing. However, I don't guarantee it's faster.

## About File Types

- `*.sts.7z`: Compressed original sample files extracted from the sts file. Audio files are in opus format.
- `*.sf2`: Converted SF2 format soundfont file.
- `*.sf3`: Converted SF3 format soundfont file.
- `*.sfz.7z`: Compressed original SFZ files. May not standard SFZ format and can't be loaded by SFZ player.
- `sfz+flac.zip`: Converted SFZ files with FLAC audio files. You can use it directly in SFZ player.

## Converted Releases

These are the instruments that have been converted to standard formats so you can use them in your favorite software. There is no need to download extra files, just extract it (if it is archived) and load it. I've checked the SFZ, SF2, and SF3 files in MuseScore 3.6.2 and they work well.

### Muse Keys

#### Grand Piano
<details><summary>Piano - Pop.sf2</summary>

> Presets:
> 
> - `Piano - Pop`: Original file: `Piano - Pop.sfz`
>   - `Key range`: `A0`-`C8`
> 
> Differences compared to the original file:
> - Removed unsupported opcodes
> - All samples have been truncated to 10s and have no loops
> - Volumes have been applied to the samples
> 
> Other information:
> 
> - Samples will be played 0.06s earlier than the score in MuseScore Studio 4
> - `Muse Keys` version: `0.4.11`

> [Download Piano - Pop.sf2](https://dl.muse-sounds.work/public/release-sf2/Muse%20Keys/Grand%20Piano/Piano%20-%20Pop.sf2) (1692.1 MiB)

---

</details>

<details><summary>Piano - Pop.sf3</summary>

> Presets:
> 
> - `Piano - Pop`: Original file: `Piano - Pop.sfz`
>   - `Key range`: `A0`-`C8`
> 
> Differences compared to the original file:
> - Removed unsupported opcodes
> - All samples have been truncated to 10s and have no loops
> - Volumes have been applied to the samples
> 
> Other information:
> 
> - Samples will be played 0.06s earlier than the score in MuseScore Studio 4
> - `Muse Keys` version: `0.4.11`

> [Download Piano - Pop.sf3](https://dl.muse-sounds.work/public/release-sf3/Muse%20Keys/Grand%20Piano/Piano%20-%20Pop.sf3) (304.27 MiB)

---

</details>

<details><summary>Piano - Pop (converted).sfz+flac.zip</summary>

> Converted from `Muse Keys` -> `Piano` -> `Piano - Pop.sfz`.
> 
> Standard information:
> - Key range: `A0`-`C8`
> 
> Modifications:
> - Removed unsupported opcodes `loop_xfade` `loop_xfade_curve`
> - Removed closing tags
> - Removed master volume control
> 
> Other information:
> - Samples will be played 0.06s earlier than the score in MuseScore Studio 4
> - `Muse Keys` version: `0.4.11`

> [Download Piano - Pop (converted).sfz+flac.zip](https://dl.muse-sounds.work/public/release-sfz%2Bflac/Muse%20Keys/Grand%20Piano/Piano%20-%20Pop%20%28converted%29.sfz%2Bflac.zip) (1408.6 MiB)

---

</details>

<details><summary>Piano - Studio (converted for MU3).sfz+flac.zip</summary>

> Converted from `Muse Keys` -> `Piano` -> `Piano - Studio.sfz`.
> 
> Standard information:
> - Key range: `A0`-`C8`
> 
> Modifications:
> - Removed unsupported opcodes `loop_xfade` `loop_xfade_curve`
> - Removed closing tags
> - Removed master volume control
> - Removed loops, all the notes will has an end
> - Added equalizer according to instrument definition file
> - Removed "trigger", keeping only the "legato" group ("first" group removed) or MuseScore 3 will trigger nothing
> 
> Other information:
> - Samples will be played 0.06s earlier than the score in MuseScore Studio 4
> - `Muse Keys` version: `0.4.11`

> [Download Piano - Studio (converted for MU3).sfz+flac.zip](https://dl.muse-sounds.work/public/release-sfz%2Bflac/Muse%20Keys/Grand%20Piano/Piano%20-%20Studio%20%28converted%20for%20MU3%29.sfz%2Bflac.zip) (1408.6 MiB)

---

</details>

## All Files

These are all the files available for download. They may be the original files, which may be non-standard formats or have extra files that are not needed for most users. If you are not sure what to download, you should check the converted releases above.

### Muse Brass

#### Bass Trombone
<details><summary>Bass Trombone.sfz.7z</summary>

> Original sfz files for `Muse Brass` `Bass Trombone` (`Bass Trombone.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Brass` version: `0.4.4`

> [Download Bass Trombone.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Brass/Bass%20Trombone/Bass%20Trombone.sfz.7z) (276.43 KiB)

---

</details>

<details><summary>Bass Trombone.sts.7z</summary>

> Original sample files for `Muse Brass` `Bass Trombone` (`Bass Trombone.sts`)

> [Download Bass Trombone.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Brass/Bass%20Trombone.sts.7z) (148.12 MiB)

---

</details>

#### Cimbasso
<details><summary>Cimbasso.sfz.7z</summary>

> Original sfz files for `Muse Brass` `Cimbasso` (`Cimbasso.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Brass` version: `0.4.4`

> [Download Cimbasso.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Brass/Cimbasso/Cimbasso.sfz.7z) (240.51 KiB)

---

</details>

<details><summary>Cimbasso.sts.7z</summary>

> Original sample files for `Muse Brass` `Cimbasso` (`Cimbasso.sts`)

> [Download Cimbasso.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Brass/Cimbasso.sts.7z) (218.72 MiB)

---

</details>

#### Horn in F
<details><summary>French Horn.sfz.7z</summary>

> Original sfz files for `Muse Brass` `Horn in F` (`French Horn.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Brass` version: `0.4.4`

> [Download French Horn.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Brass/Horn%20in%20F/French%20Horn.sfz.7z) (310.74 KiB)

---

</details>

<details><summary>French Horn.sts.7z</summary>

> Original sample files for `Muse Brass` `Horn in F` (`French Horn.sts`)

> [Download French Horn.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Brass/Horn%20in%20F/French%20Horn.sts.7z) (217.07 MiB)

---

</details>

#### Horns a6
<details><summary>French Horns a6.sfz.7z</summary>

> Original sfz files for `Muse Brass` `Horns a6` (`French Horns a6.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Brass` version: `0.4.4`

> [Download French Horns a6.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Brass/Horns%20a6/French%20Horns%20a6.sfz.7z) (18504 B)

---

</details>

<details><summary>French Horns a6.sts.7z</summary>

> Original sample files for `Muse Brass` `Horns a6` (`French Horns a6.sts`)

> [Download French Horns a6.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Brass/Horns%20a6/French%20Horns%20a6.sts.7z) (181.88 MiB)

---

</details>

#### Trombone
<details><summary>Trombone.sfz.7z</summary>

> Original sfz files for `Muse Brass` `Trombone` (`Trombone.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Brass` version: `0.4.4`

> [Download Trombone.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Brass/Trombone/Trombone.sfz.7z) (291.45 KiB)

---

</details>

<details><summary>Trombone.sts.7z</summary>

> Original sample files for `Muse Brass` `Trombone` (`Trombone.sts`)

> [Download Trombone.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Brass/Trombone.sts.7z) (137.91 MiB)

---

</details>

#### Trombones a3
<details><summary>Trombones a3.sfz.7z</summary>

> Original sfz files for `Muse Brass` `Trombones a3` (`Trombones a3.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Brass` version: `0.4.4`

> [Download Trombones a3.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Brass/Trombones%20a3/Trombones%20a3.sfz.7z) (19486 B)

---

</details>

<details><summary>Trombones a3.sts.7z</summary>

> Original sample files for `Muse Brass` `Trombones a3` (`Trombones a3.sts`)

> [Download Trombones a3.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Brass/Trombones%20a3.sts.7z) (195.78 MiB)

---

</details>

#### Trumpet
<details><summary>Trumpet.sfz.7z</summary>

> Original sfz files for `Muse Brass` `Trumpet` (`Trumpet.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Brass` version: `0.4.4`

> [Download Trumpet.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Brass/Trumpet/Trumpet.sfz.7z) (283.23 KiB)

---

</details>

<details><summary>Trumpet.sts.7z</summary>

> Original sample files for `Muse Brass` `Trumpet` (`Trumpet.sts`)

> [Download Trumpet.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Brass/Trumpet.sts.7z) (158.73 MiB)

---

</details>

#### Trumpets a4
<details><summary>Trumpets a4.sfz.7z</summary>

> Original sfz files for `Muse Brass` `Trumpets a4` (`Trumpets a4.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Brass` version: `0.4.4`

> [Download Trumpets a4.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Brass/Trumpets%20a4/Trumpets%20a4.sfz.7z) (20116 B)

---

</details>

<details><summary>Trumpets a4.sts.7z</summary>

> Original sample files for `Muse Brass` `Trumpets a4` (`Trumpets a4.sts`)

> [Download Trumpets a4.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Brass/Trumpets%20a4.sts.7z) (226.63 MiB)

---

</details>

#### Tuba
<details><summary>Tuba.sfz.7z</summary>

> Original sfz files for `Muse Brass` `Tuba` (`Tuba.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Brass` version: `0.4.4`

> [Download Tuba.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Brass/Tuba/Tuba.sfz.7z) (231.79 KiB)

---

</details>

<details><summary>Tuba.sts.7z</summary>

> Original sample files for `Muse Brass` `Tuba` (`Tuba.sts`)

> [Download Tuba.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Brass/Tuba.sts.7z) (197.57 MiB)

---

</details>


### Muse Choir

#### Altos
<details><summary>Altos.sfz.7z</summary>

> Original sfz files for `Muse Choir` `Altos` (`Altos.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Choir` version: `0.3.19`

> [Download Altos.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Choir/Altos/Altos.sfz.7z) (27.876 KiB)

---

</details>

<details><summary>Altos.sts.7z</summary>

> Original sample files for `Muse Choir` `Altos` (`Altos.sts`)

> [Download Altos.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Choir/Altos.sts.7z) (138.72 MiB)

---

</details>

#### Basses
<details><summary>Basses.sfz.7z</summary>

> Original sfz files for `Muse Choir` `Basses` (`Basses.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Choir` version: `0.3.19`

> [Download Basses.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Choir/Basses/Basses.sfz.7z) (33.333 KiB)

---

</details>

<details><summary>Basses.sts.7z</summary>

> Original sample files for `Muse Choir` `Basses` (`Basses.sts`)

> [Download Basses.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Choir/Basses.sts.7z) (169.89 MiB)

---

</details>

#### Sopranos
<details><summary>Sopranos.sfz.7z</summary>

> Original sfz files for `Muse Choir` `Sopranos` (`Sopranos.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Choir` version: `0.3.19`

> [Download Sopranos.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Choir/Sopranos/Sopranos.sfz.7z) (29.519 KiB)

---

</details>

<details><summary>Sopranos.sts.7z</summary>

> Original sample files for `Muse Choir` `Sopranos` (`Sopranos.sts`)

> [Download Sopranos.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Choir/Sopranos.sts.7z) (138.67 MiB)

---

</details>

#### Tenors
<details><summary>Tenors.sfz.7z</summary>

> Original sfz files for `Muse Choir` `Tenors` (`Tenors.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Choir` version: `0.3.19`

> [Download Tenors.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Choir/Tenors/Tenors.sfz.7z) (29.559 KiB)

---

</details>

<details><summary>Tenors.sts.7z</summary>

> Original sample files for `Muse Choir` `Tenors` (`Tenors.sts`)

> [Download Tenors.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Choir/Tenors.sts.7z) (143.8 MiB)

---

</details>


### Muse Guitars Vol. 1

#### Acoustic Nylon
<details><summary>Acoustic Nylon.sfz.7z</summary>

> Original sfz files for `Muse Guitars Vol. 1` `Acoustic Nylon` (`Acoustic Nylon.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Guitars Vol. 1` version: `0.9.8`

> [Download Acoustic Nylon.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Guitars%20Vol.%201/Acoustic%20Nylon/Acoustic%20Nylon.sfz.7z) (31.784 KiB)

---

</details>

<details><summary>Acoustic Nylon.sts.7z</summary>

> Original sample files for `Muse Guitars Vol. 1` `Acoustic Nylon` (`Acoustic Nylon.sts`)

> [Download Acoustic Nylon.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Guitars%20Vol.%201/Acoustic%20Nylon.sts.7z) (107.39 MiB)

---

</details>

#### Acoustic Steel Picked
<details><summary>Acoustic Steel Picked.sfz.7z</summary>

> Original sfz files for `Muse Guitars Vol. 1` `Acoustic Steel Picked` (`Acoustic Steel Picked.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Guitars Vol. 1` version: `0.9.8`

> [Download Acoustic Steel Picked.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Guitars%20Vol.%201/Acoustic%20Steel%20Picked/Acoustic%20Steel%20Picked.sfz.7z) (37.157 KiB)

---

</details>

<details><summary>Acoustic Steel Picked.sts.7z</summary>

> Original sample files for `Muse Guitars Vol. 1` `Acoustic Steel Picked` (`Acoustic Steel Picked.sts`)

> [Download Acoustic Steel Picked.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Guitars%20Vol.%201/Acoustic%20Steel%20Picked.sts.7z) (125.99 MiB)

---

</details>

#### Acoustic Steel Plucked
<details><summary>Acoustic Steel Plucked.sfz.7z</summary>

> Original sfz files for `Muse Guitars Vol. 1` `Acoustic Steel Plucked` (`Acoustic Steel Plucked.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Guitars Vol. 1` version: `0.9.8`

> [Download Acoustic Steel Plucked.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Guitars%20Vol.%201/Acoustic%20Steel%20Plucked/Acoustic%20Steel%20Plucked.sfz.7z) (22.375 KiB)

---

</details>

<details><summary>Acoustic Steel Plucked.sts.7z</summary>

> Original sample files for `Muse Guitars Vol. 1` `Acoustic Steel Plucked` (`Acoustic Steel Plucked.sts`)

> [Download Acoustic Steel Plucked.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Guitars%20Vol.%201/Acoustic%20Steel%20Plucked.sts.7z) (88.818 MiB)

---

</details>

#### Electric Bass
<details><summary>Electric Bass.sfz.7z</summary>

> Original sfz files for `Muse Guitars Vol. 1` `Electric Bass` (`Electric Bass.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Guitars Vol. 1` version: `0.9.8`

> [Download Electric Bass.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Guitars%20Vol.%201/Electric%20Bass/Electric%20Bass.sfz.7z) (27.427 KiB)

---

</details>

<details><summary>Electric Bass.sts.7z</summary>

> Original sample files for `Muse Guitars Vol. 1` `Electric Bass` (`Electric Bass.sts`)

> [Download Electric Bass.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Guitars%20Vol.%201/Electric%20Bass.sts.7z) (104.16 MiB)

---

</details>

#### Electric LP - Clean
<details><summary>Electric LP - Clean.sfz.7z</summary>

> Original sfz files for `Muse Guitars Vol. 1` `Electric LP - Clean` (`Electric LP - Clean.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Guitars Vol. 1` version: `0.9.8`

> [Download Electric LP - Clean.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Guitars%20Vol.%201/Electric%20LP%20-%20Clean/Electric%20LP%20-%20Clean.sfz.7z) (30.866 KiB)

---

</details>

<details><summary>Electric LP - Clean.sts.7z</summary>

> Original sample files for `Muse Guitars Vol. 1` `Electric LP - Clean` (`Electric LP - Clean.sts`)

> [Download Electric LP - Clean.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Guitars%20Vol.%201/Electric%20LP%20-%20Clean.sts.7z) (116.2 MiB)

---

</details>

#### Electric SC - Clean
<details><summary>Electric SC - Clean.sfz.7z</summary>

> Original sfz files for `Muse Guitars Vol. 1` `Electric SC - Clean` (`Electric SC - Clean.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Guitars Vol. 1` version: `0.9.8`

> [Download Electric SC - Clean.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Guitars%20Vol.%201/Electric%20SC%20-%20Clean/Electric%20SC%20-%20Clean.sfz.7z) (81.865 KiB)

---

</details>

<details><summary>Electric SC - Clean.sts.7z</summary>

> Original sample files for `Muse Guitars Vol. 1` `Electric SC - Clean` (`Electric SC - Clean.sts`)

> [Download Electric SC - Clean.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Guitars%20Vol.%201/Electric%20SC%20-%20Clean.sts.7z) (385.25 MiB)

---

</details>


### Muse Harp

#### Harp
<details><summary>Harp.sfz.7z</summary>

> Original sfz files for `Muse Harp` `Harp` (`Harp.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Harp` version: `0.2.7`

> [Download Harp.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Harp/Harp/Harp.sfz.7z) (11092 B)

---

</details>

<details><summary>Harp.sts.7z</summary>

> Original sample files for `Muse Harp` `Harp` (`Harp.sts`)

> [Download Harp.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Harp/Harp.sts.7z) (156.15 MiB)

---

</details>


### Muse Keys

#### Celesta
<details><summary>Celesta.sfz.7z</summary>

> Original sfz files for `Muse Keys` `Celesta` (`Celesta.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Keys` version: `0.4.11`

> [Download Celesta.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Keys/Celesta/Celesta.sfz.7z) (1211 B)

---

</details>

<details><summary>Celesta.sts.7z</summary>

> Original sample files for `Muse Keys` `Celesta` (`Celesta.sts`)

> [Download Celesta.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Keys/Celesta.sts.7z) (17655 KiB)

---

</details>

#### Dream Piano
<details><summary>Dream Piano.sfz.7z</summary>

> Original sfz files for `Muse Keys` `Dream Piano` (`Dream Piano.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Keys` version: `0.4.11`

> [Download Dream Piano.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Keys/Dream%20Piano/Dream%20Piano.sfz.7z) (2460 B)

---

</details>

<details><summary>Dream Piano.sts.7z</summary>

> Original sample files for `Muse Keys` `Dream Piano` (`Dream Piano.sts`)

> [Download Dream Piano.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Keys/Dream%20Piano.sts.7z) (63.537 MiB)

---

</details>

#### Grand Piano
<details><summary>Piano.sfz.7z</summary>

> Original sfz files for `Muse Keys` `Grand Piano` (`Piano.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Keys` version: `0.4.11`

> [Download Piano.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Keys/Grand%20Piano/Piano.sfz.7z) (7500 B)

---

</details>

<details><summary>Piano.sts.7z</summary>

> Original sample files for `Muse Keys` `Grand Piano` (`Piano.sts`)

> [Download Piano.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Keys/Grand%20Piano/Piano.sts.7z) (189.07 MiB)

---

</details>

<details><summary>Piano - Pop.sf2</summary>

> Presets:
> 
> - `Piano - Pop`: Original file: `Piano - Pop.sfz`
>   - `Key range`: `A0`-`C8`
> 
> Differences compared to the original file:
> - Removed unsupported opcodes
> - All samples have been truncated to 10s and have no loops
> - Volumes have been applied to the samples
> 
> Other information:
> 
> - Samples will be played 0.06s earlier than the score in MuseScore Studio 4
> - `Muse Keys` version: `0.4.11`

> [Download Piano - Pop.sf2](https://dl.muse-sounds.work/public/release-sf2/Muse%20Keys/Grand%20Piano/Piano%20-%20Pop.sf2) (1692.1 MiB)

---

</details>

<details><summary>Piano - Pop.sf3</summary>

> Presets:
> 
> - `Piano - Pop`: Original file: `Piano - Pop.sfz`
>   - `Key range`: `A0`-`C8`
> 
> Differences compared to the original file:
> - Removed unsupported opcodes
> - All samples have been truncated to 10s and have no loops
> - Volumes have been applied to the samples
> 
> Other information:
> 
> - Samples will be played 0.06s earlier than the score in MuseScore Studio 4
> - `Muse Keys` version: `0.4.11`

> [Download Piano - Pop.sf3](https://dl.muse-sounds.work/public/release-sf3/Muse%20Keys/Grand%20Piano/Piano%20-%20Pop.sf3) (304.27 MiB)

---

</details>

<details><summary>Piano - Pop (converted).sfz+flac.zip</summary>

> Converted from `Muse Keys` -> `Piano` -> `Piano - Pop.sfz`.
> 
> Standard information:
> - Key range: `A0`-`C8`
> 
> Modifications:
> - Removed unsupported opcodes `loop_xfade` `loop_xfade_curve`
> - Removed closing tags
> - Removed master volume control
> 
> Other information:
> - Samples will be played 0.06s earlier than the score in MuseScore Studio 4
> - `Muse Keys` version: `0.4.11`

> [Download Piano - Pop (converted).sfz+flac.zip](https://dl.muse-sounds.work/public/release-sfz%2Bflac/Muse%20Keys/Grand%20Piano/Piano%20-%20Pop%20%28converted%29.sfz%2Bflac.zip) (1408.6 MiB)

---

</details>

<details><summary>Piano - Studio (converted for MU3).sfz+flac.zip</summary>

> Converted from `Muse Keys` -> `Piano` -> `Piano - Studio.sfz`.
> 
> Standard information:
> - Key range: `A0`-`C8`
> 
> Modifications:
> - Removed unsupported opcodes `loop_xfade` `loop_xfade_curve`
> - Removed closing tags
> - Removed master volume control
> - Removed loops, all the notes will has an end
> - Added equalizer according to instrument definition file
> - Removed "trigger", keeping only the "legato" group ("first" group removed) or MuseScore 3 will trigger nothing
> 
> Other information:
> - Samples will be played 0.06s earlier than the score in MuseScore Studio 4
> - `Muse Keys` version: `0.4.11`

> [Download Piano - Studio (converted for MU3).sfz+flac.zip](https://dl.muse-sounds.work/public/release-sfz%2Bflac/Muse%20Keys/Grand%20Piano/Piano%20-%20Studio%20%28converted%20for%20MU3%29.sfz%2Bflac.zip) (1408.6 MiB)

---

</details>

#### Hammond Organ
<details><summary>Hammond Organ.sfz.7z</summary>

> Original sfz files for `Muse Keys` `Hammond Organ` (`Hammond Organ.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Keys` version: `0.4.11`

> [Download Hammond Organ.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Keys/Hammond%20Organ/Hammond%20Organ.sfz.7z) (1290 B)

---

</details>

<details><summary>Hammond Organ.sts.7z</summary>

> Original sample files for `Muse Keys` `Hammond Organ` (`Hammond Organ.sts`)

> [Download Hammond Organ.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Keys/Hammond%20Organ.sts.7z) (3783.7 KiB)

---

</details>

#### Harpsichord
<details><summary>Harpsichord.sfz.7z</summary>

> Original sfz files for `Muse Keys` `Harpsichord` (`Harpsichord.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Keys` version: `0.4.11`

> [Download Harpsichord.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Keys/Harpsichord/Harpsichord.sfz.7z) (828 B)

---

</details>

<details><summary>Harpsichord.sts.7z</summary>

> Original sample files for `Muse Keys` `Harpsichord` (`Harpsichord.sts`)

> [Download Harpsichord.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Keys/Harpsichord.sts.7z) (7068.5 KiB)

---

</details>

#### Soft Piano
<details><summary>Soft Piano.sfz.7z</summary>

> Original sfz files for `Muse Keys` `Soft Piano` (`Soft Piano.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Keys` version: `0.4.11`

> [Download Soft Piano.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Keys/Soft%20Piano/Soft%20Piano.sfz.7z) (1323 B)

---

</details>

<details><summary>Soft Piano.sts.7z</summary>

> Original sample files for `Muse Keys` `Soft Piano` (`Soft Piano.sts`)

> [Download Soft Piano.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Keys/Soft%20Piano.sts.7z) (44.489 MiB)

---

</details>

#### Suitcase Piano
<details><summary>Suitcase Piano.sfz.7z</summary>

> Original sfz files for `Muse Keys` `Suitcase Piano` (`Suitcase Piano.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Keys` version: `0.4.11`

> [Download Suitcase Piano.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Keys/Suitcase%20Piano/Suitcase%20Piano.sfz.7z) (1734 B)

---

</details>

<details><summary>Suitcase Piano.sts.7z</summary>

> Original sample files for `Muse Keys` `Suitcase Piano` (`Suitcase Piano.sts`)

> [Download Suitcase Piano.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Keys/Suitcase%20Piano.sts.7z) (19181 KiB)

---

</details>

#### Upright Piano
<details><summary>Upright Piano.sfz.7z</summary>

> Original sfz files for `Muse Keys` `Upright Piano` (`Upright Piano.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Keys` version: `0.4.11`

> [Download Upright Piano.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Keys/Upright%20Piano/Upright%20Piano.sfz.7z) (874 B)

---

</details>

<details><summary>Upright Piano.sts.7z</summary>

> Original sample files for `Muse Keys` `Upright Piano` (`Upright Piano.sts`)

> [Download Upright Piano.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Keys/Upright%20Piano.sts.7z) (5144 KiB)

---

</details>

#### Wurly 200A
<details><summary>Wurly 200A.sfz.7z</summary>

> Original sfz files for `Muse Keys` `Wurly 200A` (`Wurly 200A.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Keys` version: `0.4.11`

> [Download Wurly 200A.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Keys/Wurly%20200A/Wurly%20200A.sfz.7z) (1031 B)

---

</details>

<details><summary>Wurly 200A.sts.7z</summary>

> Original sample files for `Muse Keys` `Wurly 200A` (`Wurly 200A.sts`)

> [Download Wurly 200A.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Keys/Wurly%20200A.sts.7z) (4887.2 KiB)

---

</details>


### Muse Percussion

#### Bass Drum
<details><summary>Bass Drum.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Bass Drum` (`Bass Drum.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Bass Drum.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Bass%20Drum/Bass%20Drum.sfz.7z) (1294 B)

---

</details>

<details><summary>Bass Drum.sts.7z</summary>

> Original sample files for `Muse Percussion` `Bass Drum` (`Bass Drum.sts`)

> [Download Bass Drum.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Bass%20Drum.sts.7z) (8097.6 KiB)

---

</details>

#### Bell Tree
<details><summary>Bell Tree.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Bell Tree` (`Bell Tree.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Bell Tree.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Bell%20Tree/Bell%20Tree.sfz.7z) (686 B)

---

</details>

<details><summary>Bell Tree.sts.7z</summary>

> Original sample files for `Muse Percussion` `Bell Tree` (`Bell Tree.sts`)

> [Download Bell Tree.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Bell%20Tree.sts.7z) (2604.7 KiB)

---

</details>

#### Bongos
<details><summary>Bongos.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Bongos` (`Bongos.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Bongos.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Bongos/Bongos.sfz.7z) (1417 B)

---

</details>

<details><summary>Bongos.sts.7z</summary>

> Original sample files for `Muse Percussion` `Bongos` (`Bongos.sts`)

> [Download Bongos.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Bongos.sts.7z) (5985.2 KiB)

---

</details>

#### Cabasa
<details><summary>Cabasa.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Cabasa` (`Cabasa.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Cabasa.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Cabasa/Cabasa.sfz.7z) (591 B)

---

</details>

<details><summary>Cabasa.sts.7z</summary>

> Original sample files for `Muse Percussion` `Cabasa` (`Cabasa.sts`)

> [Download Cabasa.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Cabasa.sts.7z) (967.64 KiB)

---

</details>

#### Castanets
<details><summary>Castanets.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Castanets` (`Castanets.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Castanets.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Castanets/Castanets.sfz.7z) (648 B)

---

</details>

<details><summary>Castanets.sts.7z</summary>

> Original sample files for `Muse Percussion` `Castanets` (`Castanets.sts`)

> [Download Castanets.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Castanets.sts.7z) (718.29 KiB)

---

</details>

#### Claves
<details><summary>Claves.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Claves` (`Claves.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Claves.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Claves/Claves.sfz.7z) (387 B)

---

</details>

<details><summary>Claves.sts.7z</summary>

> Original sample files for `Muse Percussion` `Claves` (`Claves.sts`)

> [Download Claves.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Claves.sts.7z) (949.07 KiB)

---

</details>

#### Cowbell
<details><summary>Cowbell.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Cowbell` (`Cowbell.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Cowbell.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Cowbell/Cowbell.sfz.7z) (687 B)

---

</details>

<details><summary>Cowbell.sts.7z</summary>

> Original sample files for `Muse Percussion` `Cowbell` (`Cowbell.sts`)

> [Download Cowbell.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Cowbell.sts.7z) (3603.8 KiB)

---

</details>

#### Crotales
<details><summary>Crotales.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Crotales` (`Crotales.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Crotales.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Crotales/Crotales.sfz.7z) (715 B)

---

</details>

<details><summary>Crotales.sts.7z</summary>

> Original sample files for `Muse Percussion` `Crotales` (`Crotales.sts`)

> [Download Crotales.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Crotales.sts.7z) (8294.4 KiB)

---

</details>

#### Drum Kit
<details><summary>Drum Kit.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Drum Kit` (`Drum Kit.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Drum Kit.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Drum%20Kit/Drum%20Kit.sfz.7z) (1892 B)

---

</details>

<details><summary>Drum Kit.sts.7z</summary>

> Original sample files for `Muse Percussion` `Drum Kit` (`Drum Kit.sts`)

> [Download Drum Kit.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Drum%20Kit.sts.7z) (4720.9 KiB)

---

</details>

#### Field Drum
<details><summary>Field Drum.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Field Drum` (`Field Drum.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Field Drum.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Field%20Drum/Field%20Drum.sfz.7z) (2010 B)

---

</details>

<details><summary>Field Drum.sts.7z</summary>

> Original sample files for `Muse Percussion` `Field Drum` (`Field Drum.sts`)

> [Download Field Drum.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Field%20Drum.sts.7z) (10269 KiB)

---

</details>

#### Glockenspiel
<details><summary>Glockenspiel.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Glockenspiel` (`Glockenspiel.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Glockenspiel.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Glockenspiel/Glockenspiel.sfz.7z) (5658 B)

---

</details>

<details><summary>Glockenspiel.sts.7z</summary>

> Original sample files for `Muse Percussion` `Glockenspiel` (`Glockenspiel.sts`)

> [Download Glockenspiel.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Glockenspiel.sts.7z) (276.89 MiB)

---

</details>

#### Gong
<details><summary>Gong.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Gong` (`Gong.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Gong.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Gong/Gong.sfz.7z) (1229 B)

---

</details>

<details><summary>Gong.sts.7z</summary>

> Original sample files for `Muse Percussion` `Gong` (`Gong.sts`)

> [Download Gong.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Gong.sts.7z) (18722 KiB)

---

</details>

#### Marimba
<details><summary>Marimba.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Marimba` (`Marimba.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Marimba.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Marimba/Marimba.sfz.7z) (7514 B)

---

</details>

<details><summary>Marimba.sts.7z</summary>

> Original sample files for `Muse Percussion` `Marimba` (`Marimba.sts`)

> [Download Marimba.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Marimba.sts.7z) (179.79 MiB)

---

</details>

#### Mark Tree
<details><summary>Mark Tree.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Mark Tree` (`Mark Tree.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Mark Tree.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Mark%20Tree/Mark%20Tree.sfz.7z) (668 B)

---

</details>

<details><summary>Mark Tree.sts.7z</summary>

> Original sample files for `Muse Percussion` `Mark Tree` (`Mark Tree.sts`)

> [Download Mark Tree.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Mark%20Tree.sts.7z) (6526.1 KiB)

---

</details>

#### Metronome
<details><summary>Metronome.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Metronome` (`Metronome.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Metronome.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Metronome/Metronome.sfz.7z) (262 B)

---

</details>

<details><summary>Metronome.sts.7z</summary>

> Original sample files for `Muse Percussion` `Metronome` (`Metronome.sts`)

> [Download Metronome.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Metronome.sts.7z) (682 B)

---

</details>

#### Piatti
<details><summary>Piatti.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Piatti` (`Piatti.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Piatti.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Piatti/Piatti.sfz.7z) (908 B)

---

</details>

<details><summary>Piatti.sts.7z</summary>

> Original sample files for `Muse Percussion` `Piatti` (`Piatti.sts`)

> [Download Piatti.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Piatti.sts.7z) (5987.5 KiB)

---

</details>

#### Shaker
<details><summary>Shaker.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Shaker` (`Shaker.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Shaker.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Shaker/Shaker.sfz.7z) (884 B)

---

</details>

<details><summary>Shaker.sts.7z</summary>

> Original sample files for `Muse Percussion` `Shaker` (`Shaker.sts`)

> [Download Shaker.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Shaker.sts.7z) (1863.7 KiB)

---

</details>

#### Sleigh Bells
<details><summary>Sleigh Bells.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Sleigh Bells` (`Sleigh Bells.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Sleigh Bells.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Sleigh%20Bells/Sleigh%20Bells.sfz.7z) (455 B)

---

</details>

<details><summary>Sleigh Bells.sts.7z</summary>

> Original sample files for `Muse Percussion` `Sleigh Bells` (`Sleigh Bells.sts`)

> [Download Sleigh Bells.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Sleigh%20Bells.sts.7z) (243.97 KiB)

---

</details>

#### Snare Drum
<details><summary>Snare.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Snare Drum` (`Snare.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Snare.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Snare%20Drum/Snare.sfz.7z) (2836 B)

---

</details>

<details><summary>Snare.sts.7z</summary>

> Original sample files for `Muse Percussion` `Snare Drum` (`Snare.sts`)

> [Download Snare.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Snare%20Drum/Snare.sts.7z) (13439 KiB)

---

</details>

#### Sus. Cymbal
<details><summary>Suspended Cymbal.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Sus. Cymbal` (`Suspended Cymbal.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Suspended Cymbal.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Sus.%20Cymbal/Suspended%20Cymbal.sfz.7z) (2083 B)

---

</details>

<details><summary>Suspended Cymbal.sts.7z</summary>

> Original sample files for `Muse Percussion` `Sus. Cymbal` (`Suspended Cymbal.sts`)

> [Download Suspended Cymbal.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Sus.%20Cymbal/Suspended%20Cymbal.sts.7z) (23.199 MiB)

---

</details>

#### Taikos
<details><summary>Taikos.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Taikos` (`Taikos.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Taikos.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Taikos/Taikos.sfz.7z) (1034 B)

---

</details>

<details><summary>Taikos.sts.7z</summary>

> Original sample files for `Muse Percussion` `Taikos` (`Taikos.sts`)

> [Download Taikos.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Taikos.sts.7z) (12948 KiB)

---

</details>

#### Tam-tam
<details><summary>Tam-Tam.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Tam-tam` (`Tam-Tam.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Tam-Tam.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Tam-tam/Tam-Tam.sfz.7z) (872 B)

---

</details>

<details><summary>Tam-Tam.sts.7z</summary>

> Original sample files for `Muse Percussion` `Tam-tam` (`Tam-Tam.sts`)

> [Download Tam-Tam.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Tam-tam/Tam-Tam.sts.7z) (15351 KiB)

---

</details>

#### Tambourine
<details><summary>Tambourine.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Tambourine` (`Tambourine.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Tambourine.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Tambourine/Tambourine.sfz.7z) (1091 B)

---

</details>

<details><summary>Tambourine.sts.7z</summary>

> Original sample files for `Muse Percussion` `Tambourine` (`Tambourine.sts`)

> [Download Tambourine.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Tambourine.sts.7z) (1436.9 KiB)

---

</details>

#### Timbales
<details><summary>Timbales.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Timbales` (`Timbales.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Timbales.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Timbales/Timbales.sfz.7z) (1582 B)

---

</details>

<details><summary>Timbales.sts.7z</summary>

> Original sample files for `Muse Percussion` `Timbales` (`Timbales.sts`)

> [Download Timbales.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Timbales.sts.7z) (6464.7 KiB)

---

</details>

#### Timpani
<details><summary>Timpani.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Timpani` (`Timpani.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Timpani.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Timpani/Timpani.sfz.7z) (11417 B)

---

</details>

<details><summary>Timpani.sts.7z</summary>

> Original sample files for `Muse Percussion` `Timpani` (`Timpani.sts`)

> [Download Timpani.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Timpani.sts.7z) (306 MiB)

---

</details>

#### Toms
<details><summary>Toms.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Toms` (`Toms.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Toms.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Toms/Toms.sfz.7z) (1669 B)

---

</details>

<details><summary>Toms.sts.7z</summary>

> Original sample files for `Muse Percussion` `Toms` (`Toms.sts`)

> [Download Toms.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Toms.sts.7z) (7276.4 KiB)

---

</details>

#### Triangle
<details><summary>Triangle.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Triangle` (`Triangle.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Triangle.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Triangle/Triangle.sfz.7z) (1123 B)

---

</details>

<details><summary>Triangle.sts.7z</summary>

> Original sample files for `Muse Percussion` `Triangle` (`Triangle.sts`)

> [Download Triangle.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Triangle.sts.7z) (6014.7 KiB)

---

</details>

#### Tubular Bells
<details><summary>Tubular Bells.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Tubular Bells` (`Tubular Bells.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Tubular Bells.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Tubular%20Bells/Tubular%20Bells.sfz.7z) (1604 B)

---

</details>

<details><summary>Tubular Bells.sts.7z</summary>

> Original sample files for `Muse Percussion` `Tubular Bells` (`Tubular Bells.sts`)

> [Download Tubular Bells.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Tubular%20Bells.sts.7z) (32.701 MiB)

---

</details>

#### Vibraphone
<details><summary>Vibraphone.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Vibraphone` (`Vibraphone.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Vibraphone.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Vibraphone/Vibraphone.sfz.7z) (7810 B)

---

</details>

<details><summary>Vibraphone.sts.7z</summary>

> Original sample files for `Muse Percussion` `Vibraphone` (`Vibraphone.sts`)

> [Download Vibraphone.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Vibraphone.sts.7z) (95.32 MiB)

---

</details>

#### Wood Blocks
<details><summary>Woodblocks.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Wood Blocks` (`Woodblocks.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Woodblocks.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Wood%20Blocks/Woodblocks.sfz.7z) (727 B)

---

</details>

<details><summary>Woodblocks.sts.7z</summary>

> Original sample files for `Muse Percussion` `Wood Blocks` (`Woodblocks.sts`)

> [Download Woodblocks.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Wood%20Blocks/Woodblocks.sts.7z) (1410.5 KiB)

---

</details>

#### Xylophone
<details><summary>Xylophone.sfz.7z</summary>

> Original sfz files for `Muse Percussion` `Xylophone` (`Xylophone.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Percussion` version: `0.5.10`

> [Download Xylophone.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Percussion/Xylophone/Xylophone.sfz.7z) (6083 B)

---

</details>

<details><summary>Xylophone.sts.7z</summary>

> Original sample files for `Muse Percussion` `Xylophone` (`Xylophone.sts`)

> [Download Xylophone.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Percussion/Xylophone.sts.7z) (92.241 MiB)

---

</details>


### Muse Strings

#### Contrabasses
<details><summary>Contrabasses.sfz.7z</summary>

> Original sfz files for `Muse Strings` `Contrabasses` (`Contrabasses.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Strings` version: `0.4.18`

> [Download Contrabasses.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Strings/Contrabasses/Contrabasses.sfz.7z) (35.384 KiB)

---

</details>

<details><summary>Contrabasses.sts.7z</summary>

> Original sample files for `Muse Strings` `Contrabasses` (`Contrabasses.sts`)

> [Download Contrabasses.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Strings/Contrabasses.sts.7z) (414.41 MiB)

---

</details>

#### Viola (Solo)
<details><summary>Viola Solo.sfz.7z</summary>

> Original sfz files for `Muse Strings` `Viola (Solo)` (`Viola Solo.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Strings` version: `0.4.18`

> [Download Viola Solo.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Strings/Viola%20%28Solo%29/Viola%20Solo.sfz.7z) (563.18 KiB)

---

</details>

<details><summary>Viola Solo.sts.7z</summary>

> Original sample files for `Muse Strings` `Viola (Solo)` (`Viola Solo.sts`)

> [Download Viola Solo.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Strings/Viola%20%28Solo%29/Viola%20Solo.sts.7z) (493.67 MiB)

---

</details>

#### Violas
<details><summary>Violas.sfz.7z</summary>

> Original sfz files for `Muse Strings` `Violas` (`Violas.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Strings` version: `0.4.18`

> [Download Violas.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Strings/Violas/Violas.sfz.7z) (40.247 KiB)

---

</details>

<details><summary>Violas.sts.7z</summary>

> Original sample files for `Muse Strings` `Violas` (`Violas.sts`)

> [Download Violas.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Strings/Violas.sts.7z) (529.47 MiB)

---

</details>

#### Violin 1 (Solo)
<details><summary>Violin 1 Solo.sfz.7z</summary>

> Original sfz files for `Muse Strings` `Violin 1 (Solo)` (`Violin 1 Solo.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Strings` version: `0.4.18`

> [Download Violin 1 Solo.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Strings/Violin%201%20%28Solo%29/Violin%201%20Solo.sfz.7z) (884.37 KiB)

---

</details>

<details><summary>Violin 1 Solo.sts.7z</summary>

> Original sample files for `Muse Strings` `Violin 1 (Solo)` (`Violin 1 Solo.sts`)

> [Download Violin 1 Solo.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Strings/Violin%201%20%28Solo%29/Violin%201%20Solo.sts.7z) (512.54 MiB)

---

</details>

#### Violin 2 (Solo)
<details><summary>Violin 2 Solo.sfz.7z</summary>

> Original sfz files for `Muse Strings` `Violin 2 (Solo)` (`Violin 2 Solo.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Strings` version: `0.4.18`

> [Download Violin 2 Solo.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Strings/Violin%202%20%28Solo%29/Violin%202%20Solo.sfz.7z) (1113.9 KiB)

---

</details>

<details><summary>Violin 2 Solo.sts.7z</summary>

> Original sample files for `Muse Strings` `Violin 2 (Solo)` (`Violin 2 Solo.sts`)

> [Download Violin 2 Solo.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Strings/Violin%202%20%28Solo%29/Violin%202%20Solo.sts.7z) (628.2 MiB)

---

</details>

#### Violins 1
<details><summary>Violins 1.sfz.7z</summary>

> Original sfz files for `Muse Strings` `Violins 1` (`Violins 1.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Strings` version: `0.4.18`

> [Download Violins 1.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Strings/Violins%201/Violins%201.sfz.7z) (37.92 KiB)

---

</details>

<details><summary>Violins 1.sts.7z</summary>

> Original sample files for `Muse Strings` `Violins 1` (`Violins 1.sts`)

> [Download Violins 1.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Strings/Violins%201.sts.7z) (640.17 MiB)

---

</details>

#### Violins 2
<details><summary>Violins 2.sfz.7z</summary>

> Original sfz files for `Muse Strings` `Violins 2` (`Violins 2.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Strings` version: `0.4.18`

> [Download Violins 2.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Strings/Violins%202/Violins%202.sfz.7z) (42.182 KiB)

---

</details>

<details><summary>Violins 2.sts.7z</summary>

> Original sample files for `Muse Strings` `Violins 2` (`Violins 2.sts`)

> [Download Violins 2.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Strings/Violins%202.sts.7z) (623.67 MiB)

---

</details>

#### Violoncello (Solo)
<details><summary>Cello Solo.sfz.7z</summary>

> Original sfz files for `Muse Strings` `Violoncello (Solo)` (`Cello Solo.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Strings` version: `0.4.18`

> [Download Cello Solo.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Strings/Violoncello%20%28Solo%29/Cello%20Solo.sfz.7z) (913.39 KiB)

---

</details>

<details><summary>Cello Solo.sts.7z</summary>

> Original sample files for `Muse Strings` `Violoncello (Solo)` (`Cello Solo.sts`)

> [Download Cello Solo.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Strings/Violoncello%20%28Solo%29/Cello%20Solo.sts.7z) (672.18 MiB)

---

</details>

#### Violoncellos
<details><summary>Cellos.sfz.7z</summary>

> Original sfz files for `Muse Strings` `Violoncellos` (`Cellos.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Strings` version: `0.4.18`

> [Download Cellos.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Strings/Violoncellos/Cellos.sfz.7z) (39.24 KiB)

---

</details>

<details><summary>Cellos.sts.7z</summary>

> Original sample files for `Muse Strings` `Violoncellos` (`Cellos.sts`)

> [Download Cellos.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Strings/Violoncellos/Cellos.sts.7z) (614.53 MiB)

---

</details>


### Muse Woodwinds

#### Alto Flute
<details><summary>Alto Flute.sfz.7z</summary>

> Original sfz files for `Muse Woodwinds` `Alto Flute` (`Alto Flute.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Woodwinds` version: `0.5.23`

> [Download Alto Flute.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Woodwinds/Alto%20Flute/Alto%20Flute.sfz.7z) (496.88 KiB)

---

</details>

<details><summary>Alto Flute.sts.7z</summary>

> Original sample files for `Muse Woodwinds` `Alto Flute` (`Alto Flute.sts`)

> [Download Alto Flute.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Woodwinds/Alto%20Flute.sts.7z) (281.44 MiB)

---

</details>

#### Alto Sax
<details><summary>Alto Saxophone.sfz.7z</summary>

> Original sfz files for `Muse Woodwinds` `Alto Sax` (`Alto Saxophone.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Woodwinds` version: `0.5.23`

> [Download Alto Saxophone.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Woodwinds/Alto%20Sax/Alto%20Saxophone.sfz.7z) (513.23 KiB)

---

</details>

<details><summary>Alto Saxophone.sts.7z</summary>

> Original sample files for `Muse Woodwinds` `Alto Sax` (`Alto Saxophone.sts`)

> [Download Alto Saxophone.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Woodwinds/Alto%20Sax/Alto%20Saxophone.sts.7z) (230.31 MiB)

---

</details>

#### Baritone Sax
<details><summary>Baritone Saxophone.sfz.7z</summary>

> Original sfz files for `Muse Woodwinds` `Baritone Sax` (`Baritone Saxophone.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Woodwinds` version: `0.5.23`

> [Download Baritone Saxophone.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Woodwinds/Baritone%20Sax/Baritone%20Saxophone.sfz.7z) (532.67 KiB)

---

</details>

<details><summary>Baritone Saxophone.sts.7z</summary>

> Original sample files for `Muse Woodwinds` `Baritone Sax` (`Baritone Saxophone.sts`)

> [Download Baritone Saxophone.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Woodwinds/Baritone%20Sax/Baritone%20Saxophone.sts.7z) (290.17 MiB)

---

</details>

#### Bass Clarinet
<details><summary>Bass Clarinet.sfz.7z</summary>

> Original sfz files for `Muse Woodwinds` `Bass Clarinet` (`Bass Clarinet.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Woodwinds` version: `0.5.23`

> [Download Bass Clarinet.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Woodwinds/Bass%20Clarinet/Bass%20Clarinet.sfz.7z) (584.31 KiB)

---

</details>

<details><summary>Bass Clarinet.sts.7z</summary>

> Original sample files for `Muse Woodwinds` `Bass Clarinet` (`Bass Clarinet.sts`)

> [Download Bass Clarinet.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Woodwinds/Bass%20Clarinet.sts.7z) (348.88 MiB)

---

</details>

#### Bass Flute
<details><summary>Bass Flute.sfz.7z</summary>

> Original sfz files for `Muse Woodwinds` `Bass Flute` (`Bass Flute.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Woodwinds` version: `0.5.23`

> [Download Bass Flute.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Woodwinds/Bass%20Flute/Bass%20Flute.sfz.7z) (327.23 KiB)

---

</details>

<details><summary>Bass Flute.sts.7z</summary>

> Original sample files for `Muse Woodwinds` `Bass Flute` (`Bass Flute.sts`)

> [Download Bass Flute.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Woodwinds/Bass%20Flute.sts.7z) (183.38 MiB)

---

</details>

#### Bassoon
<details><summary>Bassoon.sfz.7z</summary>

> Original sfz files for `Muse Woodwinds` `Bassoon` (`Bassoon.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Woodwinds` version: `0.5.23`

> [Download Bassoon.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Woodwinds/Bassoon/Bassoon.sfz.7z) (561.47 KiB)

---

</details>

<details><summary>Bassoon.sts.7z</summary>

> Original sample files for `Muse Woodwinds` `Bassoon` (`Bassoon.sts`)

> [Download Bassoon.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Woodwinds/Bassoon.sts.7z) (320.56 MiB)

---

</details>

#### Clarinet in Bb
<details><summary>Clarinet in Bb.sfz.7z</summary>

> Original sfz files for `Muse Woodwinds` `Clarinet in Bb` (`Clarinet in Bb.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Woodwinds` version: `0.5.23`

> [Download Clarinet in Bb.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Woodwinds/Clarinet%20in%20Bb/Clarinet%20in%20Bb.sfz.7z) (720.99 KiB)

---

</details>

<details><summary>Clarinet in Bb.sts.7z</summary>

> Original sample files for `Muse Woodwinds` `Clarinet in Bb` (`Clarinet in Bb.sts`)

> [Download Clarinet in Bb.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Woodwinds/Clarinet%20in%20Bb.sts.7z) (343.66 MiB)

---

</details>

#### Clarinet in Eb
<details><summary>Clarinet in Eb.sfz.7z</summary>

> Original sfz files for `Muse Woodwinds` `Clarinet in Eb` (`Clarinet in Eb.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Woodwinds` version: `0.5.23`

> [Download Clarinet in Eb.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Woodwinds/Clarinet%20in%20Eb/Clarinet%20in%20Eb.sfz.7z) (599.3 KiB)

---

</details>

<details><summary>Clarinet in Eb.sts.7z</summary>

> Original sample files for `Muse Woodwinds` `Clarinet in Eb` (`Clarinet in Eb.sts`)

> [Download Clarinet in Eb.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Woodwinds/Clarinet%20in%20Eb.sts.7z) (241.18 MiB)

---

</details>

#### Contrabass Flute
<details><summary>Contrabass Flute.sfz.7z</summary>

> Original sfz files for `Muse Woodwinds` `Contrabass Flute` (`Contrabass Flute.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Woodwinds` version: `0.5.23`

> [Download Contrabass Flute.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Woodwinds/Contrabass%20Flute/Contrabass%20Flute.sfz.7z) (21.44 KiB)

---

</details>

<details><summary>Contrabass Flute.sts.7z</summary>

> Original sample files for `Muse Woodwinds` `Contrabass Flute` (`Contrabass Flute.sts`)

> [Download Contrabass Flute.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Woodwinds/Contrabass%20Flute.sts.7z) (125.77 MiB)

---

</details>

#### Contrabassoon
<details><summary>Contrabassoon.sfz.7z</summary>

> Original sfz files for `Muse Woodwinds` `Contrabassoon` (`Contrabassoon.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Woodwinds` version: `0.5.23`

> [Download Contrabassoon.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Woodwinds/Contrabassoon/Contrabassoon.sfz.7z) (255.55 KiB)

---

</details>

<details><summary>Contrabassoon.sts.7z</summary>

> Original sample files for `Muse Woodwinds` `Contrabassoon` (`Contrabassoon.sts`)

> [Download Contrabassoon.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Woodwinds/Contrabassoon.sts.7z) (246.74 MiB)

---

</details>

#### English Horn
<details><summary>English Horn.sfz.7z</summary>

> Original sfz files for `Muse Woodwinds` `English Horn` (`English Horn.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Woodwinds` version: `0.5.23`

> [Download English Horn.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Woodwinds/English%20Horn/English%20Horn.sfz.7z) (424.46 KiB)

---

</details>

<details><summary>English Horn.sts.7z</summary>

> Original sample files for `Muse Woodwinds` `English Horn` (`English Horn.sts`)

> [Download English Horn.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Woodwinds/English%20Horn.sts.7z) (241.18 MiB)

---

</details>

#### Flute 1
<details><summary>Flute 1.sfz.7z</summary>

> Original sfz files for `Muse Woodwinds` `Flute 1` (`Flute 1.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Woodwinds` version: `0.5.23`

> [Download Flute 1.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Woodwinds/Flute%201/Flute%201.sfz.7z) (599.44 KiB)

---

</details>

<details><summary>Flute 1.sts.7z</summary>

> Original sample files for `Muse Woodwinds` `Flute 1` (`Flute 1.sts`)

> [Download Flute 1.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Woodwinds/Flute%201.sts.7z) (359.9 MiB)

---

</details>

#### Flute 2
<details><summary>Flute 2.sfz.7z</summary>

> Original sfz files for `Muse Woodwinds` `Flute 2` (`Flute 2.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Woodwinds` version: `0.5.23`

> [Download Flute 2.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Woodwinds/Flute%202/Flute%202.sfz.7z) (592.39 KiB)

---

</details>

<details><summary>Flute 2.sts.7z</summary>

> Original sample files for `Muse Woodwinds` `Flute 2` (`Flute 2.sts`)

> [Download Flute 2.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Woodwinds/Flute%202.sts.7z) (326.83 MiB)

---

</details>

#### Oboe
<details><summary>Oboe.sfz.7z</summary>

> Original sfz files for `Muse Woodwinds` `Oboe` (`Oboe.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Woodwinds` version: `0.5.23`

> [Download Oboe.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Woodwinds/Oboe/Oboe.sfz.7z) (492.24 KiB)

---

</details>

<details><summary>Oboe.sts.7z</summary>

> Original sample files for `Muse Woodwinds` `Oboe` (`Oboe.sts`)

> [Download Oboe.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Woodwinds/Oboe.sts.7z) (193.64 MiB)

---

</details>

#### Piccolo
<details><summary>Piccolo.sfz.7z</summary>

> Original sfz files for `Muse Woodwinds` `Piccolo` (`Piccolo.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Woodwinds` version: `0.5.23`

> [Download Piccolo.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Woodwinds/Piccolo/Piccolo.sfz.7z) (350.66 KiB)

---

</details>

<details><summary>Piccolo.sts.7z</summary>

> Original sample files for `Muse Woodwinds` `Piccolo` (`Piccolo.sts`)

> [Download Piccolo.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Woodwinds/Piccolo.sts.7z) (189.41 MiB)

---

</details>

#### Soprano Sax
<details><summary>Soprano Saxophone.sfz.7z</summary>

> Original sfz files for `Muse Woodwinds` `Soprano Sax` (`Soprano Saxophone.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Woodwinds` version: `0.5.23`

> [Download Soprano Saxophone.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Woodwinds/Soprano%20Sax/Soprano%20Saxophone.sfz.7z) (465.88 KiB)

---

</details>

<details><summary>Soprano Saxophone.sts.7z</summary>

> Original sample files for `Muse Woodwinds` `Soprano Sax` (`Soprano Saxophone.sts`)

> [Download Soprano Saxophone.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Woodwinds/Soprano%20Sax/Soprano%20Saxophone.sts.7z) (138.02 MiB)

---

</details>

#### Tenor Sax
<details><summary>Tenor Saxophone.sfz.7z</summary>

> Original sfz files for `Muse Woodwinds` `Tenor Sax` (`Tenor Saxophone.spx`).
> 
> These files may be non-standard and can't be played in many players, or should have keys modified before being played correctly. As a result, **download of this file is only for users who know what you are doing**.
> 
> `Muse Woodwinds` version: `0.5.23`

> [Download Tenor Saxophone.sfz.7z](https://dl.muse-sounds.work/public/sfz/Muse%20Woodwinds/Tenor%20Sax/Tenor%20Saxophone.sfz.7z) (498.38 KiB)

---

</details>

<details><summary>Tenor Saxophone.sts.7z</summary>

> Original sample files for `Muse Woodwinds` `Tenor Sax` (`Tenor Saxophone.sts`)

> [Download Tenor Saxophone.sts.7z](https://dl.muse-sounds.work/public/sts/Muse%20Woodwinds/Tenor%20Sax/Tenor%20Saxophone.sts.7z) (277.85 MiB)

---

</details>


