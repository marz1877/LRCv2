# lrc_SyncedLyrics_v2
draft for format specs for lrc/SyncedLyric. Please contribute

Also See - https://id3.org/Lyrics3v2

## 1 .lrc/SyncedLyrics version info

Format 

```
[lrc version:2]
```

## 2 Singer - A song may have multiple singers

also see - https://en.wikipedia.org/wiki/LRC_(file_format)#Simple_format_extended

### Format

```
[00:12.00] [Singer:Jhon]Line 1 lyrics[/Singer:Jhon]
[00:16.00] [Singer:Luis]Line 2 lyrics[/Singer:Luis]
[1:01.00] [Singer:William,Luis]Line 3 lyrics
```

## 3 Contextual Meaning - by word/line/paragraph

### Format

```
#[Verse 2]
[00:00.00] Finding life along the way
[00:00.00] [Meaning]Melodies we haven't played
[00:00.00] No, I don't want no rest [/Meaning: That feeling where you just cant stop listening and can’t fall alseep because its to good to listen or to watch, its either its amazing or entertaining for you to hear or watch.](Yeah, yeah)
[00:00.00] Echoin' around these walls
[00:00.00] Fighting to create a song (Yeah)
[00:00.00] I don't wanna miss a beat
```

## 4 Foreign Language Translation - per Word 

### Format

```
[00:00.00] [WordMeanind,de>en]Überheblich[/WordMeanind:Arrogant], [WordMeanind]überlegen[/WordMeanind:consider]
```

## 5 Foreign Language Translation - Per Line/Phrase

### Format

```
[00:00.00] Tuuli tuule sinne [PhraseMeanind,fi>en]missä muruseni on[/PhraseMeanind:Literal:Where my loved ones are,CommonUsage:where's my baby?]
[00:00.00] Leiki hetki hänen hiuksillaan
[00:00.00] Kerro rakkauteni, kerro kuinka ikävöin
[00:00.00] Kerro, häntä ootan yhä vaan
```

## 6 Languages - Just metadata for song like "[ar:Lyrics artist]"

### Format

```
[language:Languages in the lyrics]
example [language:en,es,de]
```
## 7 UI for Translation and Meaning Feature

![ui](https://user-images.githubusercontent.com/105455604/168247326-d772633e-c073-4928-9400-ada37fa4817d.png)

When meaning mode from the top button is selected hovering over will show line, phrase or paragraph hilighted depening on context (when explaing song lyrics only one line or paragraph is sufficient) 

When translation mode is selected hovering over will hilight phrases (as small as possible) giving meaning of the phrase and words used trageted for langauge learning.

## 8 Milliseconds Word accuraccy for Karaeoke Mode

Words with milliseconds accuracy - Will hilight words as they are being played. This will be usefull for kareoke.

https://en.wikipedia.org/wiki/LRC_(file_format)#Enhanced_format

## 9 Custom Color - for expression

Format

```
[02:16.00] [cr=#dc143c]Destroy yourself, see who gives a[/cr] [cr=#420612]duck[/cr]
[02:18.00] See who gives a duck
```

## 10 Full Karaeoke - with MIDI for voice melody with pitch recognision and midi roll

A midi of voice melody can be supplied with audio files and the player can show midi roll and take mic input to work as a kareoke that can also work as a sining learing method.

![image](https://user-images.githubusercontent.com/105455604/168251330-d98a8d35-936d-44b7-9988-b86f71f4a67c.png)

It is "not similar" to https://en.wikipedia.org/wiki/CD%2BG  https://en.wikipedia.org/wiki/MP3%2BG
