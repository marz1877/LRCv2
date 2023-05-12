import os
import re
import argparse
import datetime
from pydub import AudioSegment

def millisecs_to_lrc_timestamp(millisecs):
    timestamp = str(datetime.timedelta(milliseconds=millisecs))
    return timestamp[:-3] + '.' + timestamp[-3:]

def lyrics_to_lrc(lyrics_file, audio_file):
    song = AudioSegment.from_file(audio_file)

    with open(lyrics_file, 'r') as f:
        lyrics = f.readlines()

    lrc = ''
    for line in lyrics:
        match = re.match(r'\[(\d{2}):(\d{2})\.(\d{2})\](.*)', line.strip())
        if match:
            mins, secs, millisecs, text = match.groups()
            timestamp = int(mins) * 60 * 1000 + int(secs) * 1000 + int(millisecs)
            lrc += '[{}]{}\n'.format(millisecs_to_lrc_timestamp(timestamp), text)

    lrc_file = os.path.splitext(lyrics_file)[0] + '.lrc'
    with open(lrc_file, 'w') as f:
        f.write(lrc)

    print('Synced lyrics saved to', lrc_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert lyrics to synced lyrics in .lrc format')
    parser.add_argument('lyrics_file', help='path to lyrics file')
    parser.add_argument('audio_file', help='path to audio file')
    args = parser.parse_args()

    lyrics_to_lrc(args.lyrics_file, args.audio_file)
