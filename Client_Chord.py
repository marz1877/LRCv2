import re

def read_lrcv2_chords_lyrics(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
    chords = {}
    lyrics = {}
    for line in lines:
        if re.match(r'\[\d{2}:\d{2}\.\d{2}\]', line):
            # Parse timestamp
            timestamp = line.strip()[1:-1]
            
            # Parse lyrics and chords
            tokens = re.split(r'(\[.*?\])', line.strip()[10:])
            for i in range(len(tokens)):
                if tokens[i].startswith('['):
                    # Parse chord
                    chord = tokens[i][1:-1]
                    if chord not in chords:
                        chords[chord] = []
                    chords[chord].append(timestamp)
                elif tokens[i].strip():
                    # Parse lyric
                    if timestamp not in lyrics:
                        lyrics[timestamp] = ''
                    lyrics[timestamp] += tokens[i]
                    lyrics[timestamp] += ' '
    
    # Combine chords and lyrics
    chord_lyric_lines = []
    for timestamp in sorted(lyrics.keys()):
        # Add chords
        chord_line = ''
        for chord in sorted(chords.keys()):
            if timestamp in chords[chord]:
                chord_line += chord + ' '
            else:
                chord_line += '  '
        chord_lyric_lines.append(chord_line.strip())
        
        # Add lyrics
        lyric_line = lyrics[timestamp]
        chord_lyric_lines.append(lyric_line.strip())
        
    return chord_lyric_lines

# Example usage
file_path = 'example.lrcv2'
chord_lyric_lines = read_lrcv2_chords_lyrics(file_path)
for line in chord_lyric_lines:
    print(line)
