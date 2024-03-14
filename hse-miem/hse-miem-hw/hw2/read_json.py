import json

import glob
import re

import numpy as np

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

songs = []

for file_name in glob.glob('Lyrics_*.json'):
    with open(file_name) as f:
        d = json.load(f)
        for song in d['songs']:

            artist = song['artist']
            lyrics = song['lyrics']

            lyrics = ''.join(lyrics.split("\n")[2:])
            lyrics = lyrics.lower()
            lyrics = re.sub("\[.*?\]", "", lyrics)
            for ch in lyrics:
                lyrics = lyrics.replace(ch, "") if ch in punc else lyrics
            lyrics = lyrics.replace('\n', " ")

            songs.append([lyrics, artist])

songs = np.array(songs)

print(songs.shape)
print(songs)

np.save('songs.npy', songs)

