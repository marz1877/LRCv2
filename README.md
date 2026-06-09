# LRCv2 Specefications

## Software
LRCv2 needs WYSIWYG editor specially when using many features at once. Something like https://github.com/Royce551/FRESHLyricMaker. For Kareoke fork https://github.com/UltraStar-Deluxe/USDX/.

## Use Cases
1. Lyrics
2. Meaning
3. Translation: Multi-lingua people, Language learning, Forign music listening
4. Kareoke with Time and Pitch
5. Chords: Music Learner

## Automation
**All features for creating .lrc can be automated**
1. Lyrics: Genius (https://github.com/johnwmillr/LyricsGenius) or Speech-to-Text (https://github.com/openai/whisper).
  - Synced Lyrics: MusixMatch or time lyrics using https://github.com/oseiskar/autosubsync, https://juanumusic.github.io/lyricssyncher/, https://github.com/Alien501/lrc-generator.
3. Chords: Riffstation software or UltimateGuitar DB.
4. Translation: Musixmatch or Google Translate / Offline (https://github.com/argosopentech/argos-translate).
5. Meaning: Genius.
6. For Karaoke:
  - Vocal Melody Isolation using (See below)
  - Covert it to MIDI using (See Below), for Karaoke Pitch matching.

- 1 lrcv2 can have all - Synced Lyrics + Meaning + Translatopn + Chords + Kareoke Data.

## Storing Lyrics
- File Extension .lrc or in metadata.

- ChordPro uses Title `{title: You Are My Sunshine}` and LRCv1 `[ti:Let's Twist Again]` and for Sections LRCv2 `{c:Verse 1}` but LRCv2 recommends [] for everything `[c:Verse 1]`

### Player to read filename with type speficied
*When an audio file is played and there is a .lrc in the same directory or it can be specefied in the player.*
*Can have seperate .lrc per usecase or all-in-one*

*Suggested file naming*
```
AudioFilename.lrc              -
AudioFilename_translation.lrc  -  for seperate translation lrc
AudioFilename_meaning.lrc      -  for seperate meaning lrc
AudioFilename.chordpro         -  for chords
```
#### Metadata field names -
```
SYNCEDLYRICS         - Lyrics
LYRICS_translation   - Translation
  LYRICS_translation_es   - Translation Spanish
LYRICS_meaning       - Meaning
Chordpro             - Chords
```


## 1.1 Metadata
**lrc version info**

**Start of the data**
```
[lrc version:2.0]
[language:en,es]
[features:meanings,translations,chords,colors]
[encoding:UTF-8]
```

Artist: `[ar:Song artist]`
Language: `[language:en,es,de]`
Sections: `[c:Verse 1]`

# 2. Multi Singers

Format
```
[00:12.00] [Singer:Jhon]Line 1 lyrics[/Singer:Jhon]
[00:16.00] [Singer:Luis]Line 2 lyrics[/Singer:Luis]
[1:01.00] [Singer:William,Luis]Line 3 lyrics [/Singer:William,Luis]
```

### Also See - previous standard achive similar objective but there not adapted -
- Extended LRC - (Wikipedia removed it) https://en.wikipedia.org/wiki/LRC_(file_format)#Simple_format_extended
- Walaoke_extension:_gender - https://en.wikipedia.org/wiki/LRC_(file_format)#Walaoke_extension:_gender

## 2.1 Per Section

`[Verse 1 : Vocalist Name]`

Genius Example - https://genius.com/Krewella-crying-on-the-dancefloor-lyrics . Genius has multi-singer infomation sometimes.

```
[c:Verse 1: Singer Name]
[00:13.10] Some
[00:18.58] Lovely
[00:24.94] Lyrics
[00:31.38] I hope music players adopt your proposal
# Blank synced line ends the section?
[00:37.58]
```

## 3.1 Meaning: Contextual - by word/line

Genius: Lyric meaning database

### Format
```
[00:00.00] [M]I walk a lonely road[/M:The singer is feeling lonely and isolated, and is on a path that no one else is traveling with him. He may feel like he doesn't fit in with others and is struggling to find his place in the world.]
[00:15.67] [M]Don't know where it goes[/M:The singer is uncertain of where the path will take him, and is unsure of what the future holds.]
[00:28.03] [M]My shadow's the only one that walks beside me [/M:The singer feels alone and abandoned, as represented by his shadow being the only companion on his journey.]
[00:42.25] [M]I walk this empty street [/M:The singer is walking down a street that feels barren and lifeless, emphasizing his feelings of loneliness and isolation.]
[00:53.04] [M]On the boulevard of broken dreams[/M:The "boulevard of broken dreams" is a metaphor for a place where people go to give up on their hopes and aspirations, and the singer feels like he is a part of this world of lost dreams and broken promises.]
```

### Hyperlink inside Meaning

Meaning can have hyperlinks inside them
```
[Verse 1]
[M]I walk a lonely road
The only one that I have ever known
Don't know where it goes
But it's home to me, and I walk alone[/M:It’s possible these lines were inspired by the chorus of Whitesnake’s ‘80s hit single “Here I Go Again”:]

[M]I walk this empty street
On the Boulevard of Broken Dreams[/M:The phrase “Boulevard of Broken Dreams” was first coined in a 1933 song recorded by many, from Bing Crosby to Amy Winehouse. It has since become a nickname for [Los Angeles' Sunset Boulevard](https://www.tripadvisor.com/Attraction_Review-g32655-d156501-Reviews-Sunset_Boulevard-Los_Angeles_California.html) – it passes through Hollywood, so many have seen their stardom dreams die in the street.

The title, “Boulevard of Broken Dreams”, is inspired by Gottfried Helnwein’s 1984 painting of the same name. This is a direct visual quotation of the painting “Nighthawks” by Edward Hopper that depicts a downtown diner at night. Helnwein replaced the diner’s occupants with American pop culture icons Humphrey Bogart, Marilyn Monroe, James Dean, and Elvis Presley to connect its bleak atmosphere with the tragic fate of some celebrities.]
```

# Break Line
**Explicitly add Breaklines**
```
I walk a lonely road [Br]
The only one that I have ever known [Br]
Don't know where it goes [Br]
But it's home to me, and I walk alone [Br]
I walk this empty street [Br]
On the Boulevard of Broken Dreams [Br]
```

## 3.2 Language Translation - Per Line, Phrase, Word

- Player MAY include dictionary for per word/phrase/slang/idiom translation.

- Translation example:
  - https://www.musixmatch.com/lyrics/Jenni-Vartiainen/Miss%C3%A4-muruseni-on/translation/english
  - https://lyricstranslate.com/en/missae-muruseni-where-my-sweetheart.html-0

### Format Translation
- MUST specify translation lanuages. e.g. for German to English use `de>en`.
- One Lyric MAY multiple translations.
- Format `[00:13.75] [T,lang1>lang2]Line[/T: Transaltion]`
- Example
```
[00:13.75] [T,fin>eng]Yöllä taas mä menin parvekkeelle nukkumaan,[/T: At night again I went to sleep in the balcony, CommonUsage: where's my baby?]
[00:19.62] [T,fin>eng]Jotta lähempänä mua ois hän[/T: So that they would be closer to me]
[00:25.30] [T,fin>eng]Pediltäni taivas näkyy, ryhdyin oottamaan,[/T: From my bed I saw the sky, begun to wait]
[00:57.81] Tuuli tuule sinne [T,fin>eng]missä muruseni on[/T: Where my loved ones are, CommonUsage: where's my baby?]
```

<details>
  <summary>## Current Format with per line translation and both laguages in sepearte lines with same time stamp -</summary>

```
[00:13.75] Yöllä taas mä menin parvekkeelle nukkumaan,
[00:13.75] At night again I went to sleep in the balcony
[00:19.62] Jotta lähempänä mua ois hän
[00:19.62] So that they would be closer to me
[00:25.30] Pediltäni taivas näkyy, ryhdyin oottamaan,
[00:25.30] From my bed I saw the sky, begun to wait
[00:30.92] Että näen tähden lentävän
[00:30.92] To see a star flying
[00:36.59] Sanovat jos jossain huomaa tähdenlennon niin
[00:36.59] They say that if you somewhere spot a shooting star
[00:42.17] Toivoa voit silloin mitä vaan
[00:42.17] Then you can wish for anything
[00:47.75] Yöllä ylös taivaalle mä pyynnön kuiskasin
[00:47.75] At night for the sky I whispered a plea...
[00:53.53] Kävisipä pian tuulemaan
[00:53.53] Wish the wind would soon start to blow
```
</details>

### 3.3 Contexual Language Translation - per Word/Phrase

Dictionary in the player may not be useful as word can be contexual and as used in gerneral/other cases.

### Format

```
[00:00.00] [WordMeanind,de>en]Überheblich[/WordMeanind:Arrogant], [WordMeanind]überlegen[/WordMeanind:consider]
```

## 4. Suggested UI for Translation and Meaning Feature

![ui](https://user-images.githubusercontent.com/105455604/168247326-d772633e-c073-4928-9400-ada37fa4817d.png)

When meaning mode from the top button is selected hovering should show line, phrase or paragraph hilighted depening on context (when explaing song lyrics only one line or paragraph is sufficient) 

In translation mode: hovering over should hilight phrases (as small as possible) giving meaning of the phrase and words used targeted for langauge learning.

# 5. Custom Text Color (for expression)

# Format
```
[02:16.00] [cr=#dc143c]Destroy yourself, see who gives a[/cr] [cr=#420612]duck[/cr]
[02:18.00] See who gives a duck
```

# 6. Censoring Words
- Players MAY have option to censor explicit words eg. F**k and S**t or completely ****.
- Explicit Dictionary - https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words

# 7. Custom Text Size (for word expression)
- MAY turn off when using slidding lyrics depending of screen types. e.g. phone with scrolling lyrics size can be hard to dynamicly resize.

### Format
```
[02:16.00] [sz=10]Destroy yourself, see who gives a[/sz] [sz=20]duck[/sz]
[02:18.00] See who gives a duck
```

## 8. Karaeoke - Voice melody MIDI + Mic Input using Pitch-Recognision and midi roll UI

1. Voice melody MIDI
- Can be placed alongside with audio file.
- or Extracted realtime using https://hub.docker.com/r/aclmb/stemgen steam seperator.

#### [Recommended Tools] Audio-to-Midi Convertion:
 - https://www.sonicvisualiser.org/tony/ , https://github.com/sonic-visualiser/tony
 - https://github.com/spotify/basic-pitch - Audio-to-Midi   
 - https://github.com/DamRsn/NeuralNote .

2. Player MUST show midi-piano-roll to work as a karaeoke or Singing Learing Tool.

#### Other Audio+MIDI Formats
  1. Multitrack OGG
  1. MP4/M4A with SMF tracks
  1. WAV with MIDI Metadata

 - https://github.com/jeffreyjohnens/MetaMIDIDataset

It is "not similar" to https://en.wikipedia.org/wiki/CD%2BG / https://en.wikipedia.org/wiki/MP3%2BG

<details>
  <summary>UI</summary>
  
![image](https://user-images.githubusercontent.com/105455604/168251330-d98a8d35-936d-44b7-9988-b86f71f4a67c.png)
</details>

# 9. Lyrics + Chords

- Player MAY add options to -
  - Transpose scale / "No Capo version"
  - Show chord Progression eg. `II V IV` (https://chromewebstore.google.com/detail/kantan-chord/ncdpcgdgemdklhocjgecijjjhaboopbp)

- ChordPro - https://github.com/ChordPro/chordpro, https://www.chordpro.org/
<details>
  <summary>ChordPro Format</summary>

```
{title: You Are My Sunshine}

{c:Verse 1}
[G]The other night dear as I lay sleeping
[G7]I dreamed I [C]held you in my [G]arms
[G7]But when I a[C]woke dear I was mis[G]taken
So I hung my [D7]head and [G]cried

{c:Chorus}
{soc}
You are my sunshine my only sunshine
[G7]You make me [C]happy when skies are [G]gray
[G7]You'll never [C]know dear how much I [G]love you
Please don't take [D7]my sunshine a[G]way
{eoc}
```
</details>


### LRCv2 Format

Format `[cr]Lyric [/cr=Em]`

<details>
  <summary>Example</summary>  
 
```
[00:22.37] [cr]I walk a [/cr=Em][cr]lonely road, [/cr=G]the [cr]only one that [/cr=D][cr]I have ever known[/cr=Em]
[00:29.45] [cr]Don't know where it [/cr=G][cr]goes,[/cr=Em] [cr]but it's home to me [/cr=G][cr]and I walk alone[/cr=Em]
[00:36.72] [cr]I walk this empty[/cr=Em] [cr]street[/cr=G][cr]On the Boulevard of Broken Dreams[/cr=D]
[00:43.78] [cr]Where the city[/cr=Em] [cr]sleeps[/cr=G][cr]and I'm the only one and I walk alone[/cr=Em]
[00:57.58] [cr]I walk alone,[/cr=Em] [cr]I walk alone[/cr=G][cr]I walk alone[/cr=D][cr]I walk alone and I walk a...[/cr=Em]
```
</details>

# Other Features

### Syllable-by-Syllable
**Only useful for kareoke or rap lyrics**
<details>
  <summary>Format</summary>
  
```
[00:11.45] I [00:11.89] walk [00:12.33] a [00:12.77] lone- [00:13.43] ly [00:13.75] road
[00:14.09] The [00:14.48] on- [00:14.87] ly [00:15.26] one [00:15.65] that [00:16.05] I [00:16.44] have [00:16.83] ev- [00:17.04] er [00:17.25] known
[00:17.25] Don't [00:17.95] know [00:18.64] where [00:19.34] it [00:19.69] goes
[00:20.03] But [00:20.73] it's [00:21.43] home [00:22.12] to [00:22.82] me [00:23.52] and [00:24.21] I [00:24.91] walk [00:25.61] a- [00:26.31] lone

[00:27.93] I [00:28.55] walk [00:29.18] this [00:29.80] emp- [00:30.42] ty [00:31.05] street
[00:31.68] On [00:32.03] the [00:32.38] Bou- [00:32.73] le- [00:33.08] vard [00:33.42] of [00:33.77] Bro- [00:34.12] ken [00:34.47] Dreams
[00:33.77] Where [00:34.59] the [00:35.40] ci- [00:36.22] ty [00:36.63] sleeps
[00:37.04] And [00:37.58] I'm [00:38.12] the [00:38.66] on- [00:39.20] ly [00:39.74] one [00:40.28] and [00:40.82] I [00:41.10] walk [00:41.37] a-lone

[00:41.37] I [00:41.84] walk [00:42.31] a-lone [00:43.26] I [00:43.73] walk [00:44.20] a-lone
[00:45.15] I [00:45.80] walk [00:46.45] a-lone [00:47.75] I [00:48.40] walk [00:49.05] a-

[00:51.64] My [00:52.07] shad- [00:52.50] ow's [00:52.93] the [00:53.36] on- [00:53.79] ly [00:54.22] one [00:54.65] that [00:55.08] walks [00:55.51] be- [00:55.94] side [00:56.37] me
[00:56.40] My [00:56.99] shal- [00:57.58] low [00:58.16] heart's [00:58.75] the [00:59.34] on- [00:59.93] ly [01:00.52] thing [01:01.11] that's [01:01.69] beat- [01:02.28] ing
[01:03.46] Some- [01:03.99] times [01:04.52] I [01:05.05] wish [01:05.58] some- [01:06.11] one [01:06.64] out [01:07.17] there [01:07.70] will [01:08.23] find [01:08.46] me
[01:08.72] 'Til [01:09.51] then [01:10.30] I [01:11.09] walk [01:11.88] a- [01:12.67] lone

[01:13.48] Ah-ah [01:15.22] Ah-ah [01:16.96] Ah-ah [01:18.70] Ah-ah
[01:20.44] Ah-ah [01:22.05] Ah-ah [01:23.66] Ah-ah

[01:25.28] I'm [01:25.89] walk- [01:26.50] ing [01:27.10] down [01:27.71] the [01:28.31] line
[01:28.92] That [01:29.44] di- [01:29.96] vides [01:30.48] me [01:31.00] some- [01:31.52] where [01:32.04] in [01:32.56] my [01:32.74] mind
[01:31.64] On [01:32.31] the [01:32.98] bor- [01:33.65] der- [01:34.15] line
[01:34.32] Of [01:34.82] the [01:35.33] edge [01:35.84] and [01:36.35] where [01:36.86] I [01:37.37] walk [01:37.88] a- [01:38.39] lone

[01:39.91] Read [01:40.84] be- [01:41.77] tween [01:42.70] the [01:43.63] lines
[01:44.56] What's [01:45.07] fucked [01:45.58] up [01:46.10] and [01:46.61] ev- [01:47.12] ery- [01:47.63] thing's [01:48.14] al- [01:48.40] right
[01:48.66] Check [01:49.48] my [01:50.30] vi- [01:51.12] tal [01:51.53] signs
[01:51.95] To [01:52.33] know [01:52.70] I'm [01:53.08] still [01:53.45] a- [01:53.83] live [01:54.20] and [01:54.58] I [01:54.95] walk [01:55.33] a-lone
```
</details>

### Word-by-Word
- Use Case: Millisecond accurate for Karaeoke Mode 
- Same as LRC's A2_extension:_word_time_tag - https://en.wikipedia.org/wiki/LRC_(file_format)#A2_extension:_word_time_tag

- Words with milliseconds accuracy - Will hilight words as they are being played. This will be usefull for kareoke.

### Format

<details>
  <summary>Click me</summary>

```
[Verse 1]
[00:00.00]I <00:00.00> walk <00:00.38> a <00:00.52> lonely <00:00.95> road
[00:01.79]The <00:02.19> only <00:02.40> one <00:02.79>
[00:03.08]that <00:03.25> I <00:03.40> have <00:03.70> ever <00:03.90> known
[00:05.00]Don't <00:05.18> know <00:05.36> where <00:05.54> it <00:05.72> goes
[00:07.15]But <00:07.32> it's <00:07.60> home <00:07.91> to <00:08.08> me, <00:08.23> and <00:08.45> I <00:08.61> walk <00:08.81> alone

[Chorus]
[00:14.15]I <00:14.38> walk <00:14.57> this <00:14.72> empty <00:15.04> street
[00:18.17]On <00:18.38> the <00:18.51> Boulevard <00:18.89> of <00:19.05> Broken <00:19.35> Dreams
[00:20.69]Where <00:20.89> the <00:21.07> city <00:21.27> sleeps
[00:26.14]and <00:26.32> I'm <00:26.50> the <00:26.68> only <00:27.06> one, <00:27.24> and <00:27.45> I <00:27.61> walk <00:27.81> alone
```
</details>

## Expect Adaptation By

**Music Streaming**
1. [Spotify](https://open.spotify.com/)
1. ‎[Apple Music](https://music.apple.com/)
2. [Tencent Music](https://www.tencentmusic.com/en-us/)
3. [Amazon Music](https://music.amazon.com)

**Lyrics**
1. [MusixMatch](https://www.musixmatch.com/)
1. [Genius](https://genius.com/)

**Player**
1. https://www.plex.tv/plexamp/

**Karaeoke**
1. https://github.com/DoubleDee73/Yass-Reloaded
1. https://db.openkj.org/
1. https://github.com/UltraStar-Deluxe/USDX
1. https://github.com/gyunaev/spivak

**Lyrics Player/Editor**
1. [OpenLyrics foobar2000 lyrics component](https://github.com/jacquesh/foo_openlyrics)
1. https://github.com/Spikatrix/LRC-Editor
1. https://lrc-maker.github.io/
1. https://github.com/lemutec/LyricStudio
1. Cross-platform advanced subtitle editor - https://github.com/Aegisub/Aegisub

**Audio Codec/Metadata**

1. [Xiph.Org Foundation](https://xiph.org/)
1. [FFmpeg](https://ffmpeg.org/)

# Other Formats
1. ID3 Specs - https://id3.org/Lyrics3v21. ID3 standardized SYNCEDLYRICS but not .lrc.
1. **OpenLyrics** - (https://github.com/openlyrics/openlyrics) - free-open XML standard. app / OS-independant song format for interoperability between apps
1. **Lyrics File** (open extensible lyrics format) - https://github.com/tranxuanthang/lrcget/releases/tag/2.0.0 Word-by-word lyric file format
<details>
  <summary>Lyricsfile Format</summary>
  
```
version: '1.0'
metadata:
  title: 'Your Shape'
  artist: 'Eddy'
  duration_ms: 235000

lines:
  - text: "The school isn't the best place to find a lover"
    start_ms: 12450
    end_ms: 18200
    words:
      - text: 'The '
        start_ms: 12450
        end_ms: 12900
      - text: 'school '
        start_ms: 12900
        end_ms: 13500
      - text: "isn't "
        start_ms: 13500
        end_ms: 14200
      - text: 'the '
        start_ms: 14200
        end_ms: 14600
      - text: 'best '
        start_ms: 14600
        end_ms: 15200
      - text: 'place '
        start_ms: 15200
        end_ms: 15800
      - text: 'to '
        start_ms: 15800
        end_ms: 16200
      - text: 'find '
        start_ms: 16200
        end_ms: 16800
      - text: 'a '
        start_ms: 16800
        end_ms: 17100
      - text: 'lover'
        start_ms: 17100
        end_ms: 18200
  - text: 'So the bar is where I go'
    start_ms: 18500
    end_ms: 22100
    words:
      - text: 'So '
        start_ms: 18500
        end_ms: 19000
      - text: 'the '
        start_ms: 19000
        end_ms: 19400
      - text: 'bar '
        start_ms: 19400
        end_ms: 20000
      - text: 'is '
        start_ms: 20000
        end_ms: 20400
      - text: 'where '
        start_ms: 20400
        end_ms: 21000
      - text: 'I '
        start_ms: 21000
        end_ms: 21400
      - text: 'go'
        start_ms: 21400
        end_ms: 22100

plain: |
  [Verse 1]
  The club isn't the best place to find a lover
  So the bar is where I go
```
</details>

## License
- LRCv2 specs is free to use.
- Must give credit.

### Synced-Lyric Sources
1. https://www.musixmatch.com/
2. https://www.rentanadviser.com
3. https://www.megalobiz.com/
4. https://www.lyricsify.com/

Open for contribution.
