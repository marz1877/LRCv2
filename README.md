# LRCv2
Open for contribution. ID3 standardized SYNCEDLYRICS but not .lrc.make it standard.

1. Will need a WYSIWYG editor if using every feature.
2. File Extension - .lrc, .music, or add it to metadata.
3. Purpose - lyrics, kareoke with time and pitch, Chords, meaning, translation.

### Automation
All features for creating .lrc can be automated except Meaning.

1. Get Lyrics from Internet sources like Genius or Speech-to-Text/Speech Recognition (https://github.com/openai/whisper).
2. Synced Lyrics can be retrived or time lyrics using https://github.com/oseiskar/autosubsync.
3. Chords can be automated (using software like Riffstation) or retrived from database like ultimateguitar.
4. Vocal Melody can be Isolate automatedlly using (See below) and covert it to MIDI using (See Below).
5. Translation can be retrived from Musixmatch or Google Translate or Offline using https://github.com/argosopentech/argos-translate.

## Player to read filename with type speficied

If a audio file is played and there is a .lrc in the same directory or it is specefied in player the .lrc can be named -
```
sameasaudiofilename.lrc
sameasaudiofilename_translation.lrc    for seperate translation lrc
sameasaudiofilename_meaning.lrc        for seperate meaning lrc
sameasaudiofilename.chordpro           for chordpro
```

1 file can have all 3 meaning, translation, chords

## 1.1 Metadata - .lrc version info

Format 

```
[lrc version:2]
```
## 1.2 Metadata - Language   

like "[ar:Lyrics artist]"

### Format

```
[language:Languages in the lyrics]
```
```
example [language:en,es,de]
```

## 2. Singers - Song with multiple singers

### Also See these previous standard achive similar objective but there not adapted -

Extended LRC - (Wikipedia removed it) https://en.wikipedia.org/wiki/LRC_(file_format)#Simple_format_extended
Walaoke_extension:_gender - https://en.wikipedia.org/wiki/LRC_(file_format)#Walaoke_extension:_gender

### Format

```
[00:12.00] [Singer:Jhon]Line 1 lyrics[/Singer:Jhon]
[00:16.00] [Singer:Luis]Line 2 lyrics[/Singer:Luis]
[1:01.00] [Singer:William,Luis]Line 3 lyrics [/Singer:William,Luis]
```

## 3.1 Meaning Contextual - by word/line

Genius is the only online database with lyric meaning

### Format

```
[00:00.00] [Meaning] I walk a lonely road [/Meaning: The singer is feeling lonely and isolated, and is on a path that no one else is traveling with him. He may feel like he doesn't fit in with others and is struggling to find his place in the world.]
[00:15.67] [Meaning] Don't know where it goes [/Meaning: The singer is uncertain of where the path will take him, and is unsure of what the future holds.]
[00:28.03] [Meaning] My shadow's the only one that walks beside me [/Meaning: The singer feels alone and abandoned, as represented by his shadow being the only companion on his journey.]
[00:42.25] [Meaning] I walk this empty street [/Meaning: The singer is walking down a street that feels barren and lifeless, emphasizing his feelings of loneliness and isolation.]
[00:53.04] [Meaning] On the boulevard of broken dreams [/Meaning: The "boulevard of broken dreams" is a metaphor for a place where people go to give up on their hopes and aspirations, and the singer feels like he is a part of this world of lost dreams and broken promises.]
```
## 3.2 Language Translation - Per Line, Phrase, Word

Client (Player) can have a dictionary for per word/phrase/slang/idiom translation.

Translation right now - https://www.musixmatch.com/lyrics/Jenni-Vartiainen/Miss%C3%A4-muruseni-on/translation/english
https://lyricstranslate.com/en/missae-muruseni-where-my-sweetheart.html-0

### Format

```
[00:13.75] [Translation,fin>eng]Yöllä taas mä menin parvekkeelle nukkumaan,[/Translation: Literal:At night again I went to sleep in the balcony], CommonUsage: where's my baby?]
[00:19.62] [Translation,fin>eng]Jotta lähempänä mua ois hän[/Translation: Literal:So that they would be closer to me]
[00:25.30] [Translation,fin>eng]Pediltäni taivas näkyy, ryhdyin oottamaan,[/Translation: Literal:From my bed I saw the sky, begun to wait]
[00:57.81] Tuuli tuule sinne [Translation,fin>eng]missä muruseni on[/Translation: Literal:Where my loved ones are, CommonUsage: where's my baby?]
```
Current Forat with per line translation and both laguages in sepearte lines with same time stamp -

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

### 3.3 Contexual Language Translation - per Word/Phrase

specify translation lanuages for German to English like `de>en`
file can have multiple translations

Dictionary in the player may not be useful as word can be contexual and as used in gerneral/other cases.

### Format

```
[00:00.00] [WordMeanind,de>en]Überheblich[/WordMeanind:Arrogant], [WordMeanind]überlegen[/WordMeanind:consider]
```

## 4. Suggested UI for Translation and Meaning Feature

![ui](https://user-images.githubusercontent.com/105455604/168247326-d772633e-c073-4928-9400-ada37fa4817d.png)

When meaning mode from the top button is selected hovering over will show line, phrase or paragraph hilighted depening on context (when explaing song lyrics only one line or paragraph is sufficient) 

When translation mode is selected hovering over will hilight phrases (as small as possible) giving meaning of the phrase and words used trageted for langauge learning.

## 5. Custom Text Color (for expression)

### Format

```
[02:16.00] [cr=#dc143c]Destroy yourself, see who gives a[/cr] [cr=#420612]duck[/cr]
[02:18.00] See who gives a duck
```
## 6. Custom Text Size (for expression)

This can be turned off when using slidding lyrics depending of screen types. For example on phone with scrooling lyrics size can be hard to do.

### Format

```
[02:16.00] [sz=10]Destroy yourself, see who gives a[/sz] [sz=20]duck[/sz]
[02:18.00] See who gives a duck
```
## 7. Censoring Words

Add option to convert words like fuck, shit to F**k and S**t using Dictionary - https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words

## 8. Karaeoke - Voice melody's MIDI and Mic INput using pitch recognision and midi roll

1. Voice melody's midi can be supplied with audio files or extracted realtime using -
 - https://hub.docker.com/r/aclmb/stemgen steam seperator
 - https://github.com/spotify/basic-pitch audio-to-Midi
1. the player can show midi roll and take mic input to work as a kareoke that can also work as a sining learing method
1. Convert Audio-to-Midi using-
 - https://www.sonicvisualiser.org/tony/
 - https://github.com/DamRsn/NeuralNote.

![image](https://user-images.githubusercontent.com/105455604/168251330-d98a8d35-936d-44b7-9988-b86f71f4a67c.png)

It is "not similar" to https://en.wikipedia.org/wiki/CD%2BG / https://en.wikipedia.org/wiki/MP3%2BG

## 9. Lyrics+Chords in ChordPro Fomat

ChordPro - https://github.com/ChordPro/chordpro, https://www.chordpro.org/

Client may have ablity to transpose scale, have "no capo version", or show chord progression eg. `II V IV`

#### Old Proposed Format (use ChordPro instead)
```
[00:22.37] [cr]I walk a [/cr=Em][cr]lonely road, [/cr=G]the [cr]only one that [/cr=D][cr]I have ever known[/cr=Em]
[00:29.45] [cr]Don't know where it [/cr=G][cr]goes,[/cr=Em] [cr]but it's home to me [/cr=G][cr]and I walk alone[/cr=Em]
[00:36.72] [cr]I walk this empty[/cr=Em] [cr]street[/cr=G][cr]On the Boulevard of Broken Dreams[/cr=D]
[00:43.78] [cr]Where the city[/cr=Em] [cr]sleeps[/cr=G][cr]and I'm the only one and I walk alone[/cr=Em]
[00:57.58] [cr]I walk alone,[/cr=Em] [cr]I walk alone[/cr=G][cr]I walk alone[/cr=D][cr]I walk alone and I walk a...[/cr=Em]
```

# Other Features

#### Word-by-Word Millisecond accurate for Karaeoke Mode

##### Also See - 
A2_extension:_word_time_tag - https://en.wikipedia.org/wiki/LRC_(file_format)#A2_extension:_word_time_tag
LRC Enhanced Format - https://en.wikipedia.org/wiki/LRC_(file_format)#A2_extension:_word_time_tag
Enhanced_format - https://en.wikipedia.org/wiki/LRC_(file_format)#Enhanced_format

Words with milliseconds accuracy - Will hilight words as they are being played. This will be usefull for kareoke.

### Format 

(same as https://en.wikipedia.org/wiki/LRC_(file_format)#A2_extension:_word_time_tag)

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

## Expect Adaptation By
1. Spotify(https://open.spotify.com/)
1. MusixMatch(https://www.musixmatch.com/)
1. Genius(https://genius.com/)
1. OpenLyrics foobar2000 lyrics component(https://github.com/jacquesh/foo_openlyrics)
1. https://github.com/Spikatrix/LRC-Editor
1. https://lrc-maker.github.io/
1. https://github.com/lemutec/LyricStudio

## Also See
1. ID3 Specs - https://id3.org/Lyrics3v21. 
1. Cross-platform advanced subtitle editor - https://github.com/Aegisub/Aegisub
1. OpenLyrics (https://github.com/openlyrics/openlyrics) - is a free, open XML standard for Christian worship songs. The goal of OpenLyrics is to provide an application-independant and operating system-independant song format for interoperability between applications

## SyncedLyric Sources
1. https://www.rentanadviser.com
1. https://www.megalobiz.com/
1. https://www.lyricsify.com/
