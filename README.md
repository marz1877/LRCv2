# LRCv2 Specifications
LRC v2 format specs proposal. Synced Lyrics with Meaning, Translation, Singer metadata, Chords, Kareoke with Time and Pitch

## Software
LRCv2 needs WYSIWYG editor specially when using many features at once. Something like https://github.com/Royce551/FRESHLyricMaker. For Kareoke fork https://github.com/UltraStar-Deluxe/USDX/.

## Use Cases
1. Synced Lyrics
2. Meaning
3. Translation: Multi-lingua people, Language learning, Forign music listening
4. Kareoke with Time and Pitch
5. Chords: Music Learner

## Automation
**All features for creating .lrc can be automated**
1. Lyrics
  - Lyrics: Genius (https://github.com/johnwmillr/LyricsGenius)
  - Speech-to-Text: https://github.com/openai/whisper
  - Synced Lyrics DB: MusixMatch
  - Lyrics Syncer: https://github.com/oseiskar/autosubsync , https://juanumusic.github.io/lyricssyncher/ , https://github.com/Alien501/lrc-generator .
3. Chords:
  - Software: Riffstation
  - DB: UltimateGuitar
4. Translation:
  - DB: Musixmatch
  - Service: Google Translate
  - Software: Offline (https://github.com/argosopentech/argos-translate)
5. Meaning: Genius
6. For Karaoke:
  - Vocal Melody Isolation using (See below)
  - Covert it to MIDI using (See Below), for Karaoke Pitch matching.

- One LRCv2 file can have all - Synced Lyrics + Meaning + Translation + Chords + Kareoke Data.

## Storing Lyrics
**File Extension .lrc or in metadata.**
- When an audio file is played and there is a .lrc in the same directory or it can be specefied in the player.
- Player to read filename with type speficied
- Can have seperate .lrc per usecase or all-in-one
*Suggested file naming*
```
AudioFilename.lrc              -
AudioFilename_translation.lrc  -  for seperate translation lrc
AudioFilename_meaning.lrc      -  for seperate meaning lrc
AudioFilename.chordpro         -  for chords
```
#### Metadata fields -
```
SYNCEDLYRICS             - Synced Lyrics
SYNCEDLYRICS_Word        - Word-by-Word Lyrics
SYNCEDLYRICS_Syllable        - Syllable-by-Syllable Lyrics
LYRICS_TRANSLATION       - Translation
  LYRICS_TRANSLATION_ES   - Translation Spanish
LYRICS_meaning       - Meaning
Chordpro             - Chords
```

## Metadata
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

- NOTE: LRCv1 uses `[ti:Let's Twist Again]` and ChordPro uses Title `{title: You Are My Sunshine}` 

# 1. Time Stamping
- MUST use Breakline [Br] at the end of each line
- MUST using opening and closing time.

## Break Line
- MUST Explicitly add Breaklines using `[Br]`

<details>
  <summary>Format</summary>

```
I walk a lonely road [Br]
The only one that I have ever known [Br]
Don't know where it goes [Br]
But it's home to me, and I walk alone [Br]
I walk this empty street [Br]
On the Boulevard of Broken Dreams [Br]
```
</details>details>

## Word-by-Word
- Use Case: Alternative to syllable mode for Karaeoke Mode 
- Other Format: [LRC's A2_extension:_word_time_tag](https://en.wikipedia.org/wiki/LRC_(file_format)#A2_extension:_word_time_tag)
- Players MAY hilight words as they are being played.

### Format

<details>
  <summary>Formar</summary>

```
<00:11.45> I <00:11.89> walk <00:12.33> a <00:12.77> lone- <00:13.43> ly <00:13.75> road </00:14.09> [Br]
<00:14.09> The <00:14.48> on- <00:14.87> ly <00:15.26> one <00:15.65> that <00:16.05> I <00:16.44> have <00:16.83> ev- <00:17.04> er <00:17.25> known </00:17.25> [Br]
<00:17.25> Don't <00:17.95> know <00:18.64> where <00:19.34> it <00:19.69> goes </00:20.03> [Br]
<00:20.03> But <00:20.73> it's <00:21.43> home <00:22.12> to <00:22.82> me <00:23.52> and <00:24.21> I <00:24.91> walk <00:25.61> a- <00:26.31> lone </00:27.93> [Br]

<00:27.93> I <00:28.55> walk <00:29.18> this <00:29.80> emp- <00:30.42> ty <00:31.05> street </00:31.68> [Br]
<00:31.68> On <00:32.03> the <00:32.38> Bou- <00:32.73> le- <00:33.08> vard <00:33.42> of <00:33.77> Bro- <00:34.12> ken <00:34.47> Dreams </00:35.00> [Br]
<00:33.77> Where <00:34.59> the <00:35.40> ci- <00:36.22> ty <00:36.63> sleeps </00:37.04> [Br]
<00:37.04> And <00:37.58> I'm <00:38.12> the <00:38.66> on- <00:39.20> ly <00:39.74> one <00:40.28> and <00:40.82> I <00:41.10> walk <00:41.37> a-lone </00:41.37> [Br]

<00:41.37> I <00:41.84> walk <00:42.31> a-lone <00:43.26> I <00:43.73> walk <00:44.20> a-lone </00:45.15> [Br]
<00:45.15> I <00:45.80> walk <00:46.45> a-lone <00:47.75> I <00:48.40> walk <00:49.05> a- </00:51.64> [Br]
```
</details>

## Syllable-by-Syllable
Use Case: Only kareoke or rap lyrics
<details>
  <summary>Syllable-by-Syllable Format</summary>
  
```
<00:11.45> I <00:11.89> walk <00:12.33> a <00:12.77> lone- <00:13.43> ly <00:13.75> road </00:14.09> [Br]
<00:14.09> The <00:14.48> on- <00:14.87> ly <00:15.26> one <00:15.65> that <00:16.05> I <00:16.44> have <00:16.83> ev- <00:17.04> er <00:17.25> known </00:17.25> [Br]
<00:17.25> Don't <00:17.95> know <00:18.64> where <00:19.34> it <00:19.69> goes </00:20.03> [Br]
<00:20.03> But <00:20.73> it's <00:21.43> home <00:22.12> to <00:22.82> me <00:23.52> and <00:24.21> I <00:24.91> walk <00:25.61> a- <00:26.31> lone </00:27.93> [Br]

<00:27.93> I <00:28.55> walk <00:29.18> this <00:29.80> emp- <00:30.42> ty <00:31.05> street </00:31.68> [Br]
<00:31.68> On <00:32.03> the <00:32.38> Bou- <00:32.73> le- <00:33.08> vard <00:33.42> of <00:33.77> Bro- <00:34.12> ken <00:34.47> Dreams </00:35.00> [Br]
<00:33.77> Where <00:34.59> the <00:35.40> ci- <00:36.22> ty <00:36.63> sleeps </00:37.04> [Br]
<00:37.04> And <00:37.58> I'm <00:38.12> the <00:38.66> on- <00:39.20> ly <00:39.74> one <00:40.28> and <00:40.82> I <00:41.10> walk <00:41.37> a-lone </00:41.37> [Br]

<00:41.37> I <00:41.84> walk <00:42.31> a-lone <00:43.26> I <00:43.73> walk <00:44.20> a-lone </00:45.15> [Br]
<00:45.15> I <00:45.80> walk <00:46.45> a-lone <00:47.75> I <00:48.40> walk <00:49.05> a- </00:51.64> [Br]
```
</details>

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

# 2. Multi Singers
`[0:00.00] <s:Singer1,Singer2>Line</s:Singer1>  

<details>
  <summary>Format</summary>

  ```
[00:12.00] <s:Jhon>Line 1 lyrics</s:Jhon>
[00:16.00] <s:Luis>Line 2 lyrics</s:Luis>
[1:01.00] <s:William,Luis>Line 3 lyrics</s:William,Luis>
```
</details>

#### Also See - other formats with similar objective -
- Extended LRC - (Wikipedia removed it) https://en.wikipedia.org/wiki/LRC_(file_format)#Simple_format_extended
- Walaoke_extension:_gender - https://en.wikipedia.org/wiki/LRC_(file_format)#Walaoke_extension:_gender

## 2.1 Per Section

- LRCv1 uses for `{c:Verse 1}`
- LRCv2 recommends [] for everything `[c:Verse 1]`
- If Entire Section is sung by 1 singer then `[c:Verse 1 : Vocalist Name]`

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

# 3 Meaning

- Recommended Lyric meaning database: Genius

## Contextual
by Paragrah/line/word

<details>
  <summary>Format</summary>
  
### Format
```
[00:00.00] [M]I walk a lonely road[/M:The singer is feeling lonely and isolated, and is on a path that no one else is traveling with him. He may feel like he doesn't fit in with others and is struggling to find his place in the world.]
[00:15.67] [M]Don't know where it goes[/M:The singer is uncertain of where the path will take him, and is unsure of what the future holds.]
[00:28.03] [M]My shadow's the only one that walks beside me [/M:The singer feels alone and abandoned, as represented by his shadow being the only companion on his journey.]
[00:42.25] [M]I walk this empty street [/M:The singer is walking down a street that feels barren and lifeless, emphasizing his feelings of loneliness and isolation.]
[00:53.04] [M]On the boulevard of broken dreams[/M:The "boulevard of broken dreams" is a metaphor for a place where people go to give up on their hopes and aspirations, and the singer feels like he is a part of this world of lost dreams and broken promises.]
```
</details>

## Hyperlink inside Meaning
- Meaning MAY CONTAIN hyperlinks

<details>
  <summary>Format</summary>
  
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
</details>

## 3.2 Language Translation - Per Word,Phrase, Line

### Word-by-Word
- Player MAY include dictionary for per word/phrase/slang/idiom translation.

### Line(s)
- Recommended Translated Lyrics DB:
  - https://lyricstranslate.com/ eg. https://lyricstranslate.com/en/missae-muruseni-where-my-sweetheart.html-0
  - https://www.musixmatch.com/ eg. https://www.musixmatch.com/lyrics/Jenni-Vartiainen/Miss%C3%A4-muruseni-on/translation/english

### Translation Format
- MUST specify translation lanuages. e.g. German to English is `de:en`.
- One Lyric MAY multiple translations.
- Format `[00:13.75] [T:lang1:lang2]Line[/T: Transaltion]`
- MAY contain literal and common usage meaning
<details>
  <summary>Example</summary>
  
```
[00:13.75] [T:fin:eng]Yöllä taas mä menin parvekkeelle nukkumaan,[/T: Literal: At night again I went to sleep in the balcony, CommonUsage: where's my baby?]
[00:19.62] [T:fin:eng]Jotta lähempänä mua ois hän[/T:So that they would be closer to me]
[00:25.30] [T:fin:eng]Pediltäni taivas näkyy, ryhdyin oottamaan,[/T:From my bed I saw the sky, begun to wait]
[00:57.81] Tuuli tuule sinne [T:fin:eng]missä muruseni on[/T:Where my loved ones are, CommonUsage: where's my baby?]
```
</details>

MusixMatch Syntax and UI
<details>
  <summary>MusixMatch Syntax and UI - with per-line translation and both laguages in sepearte lines with same time stamp</summary>

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

## 3.3 Contexual Language Translation - per Word/Phrase

- NOTE: Dictionary in the player may not be useful as word can be contexual and as used in gerneral/other cases.
- MAY use LLMs.

### Format

```
[00:00.00] [WordMeanind,de>en]Überheblich[/WordMeanind:Arrogant], [WordMeanind]überlegen[/WordMeanind:consider]
```

## 4. Suggested UI for Translation and Meaning Feature

![ui](https://user-images.githubusercontent.com/105455604/168247326-d772633e-c073-4928-9400-ada37fa4817d.png)

- In meaning mode: hovering should show line, phrase or paragraph hilighted depening on context (explaination for only lines or paragraph is sufficient, words may be used rarely) 
- In translation mode: hovering over should hilight phrases (as small as possible) giving meaning of the phrase and words used targeted for langauge learning.

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
<details>
  <summary>ClickMe</summary>
```
[02:16.00] [sz=10]Destroy yourself, see who gives a[/sz] [sz=20]duck[/sz]
[02:18.00] See who gives a duck
```
</details>

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

Format `[ch]Lyric [/ch=Em]`

<details>
  <summary>LRCv2 Format</summary>  
 
```
[00:22.37] [ch]I walk a [/ch=Em][ch]lonely road, [/ch=G]the [ch]only one that [/ch=D][ch]I have ever known[/ch=Em]
[00:29.45] [ch]Don't know where it [/ch=G][ch]goes,[/ch=Em] [ch]but it's home to me [/ch=G][ch]and I walk alone[/ch=Em]
[00:36.72] [ch]I walk this empty[/ch=Em] [ch]street[/ch=G][ch]On the Boulevard of Broken Dreams[/ch=D]
[00:43.78] [ch]Where the city[/ch=Em] [ch]sleeps[/ch=G][ch]and I'm the only one and I walk alone[/ch=Em]
[00:57.58] [ch]I walk alone,[/ch=Em] [ch]I walk alone[/ch=G][ch]I walk alone[/ch=D][ch]I walk alone and I walk a...[/ch=Em]
```
</details>

# Expect Adaptation By

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

# Other Lyric Formats
1. ID3 Specs - https://id3.org/Lyrics3v21. ID3 standardized SYNCEDLYRICS but not .lrc.
1. **OpenLyrics** - (https://github.com/openlyrics/openlyrics) - free-open XML standard. app / OS-independant song format for interoperability between apps

# License
- LRCv2 specs is free to use.
- Must give credit.

### Synced-Lyric Sources
1. https://github.com/tranxuanthang/lrclib
1. https://www.musixmatch.com/
1. https://www.rentanadviser.com
1. https://www.megalobiz.com/
1. https://www.lyricsify.com/

# Open for contribution.
