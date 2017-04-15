import pandas as pd

album_data = pd.read_csv("top_album.csv", sep=',')

album_data.album = album_data.album.str.replace(' ','-')
album_data.album = album_data.album.str.replace("'",'-')
album_data.album = album_data.album.str.replace(".",'')
album_data.album = album_data.album.str.replace(" ?",'')
album_data.artist = album_data.artist.str.replace("'", '')
album_data.artist = album_data.artist.str.replace(' ', '-')

from unidecode import unidecode
for i in range(0,len(album_data)):
    album_data.album.iloc[i] = unidecode(album_data.album.iloc[i].lower())
    album_data.artist.iloc[i] = unidecode(album_data.artist.iloc[i].lower())

album_data["url"] = ""
for i in range(0,len(album_data)):
    album_data.url.iloc[i] = "https://genius.com/albums/" + album_data.artist.iloc[i] + '/' + album_data.album.iloc[i]

album_data.to_csv("album_data_with_url.csv")