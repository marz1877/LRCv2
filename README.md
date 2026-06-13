# LRCv2 Specifications
LRCv2 XML-inspired format specification proposal draft with features - Synced Lyrics with Meaning, Translation, Singer metadata, Custom Styling, Chords, Karaeoke with Time and Pitch.

<img width="1774" height="887" alt="image" src="https://github.com/user-attachments/assets/168d0a32-3e1f-4bdd-8f55-45924f34180e" />

## Use Cases
1. Synced Lyrics
2. Meaning
3. Translation: For multilingual people, Language learning, foreign music listening.
4. Singer metadata: Kareoke
5. Custom Styling: Expressive lyrics.
6. Kareoke with Time and Pitch Data, Singing Learning Tool.
7. Chords: Music Learner.
8. Custom Images and Text: Music Learning Tool for Music Chords/Notation
9. Background Image/Video

### Why LRCv2 is needed
**LRCv1 lacks:**
1. Translation: LRCv1 Translation is a wordaround, only per line translation is possible not word or phase or paragraph
1. Meaning/annotations: Lyrics meaning usage is popular and needs a standardization.
1. Multiple singers
1. Reliable word-level timing
1. Styling

- Too much fragmentation in formats, all trying to achive the same thing and few differences in the features TTML, WebVTT, LRCv1-A2, YRC, QRC, KRC, LQE, LyricsFile.

### Automation
**All features for creating .lrc can be automated**
1. Lyrics
  - Speech-to-Text: https://github.com/openai/whisper
  - Synced Lyrics DB: MusixMatch
  - Lyrics Syncer: https://github.com/s9swata/ttml-parser (Input Audio+Lyrics Ouput:TTML using Groq Whisper), https://github.com/oseiskar/autosubsync , https://juanumusic.github.io/lyricssyncher/ , https://github.com/Alien501/lrc-generator , https://github.com/mikezzb/lyrics-sync ,
   - Lyrics Syncer (Line-by-Line): Service : https://lyricpotato.com/ , https://lyrisync.ovokacho.com/en
2. Translation:
  - DB: Musixmatch
  - Online: [Google Translate](https://translate.google.com)
  - Software: https://github.com/argosopentech/argos-translate , https://github.com/Spikatrix/Traly
3. Meaning: DB: Genius (https://github.com/johnwmillr/LyricsGenius) or LLM
4. Chords:
  - Software: Riffstation, https://ecoliving-tips.github.io/chord-finder.html, https://guitariz.studio/chord-ai, Chordify 
  - DB: UltimateGuitar
5. Karaoke:
  - Vocal Melody Isolation using (See below)
  - Covert it to MIDI using (See Below), for Karaoke Pitch matching.

- One LRCv2 file can have all features - Synced Lyrics + Meaning + Translation + Chords + Kareoke Data.

## Storing
**.lrc XML-inspired or in audio file's metadata**
- as sidecar file.
- Player to read filename with type speficied
- Can have seperate .lrc per usecase or all-in-one
*Suggested sidecar file naming*
```
AudioFilename.lrc              -
AudioFilename_translation.lrc  -  for seperate translation lrc
AudioFilename_meaning.lrc      -  for seperate meaning lrc
AudioFilename.chordpro         -  for chords
```
Benefit of sidecar is player can load what it supports.

### When inside audio use Metadata fields -
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

**Header**
```
[lrc version:2.0]
[language:en,es]
[features:meaning,translation,chords,color,textsize]
[encoding:UTF-8]
[id:musicbrainz-id]
[isrc:USWB19xxx589]
[BPM:123]
```

```metadata
Artist: `[ar:Song artist]`
Language: `[language:en,es,de]`
```

```EBNF
timestamp := "<mm:ss.xx>"
line := timestamp text "<br>"
section := "<c:name>"
```

- LRCv1 uses `[ti:Let's Twist Again]`, ChordPro uses Title `{title: You Are My Sunshine}`

# Example

<details>
  <summary>LRCv2 Full Song example - with meaning w/ hyperlink, per line sync</summary>
  
```
<c:Verse 1>
<soc>
<00:11.45><m>I walk a lonely road<br>
<00:14.09>The only one that I have ever known<br>
<00:17.25>Don't know where it goes<br>
<00:20.03>But it's home to me, and I walk alone<br></m:It’s possible these lines were inspired by the chorus of [Whitesnake’s ‘80s hit single “Here I Go Again”](https://en.wikipedia.org/wiki/Here_I_Go_Again):<br>
<br>Here I go again on my own<br>Going down the only road I’ve ever known<br>Like a drifter I was born to walk alone>
<00:27.93><m>I walk this empty street<br>
<00:31.68>On the Boulevard of Broken Dreams<br></m:The phrase “Boulevard of Broken Dreams” was first coined in a 1933 song recorded by many, from Bing Crosby to Amy Winehouse. It has since become a nickname for Los Angeles' Sunset Boulevard – it passes through Hollywood, so many have seen their stardom dreams die in the street.<br>
The title, “Boulevard of Broken Dreams”, is inspired by Gottfried Helnwein’s 1984 painting of the same name. This is a direct visual quotation of the painting “Nighthawks” by Edward Hopper that depicts a downtown diner at night. Helnwein replaced the diner’s occupants with American pop culture icons Humphrey Bogart, Marilyn Monroe, James Dean, and Elvis Presley to connect its bleak atmosphere with the tragic fate of some celebrities.<br>
This line also seems to draw inspiration from the the Motown 1966 Jimmy Ruffin’s classic “What Becomes of the Brokenhearted” where he sings<br>As I walk this land of broken dreams<br>There are many other similar lines in both this song and the one cited, which was written almost 40 years earlier.<br>Though the phrase “Boulevard of Broken Dreams” is used by various songwriters, the one most relevant to Green Day generally and this song specifically is probably Elvis Costello, in Brilliant Mistake:<br>He thought he was the king of America<br>But it was just a boulevard of broken dreams<br>The themes of the Costello song are quite similar to those in American Idiot.>
<00:33.77>Where the city sleeps<br>
<00:37.04>And I'm the only one, and I walk alone<br>
<eoc>

<c:Pre-Chorus>
<soc>
<00:41.37>I walk alone, I walk alone<br>
<00:45.15>I walk alone, and I walk a—<br>
<eoc>

<c:Chorus>
<soc>
<00:51.64><m>My shadow's the only one that walks beside me<br></m:When people walk, they often form shadows, which is a dark area or shape produced by a body coming between rays of light and a surface. It is relative to the amount of sunlight the Sun provides at a particular time and location, and as the Jesus of Suburbia is the only person in the area, his shadow is his only accompaniment.<br> Also for some reason Billie just doesn’t say “the” in this lyric, but “the” is more or less implied to be said.><br>My shallow heart's the only thing that's beatin'<br>
<01:03.46><m>Sometimes, I wish someone out there will find me<br>
<01:08.72>'Til then, I walk alone</m:This is a crucial aspect of the song and a look into Jesus of Suburbia’s mind. Lonely and depressed, he wants to seek comfort in a lover or friend. Instead of making an effort to find that person though, he takes a passive approach and gives into his isolating thoughts, hoping somebody else will stumble upon him. It’s an ineffective, kick the can down the road mindset that’s destined to fail.>
<eoc>

<c:Post-Chorus>
<soc>
<01:13.48>Ah-ah, ah-ah, ah-ah, ah-ah<br>
<01:20.44>Ah-ah, ah-ah, ah-ah<br>
<eoc>

<c:Verse 2>
<soc>
<01:25.28><m>I'm walkin' down the line<br>
<01:28.92>That divides me somewhere in my mind<br>
<01:28.92>On the borderline<br>
<01:28.92>Of the edge and where I walk alone<br></m:These lines take a step into Jesus of Suburbia’s mind. It shows his emotional problems and his troubled thoughts that have lingered with him since he left home. He’s troubled by all the wrong he’s done and meditates all his actions.<br>The line foreshadows Jesus of Suburbia’s Dissociative Identity Disorder where he eventually shares his mind with St. Jimmy.><br>
<01:39.91><m>Read between the lines<br>
<01:44.56>What's fucked up and everything's all right<br></m:He’s trying to decode his inner thoughts and work out which parts of him are still functioning properly.>
<01:48.66><m>Check my vital signs<br>
<01:51.95>To know I'm still alive, and I walk alone<br></m:During live performances, Billie Joe Armstrong often changes this lyrics asking the crowd:>
<eoc>

<c:Pre-Chorus>
<soc>
<01:55.71>I walk alone, I walk alone<br>
<02:03.08>I walk alone, and I walk a—<br>
<eoc>

<c:Chorus: Billie Joe Armstrong, Jason White>
<02:05.82>My shadow's the only one that walks beside me<br>
<02:11.30>My shallow heart's the only thing that's beatin'<br>
<02:17.94>Sometimes, I wish someone out there will find me<br>
<02:23.62>'Til then, I walk alone<br>

<c:Post-Chorus>
<soc>
<02:28.78>Ah-ah, ah-ah, ah-ah, ah-ah<br></02:27.78>
<02:35.09>Ah-ah, ah-ah<br>
<02:35.09>I walk alone, and I walk a—<br>
<eoc>

<c:Guitar Solo>

<c:Bridge>
<03:05.50>I walk this empty street<br>
<03:09.51>On the Boulevard of Broken Dreams<br>
<03:12.72>Where the city sleeps<br>
<03:14.93>And I'm the only one, and I walk a—<br>

<c:Chorus>
<soc>
<03:18.21>My shadow's the only one that walks beside me<br>
<03:23.89>My shallow heart's the only thing that's beatin'<br>
<03:29.56><m>Sometimes, I wish someone out there will find me<br>
<03:35.56>'Til then, I walk alone<br></m:This is a crucial aspect of the song and a look into Jesus of Suburbia’s mind. Lonely and depressed, he wants to seek comfort in a lover or friend. Instead of making an effort to find that person though, he takes a passive approach and gives into his isolating thoughts, hoping somebody else will stumble upon him. It’s an ineffective, kick the can down the road mindset that’s destined to fail.> </03:46.74>
<eoc>

<03:46.74><c:Instrumental Outro>
```
</details>

# Core Features

## 1.⏱️Time Stamping
- MAY use opening and closing time.
- MAY use Breakline `<br>` at the end of each line.

Brealine PROS:
- No CR `Carriage Return` and LF `Line Feed` issues.
- Consistent time metadata for line-by-line and word-by-word.

<details>
  <summary>Simplified Example</summary>

```
I walk a lonely road <Br>
The only one that I have ever known <Br>
```
</details>

### Other Synced Lyric Formats
- [Best Current] [TTML (Timed Text Markup Language)](https://www.w3.org/TR/2018/REC-ttml1-20181108/) [Word-by-Word, transliteration] https://github.com/amll-dev/amll-ttml-db/blob/main/instructions/ttml-specification-en.md .ttml Word-by-Word or Syllable-by-Syllable. Used by: Apple Music.
TTML supports word timing, translations, syling not meaning, chords.
- [LRCv1] [LRC's A2_extension:_word_time_tag](https://en.wikipedia.org/wiki/LRC_(file_format)#A2_extension:_word_time_tag) (Word-by-Word)
- (seems good) [Lyricify](https://github.com/WXRIW/Lyricify-App) https://amll.dev/en/guides/lyric/formats.html#lyricify-formats 
  - LYL	.lyl	Line-level	Lyricify	Lyricify's custom line-based format.
  - LYS	.lys	Word/syllable	Lyricify	Supports duet/background vocals and per-syllable timing.
  - [Good] LQE	.lqe	Word/syllable	Lyricify Quick Export	Container format that can bundle lyrics, translations, and pronunciations together.
- [Basic] WebVTT (used by YouTube for subtitle and lyrics)
- [Basic] ASS/SSA - https://www.quicklrc.com/subtitle-formats/ass
- [proprietary] KRC KuGou Music Word
- YRC- .yrc - Word-by-word	`NetEase Cloud Music`	Proprietary karaoke-style lyric format used by NetEase. proprietary
- QRC- .qrc - Word-by-word	`QQ Music`	Similar to YRC but with different syntax; sometimes distributed encrypted. proprietary
- [Subtitle oriented] TRC (Track Row Column) created by Motion Analysis Corporation.
- [Subtitle oriented] Universal Subtitle Format(https://en.wikipedia.org/wiki/Universal_Subtitle_Format)

- [Good but YAML is hard to work with and it doesn't support many features] **Lyrics File** (YAML based open format) - https://github.com/tranxuanthang/lrcget/releases/tag/2.0.0 Word-by-word lyric file format
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

They should switch to LRCv2 as every other format doesn't have all the features of LRCv2

#### Word-by-Word
**Use Case:** Karaeoke

### Format Word-by-Word

<details>
  <summary>LRCv2 Word-by-Word Full Song Example</summary>

```
<00:01.20>Yeah </00:01.54><00:02.54>yeah </00:02.96><00:03.96>yeah </00:04.40><00:05.37>yeah</00:05.75><br>
<00:06.05>Fever </00:06.35><00:06.35>dream </00:06.66><00:06.66>high </00:07.06><00:07.06>in </00:07.29><00:07.29>the </00:07.48><00:07.48>quiet </00:07.74><00:07.74>of </00:07.96><00:07.96>the </00:08.13><00:08.13>night</00:08.45><br>
<00:08.51>You </00:08.70><00:08.70>know </00:09.04><00:09.04>that </00:09.24><00:09.24>I </00:09.51><00:09.51>caught </00:09.72><00:09.72>it</00:09.95><br>
<00:09.95>Oh </00:10.12><00:10.12>yeah </00:10.38><00:10.38>you're </00:10.54><00:10.54>right </00:10.74><00:10.74>I </00:10.94><00:10.94>want </00:11.14><00:11.14>it</00:11.39><br>
<00:11.63>Bad </00:11.93><00:11.93>bad </00:12.30><00:12.30>boy </00:12.67><00:12.67>shiny </00:12.92><00:12.92>toy </00:13.34><00:13.34>with </00:13.65><00:13.65>a </00:13.86><00:13.86>price</00:14.18><br>
<00:14.18>You </00:14.41><00:14.41>know </00:14.70><00:14.70>that </00:14.90><00:14.90>I </00:15.15><00:15.15>bought </00:15.42><00:15.42>it</00:15.56><br>
<00:15.56>Oh </00:15.71><00:15.71>yeah </00:15.86><00:15.86>you're </00:16.03><00:16.03>right </00:16.29><00:16.29>I </00:16.51><00:16.51>want </00:16.67><00:16.67>it</00:16.84><br>
<00:16.84>Killing </00:17.00><00:17.00>me </00:17.24><00:17.24>slow </00:17.99><00:17.99>out </00:18.20><00:18.20>the </00:18.51><00:18.51>window</00:19.06><br>
<00:19.34>I'm </00:19.53><00:19.53>always </00:19.77><00:19.77>waiting </00:20.10><00:20.10>for </00:20.27><00:20.27>you </00:20.45><00:20.45>to </00:20.65><00:20.65>be </00:20.78><00:20.78>waiting </00:21.21><00:21.21>below</00:21.80><br>
<00:22.32>Devils </00:22.55><00:22.55>roll </00:22.73><00:22.73>the </00:22.92><00:22.92>dice </00:23.48><00:23.73>angels </00:23.93><00:23.93>roll </00:24.12><00:24.12>their </00:24.34><00:24.34>eyes</00:24.80><br>
<00:24.96>What </00:25.12><00:25.12>doesn't </00:25.46><00:25.46>kill </00:25.88><00:25.88>me </00:26.13><00:26.13>makes </00:26.33><00:26.33>me </00:26.53><00:26.53>want </00:26.74><00:26.74>you </00:27.02><00:27.02>more</00:27.49><br>
<00:28.05>And </00:28.27><00:28.27>it's </00:28.54><00:28.54>new </00:29.42><00:29.73>the </00:29.90><00:29.90>shape </00:30.15><00:30.15>of </00:30.37><00:30.37>your </00:30.70><00:30.70>body</00:31.11><br>
<00:31.11>It's </00:31.38><00:31.38>blue </00:32.22><00:32.53>the </00:32.71><00:32.71>feeling </00:33.13><00:33.13>I </00:33.46><00:33.46>got</00:33.78><br>
<00:33.78>And </00:33.98><00:33.98>it's </00:34.30><00:34.30>ooh </00:35.50><00:35.50>whoa </00:36.36><00:36.36>oh</00:36.77><br>
<00:36.87>It's </00:37.05><00:37.05>a </00:37.22><00:37.22>cruel </00:38.10><00:38.10>summer</00:39.52><br>
<00:39.71>It's </00:39.90><00:39.90>cool </00:40.80><00:41.11>that's </00:41.39><00:41.39>what </00:41.70><00:41.70>I </00:41.90><00:41.90>tell </00:42.25><00:42.25>'em</00:42.62><br>
<00:42.62>No </00:42.90><00:42.90>rules </00:43.65><00:43.89>in </00:44.08><00:44.08>breakable </00:44.71><00:44.71>heaven</00:45.17><br>
<00:45.17>But </00:45.48><00:45.48>ooh </00:46.74><00:46.74>whoa </00:47.08><00:47.08>oh</00:47.74><br>
<00:48.03>It's </00:48.20><00:48.20>a </00:48.37><00:48.37>cruel </00:49.42><00:49.42>summer</00:50.58><br>
<00:50.94>With </00:51.12><00:51.12>you</00:51.62><br>
<00:54.00>Hang </00:54.20><00:54.20>your </00:54.38><00:54.38>head </00:54.67><00:54.67>low </00:54.98><00:54.98>in </00:55.15><00:55.15>the </00:55.33><00:55.33>glow </00:55.62><00:55.62>of </00:55.84><00:55.84>the </00:56.06><00:56.06>vending </00:56.45><00:56.45>machine</00:57.12><br>
<00:57.13>I'm </00:57.32><00:57.32>not </00:57.53><00:57.53>dying</00:57.82><br>
<00:57.82>Oh </00:57.99><00:57.99>yeah </00:58.15><00:58.15>you're </00:58.30><00:58.30>right </00:58.57><00:58.57>I </00:58.81><00:58.81>want </00:59.06><00:59.06>it</00:59.43><br>
<00:59.43>We </00:59.65><00:59.65>say </00:59.82><00:59.82>that </01:00.02><01:00.02>we'll </01:00.29><01:00.29>just </01:00.65><01:00.65>screw </01:00.85><01:00.85>it </01:01.04><01:01.04>up </01:01.32><01:01.32>in </01:01.54><01:01.54>these </01:01.71><01:01.71>trying </01:02.20><01:02.20>times</01:02.60><br>
<01:02.60>We're </01:02.82><01:02.82>not </01:03.16><01:03.16>trying</01:03.56><br>
<01:03.56>Oh </01:03.71><01:03.71>yeah </01:03.93><01:03.93>you're </01:04.13><01:04.13>right </01:04.39><01:04.39>I </01:04.59><01:04.59>want </01:04.76><01:04.76>it</01:04.94><br>
<01:04.94>So </01:05.11><01:05.11>cut </01:05.27><01:05.27>the </01:05.43><01:05.43>headlights </01:05.76><01:05.98>summer's </01:06.23><01:06.23>a </01:06.63><01:06.63>knife</01:06.99><br>
<01:07.23>I'm </01:07.42><01:07.42>always </01:07.70><01:07.70>waiting </01:08.07><01:08.07>for </01:08.25><01:08.25>you </01:08.44><01:08.44>just </01:08.63><01:08.63>to </01:08.80><01:08.80>cut </01:09.04><01:09.04>to </01:09.22><01:09.22>the </01:09.38><01:09.38>bone</01:09.86><br>
<01:10.27>Devils </01:10.49><01:10.49>roll </01:10.69><01:10.69>the </01:10.91><01:10.91>dice </01:11.43><01:11.71>angels </01:11.98><01:11.98>roll </01:12.18><01:12.18>their </01:12.38><01:12.38>eyes</01:12.83><br>
<01:13.03>And </01:13.21><01:13.21>if </01:13.37><01:13.37>I </01:13.64><01:13.64>bleed </01:13.92><01:13.92>you'll </01:14.15><01:14.15>be </01:14.36><01:14.36>the </01:14.53><01:14.53>last </01:14.78><01:14.78>to </01:15.04><01:15.04>know</01:15.56><br>
<01:15.79>Oh </01:16.36><01:16.36>it's </01:16.56><01:16.56>new </01:17.51><01:17.76>the </01:17.94><01:17.94>shape </01:18.10><01:18.10>of </01:18.34><01:18.34>your </01:18.71><01:18.71>body</01:19.06><br>
<01:19.06>It's </01:19.38><01:19.38>blue </01:20.17><01:20.52>the </01:20.70><01:20.70>feeling </01:21.24><01:21.24>I </01:21.46><01:21.46>got</01:21.72><br>
<01:21.72>And </01:21.91><01:21.91>it's </01:22.15><01:22.15>ooh </01:23.47><01:23.47>whoa </01:23.80><01:23.80>oh</01:24.53><br>
<01:24.94>It's </01:25.11><01:25.11>a </01:25.29><01:25.29>cruel </01:26.18><01:26.18>summer</01:27.46><br>
<01:27.71>It's </01:27.90><01:27.90>cool </01:28.73><01:29.11>that's </01:29.40><01:29.40>what </01:29.75><01:29.75>I </01:29.95><01:29.95>tell </01:30.26><01:30.26>'em</01:30.46><br>
<01:30.46>No </01:30.66><01:30.66>rules </01:31.64><01:31.86>in </01:32.08><01:32.08>breakable </01:32.81><01:32.81>heaven</01:33.20><br>
<01:33.20>But </01:33.43><01:33.43>ooh </01:34.73><01:34.73>whoa </01:35.08><01:35.08>oh</01:35.89><br>
<01:36.20>It's </01:36.38><01:36.38>a </01:36.56><01:36.56>cruel </01:37.43><01:37.43>summer</01:38.81><br>
<01:38.81>With </01:39.03><01:39.03>you</01:39.50><br>
<01:39.52>I'm </01:39.77><01:39.77>drunk </01:40.11><01:40.11>in </01:40.30><01:40.30>the </01:40.50><01:40.50>back </01:40.83><01:40.83>of </01:41.02><01:41.02>the </01:41.20><01:41.20>car</01:41.50><br>
<01:41.77>And </01:41.95><01:41.95>I </01:42.11><01:42.11>cried </01:42.37><01:42.37>like </01:42.56><01:42.56>a </01:42.74><01:42.74>baby </01:43.12><01:43.12>coming </01:43.47><01:43.47>home </01:43.72><01:43.72>from </01:43.91><01:43.91>the </01:44.08><01:44.08>bar</01:44.35><br>
<01:44.60>Oh</01:45.03><br>
<01:45.03>Said </01:45.25><01:45.25>I'm </01:45.47><01:45.47>fine </01:45.77><01:45.77>but </01:45.97><01:45.97>it </01:46.17><01:46.17>wasn't </01:46.69><01:46.69>true</01:47.00><br>
<01:47.27>I </01:47.46><01:47.46>don't </01:47.72><01:47.72>want </01:47.90><01:47.90>to </01:48.01><01:48.01>keep </01:48.26><01:48.26>secrets </01:48.90><01:48.90>just </01:49.22><01:49.22>to </01:49.44><01:49.44>keep </01:49.73><01:49.73>you</01:50.17><br>
<01:50.19>And </01:50.38><01:50.38>I </01:50.72><01:50.72>snuck </01:51.08><01:51.08>in </01:51.47><01:51.47>through </01:51.73><01:51.73>the </01:51.92><01:51.92>garden </01:52.33><01:52.33>gate</01:52.85><br>
<01:52.85>Every </01:53.17><01:53.17>night </01:53.58><01:53.58>that </01:53.89><01:53.89>summer </01:54.34><01:54.34>just </01:54.57><01:54.57>to </01:54.75><01:54.75>seal </01:55.01><01:55.01>my </01:55.26><01:55.26>fate</01:55.68><br>
<01:55.68>Oh</01:56.17><br>
<01:56.17>And </01:56.49><01:56.49>I </01:56.77><01:56.77>scream </01:57.18><01:57.18>for </01:57.35><01:57.35>whatever </01:57.91><01:57.91>it's </01:58.11><01:58.11>worth</01:58.48><br>
<01:58.78>"</01:58.96><01:58.96>I </01:59.12><01:59.12>love </01:59.30><01:59.30>you" </01:59.65><01:59.65>ain't </01:59.94><01:59.94>that </02:00.17><02:00.17>the </02:00.35><02:00.35>worst </02:00.63><02:00.63>thing </02:01.03><02:01.03>you </02:01.25><02:01.25>ever </02:01.55><02:01.55>heard</02:01.91><br>
<02:02.25>He </02:02.45><02:02.45>looks </02:02.78><02:02.78>up </02:03.08><02:03.08>grinning </02:03.49><02:03.49>like </02:03.78><02:03.78>a </02:03.98><02:03.98>devil</02:04.22><br>
<02:04.22>It's </02:04.48><02:04.48>new </02:05.36><02:05.72>the </02:05.89><02:05.89>shape </02:06.17><02:06.17>of </02:06.42><02:06.42>your </02:06.72><02:06.72>body</02:06.99><br>
<02:06.99>It's </02:07.36><02:07.36>blue </02:08.08><02:08.43>the </02:08.62><02:08.62>feeling </02:09.28><02:09.28>I </02:09.52><02:09.52>got</02:09.71><br>
<02:09.71>And </02:09.92><02:09.92>it's </02:10.24><02:10.24>ooh </02:11.07><02:11.07>whoa </02:11.86><02:11.86>oh</02:12.54><br>
<02:12.84>It's </02:13.01><02:13.01>a </02:13.18><02:13.18>cruel </02:14.09><02:14.09>summer</02:15.36><br>
<02:15.68>It's </02:15.86><02:15.86>cool </02:16.79><02:17.17>that's </02:17.42><02:17.42>what </02:17.73><02:17.73>I </02:17.93><02:17.93>tell </02:18.23><02:18.23>'em</02:18.44><br>
<02:18.44>No </02:18.65><02:18.65>rules </02:19.64><02:19.88>in </02:20.07><02:20.07>breakable </02:20.72><02:20.72>heaven</02:21.20><br>
<02:21.20>But </02:21.40><02:21.40>ooh </02:22.65><02:22.65>whoa </02:23.21><02:23.21>oh</02:23.91><br>
<02:24.06>It's </02:24.26><02:24.26>a </02:24.43><02:24.43>cruel </02:25.42><02:25.42>summer</02:26.81><br>
<02:27.03>With </02:27.20><02:27.20>you</02:27.62><br>
<02:27.77>I'm </02:27.96><02:27.96>drunk </02:28.22><02:28.22>in </02:28.46><02:28.46>the </02:28.64><02:28.64>back </02:28.91><02:28.91>of </02:29.11><02:29.11>the </02:29.27><02:29.27>car</02:29.60><br>
<02:29.64>And </02:29.80><02:29.80>I </02:29.97><02:29.97>cried </02:30.30><02:30.30>like </02:30.48><02:30.48>a </02:30.66><02:30.66>baby </02:30.97><02:30.97>coming </02:31.34><02:31.34>home </02:31.61><02:31.61>from </02:31.78><02:31.78>the </02:31.98><02:31.98>bar</02:32.40><br>
<02:32.40>Oh</02:33.01><br>
<02:33.01>Said </02:33.21><02:33.21>I'm </02:33.42><02:33.42>fine </02:33.79><02:33.79>but </02:34.01><02:34.01>it </02:34.22><02:34.22>wasn't </02:34.72><02:34.72>true</02:35.08><br>
<02:35.29>I </02:35.50><02:35.50>don't </02:35.69><02:35.69>wanna </02:35.98><02:35.98>keep </02:36.25><02:36.25>secrets </02:36.92><02:36.92>just </02:37.19><02:37.19>to </02:37.45><02:37.45>keep </02:37.73><02:37.73>you</02:38.10><br>
<02:38.10>And </02:38.31><02:38.31>I </02:38.68><02:38.68>snuck </02:39.08><02:39.08>in </02:39.44><02:39.44>through </02:39.75><02:39.75>the </02:40.05><02:40.05>garden </02:40.31><02:40.31>gate</02:40.81><br>
<02:40.81>Every </02:41.07><02:41.07>night </02:41.54><02:41.54>that </02:41.88><02:41.88>summer </02:42.34><02:42.34>just </02:42.59><02:42.59>to </02:42.76><02:42.76>seal </02:42.99><02:42.99>my </02:43.25><02:43.25>fate</02:43.65><br>
<02:43.65>Oh</02:44.25><br>
<02:44.25>And </02:44.48><02:44.48>I </02:44.75><02:44.75>scream </02:45.10><02:45.10>for </02:45.34><02:45.34>whatever </02:45.87><02:45.87>it's </02:46.07><02:46.07>worth</02:46.67><br>
<02:46.80>"</02:46.96><02:46.96>I </02:47.16><02:47.16>love </02:47.31><02:47.31>you" </02:47.59><02:47.59>ain't </02:47.83><02:47.83>that </02:48.09><02:48.09>the </02:48.28><02:48.28>worst </02:48.64><02:48.64>thing </02:48.96><02:48.96>you </02:49.22><02:49.22>ever </02:49.51><02:49.51>heard</02:49.91><br>
<02:50.69>Yeah </02:50.98><02:52.01>yeah </02:52.27><02:53.42>yeah </02:53.73><02:54.78>yeah</02:55.31><br>
```
</details>

<details>
  <summary>LRCv2 Word-by-Word Format Example</summary>

```
<00:11.45>I <00:11.89>walk <00:12.33>a <00:12.77>lone-<00:13.43>ly <00:13.75>road</00:14.09><bBr>
<00:14.09>The <00:14.48>on- <00:14.87>ly <00:15.26>one <00:15.65>that <00:16.05>I <00:16.44>have <00:16.83>ev-<00:17.04>er <00:17.25>known </00:17.25><br>
<00:17.25>Don't <00:17.95>know <00:18.64>where <00:19.34>it <00:19.69>goes </00:20.03><br>
<00:20.03>But <00:20.73>it's <00:21.43>home <00:22.12>to <00:22.82>me <00:23.52>and <00:24.21>I <00:24.91>walk <00:25.61> a-<00:26.31>lone</00:27.93><br>

<00:27.93>I <00:28.55>walk <00:29.18>this <00:29.80>emp- <00:30.42>ty <00:31.05>street </00:31.68><br>
<00:31.68>On <00:32.03>the <00:32.38>Bou- <00:32.73>le- <00:33.08>vard <00:33.42>of <00:33.77>Bro-<00:34.12>ken <00:34.47>Dreams </00:35.00><br>
<00:33.77>Where <00:34.59>the <00:35.40>ci- <00:36.22>ty <00:36.63>sleeps </00:37.04><br>
<00:37.04>And <00:37.58>I'm <00:38.12>the <00:38.66>on- <00:39.20>ly <00:39.74>one <00:40.28>and <00:40.82>I <00:41.10>walk <00:41.37>a-lone </00:41.37><br>

<00:41.37>I <00:41.84>walk <00:42.31>a-lone <00:43.26>I <00:43.73>walk <00:44.20>a-lone </00:45.15><br>
<00:45.15>I <00:45.80>walk <00:46.45>a-lone <00:47.75>I <00:48.40>walk <00:49.05>a- </00:51.64><br>
```
</details>

## Syllable-by-Syllable

**Use Case:** kareoke or rap lyrics

<details>
  <summary>Syllable-by-Syllable Format Example</summary>
  
```
<00:11.45> I <00:11.89> walk <00:12.33> a <00:12.77> lone- <00:13.43> ly <00:13.75> road </00:14.09> <br>
<00:14.09> The <00:14.48> on- <00:14.87> ly <00:15.26> one <00:15.65> that <00:16.05> I <00:16.44> have <00:16.83> ev- <00:17.04> er <00:17.25> known </00:17.25> <br>
<00:17.25> Don't <00:17.95> know <00:18.64> where <00:19.34> it <00:19.69> goes </00:20.03> <br>
<00:20.03> But <00:20.73> it's <00:21.43> home <00:22.12> to <00:22.82> me <00:23.52> and <00:24.21> I <00:24.91> walk <00:25.61> a- <00:26.31> lone </00:27.93> <br>

<00:27.93> I <00:28.55> walk <00:29.18> this <00:29.80> emp- <00:30.42> ty <00:31.05> street </00:31.68> <br>
<00:31.68> On <00:32.03> the <00:32.38> Bou- <00:32.73> le- <00:33.08> vard <00:33.42> of <00:33.77> Bro- <00:34.12> ken <00:34.47> Dreams </00:35.00> <br>
<00:33.77> Where <00:34.59> the <00:35.40> ci- <00:36.22> ty <00:36.63> sleeps </00:37.04> <br>
<00:37.04> And <00:37.58> I'm <00:38.12> the <00:38.66> on- <00:39.20> ly <00:39.74> one <00:40.28> and <00:40.82> I <00:41.10> walk <00:41.37> a-lone </00:41.37> <br>

<00:41.37> I <00:41.84> walk <00:42.31> a-lone <00:43.26> I <00:43.73> walk <00:44.20> a-lone </00:45.15> <br>
<00:45.15> I <00:45.80> walk <00:46.45> a-lone <00:47.75> I <00:48.40> walk <00:49.05> a- </00:51.64> <br>
```
</details>

# 2. Multi Singers

Format: `<0:00.00> <s:Singer1,Singer2>Words</s:Singer1>`


<details>
  <summary>Full Song Example</summary>
  
```
<c:Verse 1: Harry, Liam>
<soc>
<00:00.00> <s:Harry>Written in these walls are the stories that I can't explain</s:Harry>
<00:04.50> <s:Harry>I leave my heart open, but it stays right here empty for days</s:Liam>
<00:09.00> <s:Liam>She told me in the mornin' she don't feel the same about us in her bones</s:Liam>
<00:13.50> <s:Liam>It seems to me that when I die, these words will be written on my stone</s:Liam>
<eoc>

<c:Pre-Chorus: Zayn>
<soc>
<00:18.00> <s:Zayn>And I'll be gone, gone tonight</s:Zayn>
<00:18.00> <s:All>Oh Oh Oh<00:20.00></s:All>
<00:21.50> <s:Zayn>The ground beneath my feet is open wide</s:Zayn>
<00:25.00> <s:Zayn>The way that I've been holding on too tight</s:Zayn>
<00:29.00> <s:Zayn>With nothing in between</s:Zayn>
<eoc>

<c:Chorus: Harry, All>
<soc>
<00:32.00> <s:Harry,All>The story of my life, I take her home</s:Harry,All>
<00:35.50> <s:Harry,All>I drive all night to keep her warm</s:Harry,All>
<00:39.00> <s:Harry,All>And time is frozen (The story of, the story of)</s:Harry,All>
<00:43.00> <s:Harry,All>The story of my life, I give her hope</s:Harry,All>
<00:46.50> <s:Harry,All>I spend her love until she's broke inside</s:Harry,All>
<00:50.00> <s:Harry,All>The story of my life (The story of, the story of)</s:Harry,All>
<eoc>

<c:Verse 2: Niall, Liam>
<soc>
<00:54.00> <s:Niall,Liam>Written on these walls are the colors that I can't change</s:Niall,Liam>
<00:58.50> <s:Niall,Liam>Leave my heart open, but it stays right here in its cage</s:Niall,Liam>
<01:03.00> <s:Niall,Liam>I know that in the mornin', I'll see us in the light up on the hill</s:Niall,Liam>
<01:07.50> <s:Niall,Liam>Although I am broken, my heart is untamed still</s:Niall,Liam>
<eoc>

<c:Pre-Chorus: Louis>
<soc>
<01:12.00> <s:Louis>And I'll be gone, gone tonight</s:Louis>
<01:15.50> <s:Louis>The fire beneath my feet is burning bright</s:Louis>
<01:19.00> <s:Louis>The way that I've been holding on so tight</s:Louis>
<01:23.00> <s:Louis>With nothing in between</s:Louis>
<eoc>

<c:Chorus: Harry, All>
<soc>
<01:26.00> <s:Harry,All>The story of my life, I take her home</s:Harry,All>
<01:29.50> <s:Harry,All>I drive all night to keep her warm</s:Harry,All>
<01:33.00> <s:Harry,All>And time is frozen (The story of, the story of)</s:Harry,All>
<01:37.00> <s:Harry,All>The story of my life, I give her hope</s:Harry,All>
<01:40.50> <s:Harry,All>I spend her love until she's broke inside</s:Harry,All>
<01:44.00> <s:Harry,All>The story of my life (The story of, the story of)</s:Harry,All>
<eoc>

<c:Bridge: Zayn>
<soc>
<01:48.00> <s:Zayn>And I've been waiting for this time to come around</s:Zayn>
<01:52.00> <s:Zayn>But baby, running after you is like chasin' the clouds</s:Zayn>
<eoc>

<c:Breakdown: Niall>
<soc>
<01:56.00> <s:Niall>The story of my life, I take her home</s:Niall>
<02:00.00> <s:Niall>I drive all night to keep her warm</s:Niall>
<02:04.00> <s:Niall>And time is frozen</s:Niall>
<eoc>

<c:Chorus: All, Zayn>
<soc>
<02:08.00> <s:All,Zayn>The story of my life, I give her hope (I give her hope)</s:All,Zayn>
<02:12.00> <s:All,Zayn>I spend her love until she's broke inside (Till she's broke inside)</s:All,Zayn>
<02:16.00> <s:All,Zayn>The story of my life (The story of, the story of)</s:All,Zayn>
<eoc>

<c:Outro: All, Harry>
<soc>
<02:20.00> <s:All,Harry>The story of my life</s:All,Harry>
<02:24.00> <s:All,Harry>The story of my life (The story of)</s:All,Harry>
<02:28.00> <s:All,Harry>(The story of, the story of)</s:All,Harry>
<02:32.00> <s:All,Harry>The story of my life</s:All,Harry>
<eoc>
```
</details>

<details>
  <summary>Format Example</summary>

  ```
<00:12.00> <s:Jhon>Line 1 lyrics</s:Jhon><Br>
<00:16.00> <s:Luis>Line 2 lyrics</s:Luis><Br>
<01:01.00> <s:William,Luis>Line 3 lyrics</s:William,Luis><Br>
```
</details>

#### Also See - other formats with similar objective -
- Extended LRC - (Wikipedia removed it) https://en.wikipedia.org/wiki/LRC_(file_format)#Simple_format_extended [Multiple singer]
- Walaoke_extension:_gender - https://en.wikipedia.org/wiki/LRC_(file_format)#Walaoke_extension:_gender [Singer Gender]

## 2.1 Per Section

- LRCv2 recommends `<>` for everything `<c:Verse 1>`
- If Entire Section is sung by 1 singer then `<c:Verse 1: Vocalist Name>`
- Mark start of section with `<soc>` and end of section with `<eoc>`.

Note: LRCv1 uses for `{c:Verse 1}`

Genius Example - https://genius.com/Krewella-crying-on-the-dancefloor-lyrics (Genius has multi-singer infomation).

```
<c:Verse 1: Vocalist Name>
<00:24.94> Lyrics
```

## 3. Meaning

- Recommended Lyric meaning database: Genius

Format`<m>Lyrics</m:Meaning>`

## Contextual
**by Paragrah/line/word**

FORMAT: See Main Example

## Hyperlink inside Meaning
- Meaning CAN contain hyperlinks.

FORMAT: See Main Example

## 3.2 Language Translation - Per Word,Phrase, Line

### Word-by-Word
- Player MAY include dictionary for per word/phrase/slang/idiom translation.

### Line(s)

FORMAT: See Main Example

LRCv1 uses `[xx:xx.xx]` LRCv2 uses `<xx:xx.xx>` with `<br>` at end of lines

### Translation Format
- MUST specify translation lanuages. e.g. German to English is `deu:eng`.
- MUST use ISO 639-3 language codes.
- One lyric CAN multiple translations.
- Format `<00:13.75> <T:lang1:lang2>Line</T:TransaltedText>`
- MAY contain 'Literal' and 'Common Usage' meaning.
<details>
  <summary>Example with Literal and Commonusage </summary>
  
```
<00:13.75> <t:fin:eng>Yöllä taas mä menin parvekkeelle nukkumaan,</t:Literal=At night again I went to sleep in the balcony.CommonUsage=where's my baby?>
<00:19.62> <t:fin:eng>Jotta lähempänä mua ois hän</t:So that they would be closer to me>
<00:25.30> <t:fin:eng>Pediltäni taivas näkyy, ryhdyin oottamaan,</t:From my bed I saw the sky, begun to wait>
<00:57.81> Tuuli tuule sinne <T:fin:eng]missä muruseni on</T:Where my loved ones are, CommonUsage: where's my baby?>
```
</details>

Other Trnslated Lyrics Format: Syntax and UI
<details>
  <summary>Current LRCv1 workaround Syntax and UI - with per-line translation and both laguages in sepearte lines with same time stamp</summary>

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

# Suggested UI for Translation and Meaning Feature

### Big Screen
![ui](https://user-images.githubusercontent.com/105455604/168247326-d772633e-c073-4928-9400-ada37fa4817d.png)

- In meaning mode: hovering should show line, phrase or paragraph hilighted depening on context (explaination for only lines or paragraph is sufficient, words may be used rarely) 
- In translation mode: hovering over should hilight phrases (as small as possible) giving meaning of the phrase and words used targeted for langauge learning.

# Censoring Words

- Players MAY have option to censor explicit words eg. F**k and S**t or completely ****.
- Explicit Dictionary - https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words

# Extended Features

# 4. Styling

## 4.1 Custom Text Color (for expression)

# Format
```
[02:16.00] [cr=#dc143c]Destroy yourself, see who gives a[/cr] [cr=#420612]duck[/cr]
[02:18.00] See who gives a duck
```

## 4.2 Custom Text Size (for word expression)
- MAY turn off when using slidding lyrics depending of screen types. e.g. phone with scrolling lyrics size can be hard to dynamicly resize.

### Format
<details>
  <summary>ClickMe</summary>
```
[02:16.00] [sz=10]Destroy yourself, see who gives a[/sz] [sz=20]duck[/sz]
[02:18.00] See who gives a duck
```
</details>

# 5. Karaeoke (LRCv2-K)
**Voice melody MIDI + Mic Input w/ Pitch-Recognition on MIDI-piano-roll**

- May include meatdata `[midioffset:00:00.00]`
- Optional: Players MAY support this feature but explicity tell when not suported.

## 1. Voice melody MIDI

#### TORING:
- MAYBE used as sidecar file for audio file with LRCv2.

#### CREATION/AUTOMATION:
- Extract Steam (realtime or pre-make) - https://github.com/nomadkaraoke/python-audio-separator, https://github.com/facebookresearch/demucs , https://hub.docker.com/r/aclmb/stemgen, https://github.com/anjok07/ultimatevocalremovergui .
- Audio to MIDI - https://gist.github.com/natowi/d26c7e97443ec97e8032fb7e7596f0b0, https://github.com/DamRsn/NeuralNote, https://github.com/spotify/basic-pitch, https://sourceforge.net/projects/a2m/

#### Recommended Tools- Audio-to-Midi Convertion:
 - https://www.sonicvisualiser.org/tony/ , https://github.com/sonic-visualiser/tony
 - https://github.com/spotify/basic-pitch - Audio-to-Midi   
 - https://github.com/DamRsn/NeuralNote .

## 2. Player MUST show midi-piano-roll to work as a karaeoke or Singing Learing Tool.

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

# 6. Chords
- Optional
- Player MAY add options to -
  - Show Chord Charts for many instruments
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


### LRCv2 Chord+Lyrics Format

Format `<ch>Lyric </ch:Em>`

<details>
  <summary>LRCv2 Chord+Lyrics</summary>  
 
```
<00:22.37> <ch>I walk a </ch:Em><ch>lonely road, </ch:G>the <ch>only one that </ch=D><ch>I have ever known</ch:Em> <br>
<00:29.45> <ch>Don't know where it </ch:G><ch>goes,</ch:Em> <ch>but it's home to me </ch=G><ch>and I walk alone</ch:Em> <br>
<00:36.72> <ch>I walk this empty</ch:Em> <ch>street</ch:G><ch>On the Boulevard of Broken Dreams</ch:D> <br>
<00:43.78> <ch>Where the city</ch:Em> <ch>sleeps</ch:G><ch>and I'm the only one and I walk alone</ch:Em> <br>
<00:57.58> <ch>I walk alone,</ch:Em> <ch>I walk alone</ch:G.<ch>I walk alone</ch:D><ch>I walk alone and I walk a...</ch:Em> <br>
```
</details>

### LRCv2 Chord+Lyrics (Chords Seperately) Format Type 2

Use a seperate Chord file with time stamps without lyrics. Which helps with song has many instrumental breaks.

<details>
  <summary>LRCv2 Format</summary>  
 
```
<00:22.37=Em> Word Word</00:00.00> <00:22.37=G>Word Word </00:22.37 <00:22.37=D>Word WordWord Word </00:22.37> <00:22.37=A> Word Word</00:22.37><Br>
```
</details>

# Special Features

# 7. Custom Images and Text
- Optional
- MUST NOT Show lyrics and `Custom Images and Text` together.
- custom text usecase guitar/bass/drums tabs or Music notation.
- Custom Images Along with with Lyrics.

This would need a .7z zip with all the custom data

Format
```
<00:00.00>File Name</00:00.00>
```
# 8. Background Image/Video
- Optional
- MAY load background images/video in zip file
- Player MUST not play audio from the video

Format: `<bi=filename.ext>lyrics</bi=filename.ext>`

## Other Recommendations
- Player MAY have option to mute or turn down instruments using steam seperation.

## Expect Adaptation By

**Music Streaming Services**
1. [Spotify](https://open.spotify.com/)
2. [YouTUbeMusic](https://music.youtube.com/)
1. ‎[Apple Music](https://music.apple.com/)
1. [Tencent Music](https://www.tencentmusic.com/en-us/)
1. [Amazon Music](https://music.amazon.com)

1. [UltimateGuitar](https://www.ultimate-guitar.com/) (Lyrics+Chords)

**Lyrics Services**
1. [MusixMatch](https://www.musixmatch.com/) (Synced Lyrics)
1. [Genius](https://genius.com/) (Lyrics Meaning)

**Music Player Apps Desktop**
1. Foobar2000: [OpenLyrics lyrics component](https://github.com/jacquesh/foo_openlyrics)
2. https://roon.app/en/
3. https://jriver.com/
4. https://audirvana.com/
5. https://www.plex.tv/plexamp/
6. https://github.com/digimezzo/dopamine
7. https://www.mediamonkey.com/
8. https://deadbeef.sourceforge.io/
9. https://gitlab.gnome.org/GNOME/rhythmbox
10. https://aimp.ru/
11. https://aurisplayer.com/
12. https://getmusicbee.com/

**Stream Server**
1. https://github.com/navidrome/navidrome

**Android Players**
1. https://github.com/MetrolistGroup/Metrolist
2. https://github.com/mardous/BoomingMusic
3. https://powerampapp.com/
4. https://symfonium.app/
5. https://github.com/Moriafly/SaltPlayerSource (Android - Car Features, Windows, HarmonyOS)

**Karaeoke**
1. https://github.com/DoubleDee73/Yass-Reloaded
1. https://db.openkj.org/
1. https://github.com/UltraStar-Deluxe/USDX
1. https://github.com/gyunaev/spivak

**Lyrics Player/Editor**
1. https://github.com/tranxuanthang/lrcget1. 
1. https://github.com/Spikatrix/LRC-Editor
1. https://lrc-maker.github.io/
1. https://github.com/lemutec/LyricStudio
1. Cross-platform advanced subtitle editor - https://github.com/Aegisub/Aegisub
1. https://github.com/WXRIW/Lyricify-App

**Audio Codec/Metadata**
1. [Xiph.Org Foundation](https://xiph.org/)
2. [FFmpeg](https://ffmpeg.org/)

**Synced-Lyric Sources**
1. https://github.com/tranxuanthang/lrclib (Open Source DB)
1. https://www.musixmatch.com/ (Word-by-Word and Line-by-line)
1. https://www.rentanadviser.com
1. https://www.megalobiz.com/
1. https://www.lyricsify.com/

**Translated Lyrics DB:**
1. https://lyricstranslate.com/ eg. https://lyricstranslate.com/en/missae-muruseni-where-my-sweetheart.html-0
1. https://www.musixmatch.com/ eg. https://www.musixmatch.com/lyrics/Jenni-Vartiainen/Miss%C3%A4-muruseni-on/translation/english

#### Other Lyric Formats
1. ID3 SYNCEDLYRICS - https://id3.org/Lyrics3v21. ID3 standardized SYNCEDLYRICS but not .lrc.
1. **OpenLyrics** - (https://github.com/openlyrics/openlyrics) - free-open XML standard. app / OS-independant song format for interoperability between apps
**Music Notation**
1. [Music_notation_file_formats](https://en.wikipedia.org/wiki/Category:Music_notation_file_formats)
1. .mscz/.mscx - https://musescore.org/en/handbook/3/file-formats#mscz
1. .mxl (Music XML) - https://handbook.musescore.org/file-management/working-with-musicxml-files

## Software
- LRCv2 needs WYSIWYG editor specially when using many features at once.
- Something like https://github.com/Royce551/FRESHLyricMaker.
- For Kareoke fork https://github.com/UltraStar-Deluxe/USDX/.

## License
- LRCv2 specs is free to use.

#### GUI Tool to Manually Per Word Sync:
  - https://github.com/pxeemo/LySy
  - https://github.com/better-lyrics/composer (does steam seperation using HTDemucs)
  - https://github.com/streetlegithub/amll-ttml-tool-english
  - https://github.com/amll-dev/applemusic-like-lyrics
    - https://github.com/Raqhael-ux/Voxen-LRC-Editor

#### Other Tools
  - https://github.com/eepyyyy/enhanced-lrc (TTML to ELRC)

## Open for contribution.
