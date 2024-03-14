from lyricsgenius import Genius

genius = Genius('xWerHTtNQS-mEjU_KvwENPGYL2uVh4AI__BAS2DSdSZYDbglBRlvxLWh25GEtuV0')

artists_name = [
    'Fall Out Boy',
    'Dax',
    'AJR',
    'Eminem',
    'Evanescence',
    'Panic! At The Disco',
    'Frank Sinatra'
    'Imagine Dragons'
]

for artist_name in artists_name:
    artist = genius.search_artist(artist_name, max_songs=20)
    artist.save_lyrics()
