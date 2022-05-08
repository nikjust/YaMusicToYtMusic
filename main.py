import json
import sys
import time

import requests

playlist_url = open("playlist.txt", "r").read()

r = requests.get(playlist_url)
playlist = json.loads(r.text)
tracks = playlist['playlist']["tracks"]
music = []

for track in tracks:
    tr = f"{track['artists'][0]['name']} - {track['title']}"
    music.append(tr)
    print(tr)

print(music)

while True:
    reaction = input("copy yandex music playlist to youtube music? (y/n): ")

    if reaction == "n":
        sys.exit()
    if reaction == "y":
        break

from ytmusicapi import YTMusic


YTMusic.setup(filepath='headers_auth.json', headers_raw=open("raw_headers.txt", "r").read())
ytmusic = YTMusic("headers_auth.json")

playlistId = ytmusic.create_playlist('YaMusic', 'YaMusic copied music')

for m in music:
    time.sleep(0.5)
    try:
        search_results = ytmusic.search(m)
        ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])
    except KeyError:
        print(f"track: {m} not found")
    except Exception as e:
        print(f"track: {m} gived an error: {e}")
    else:
        print(f"{m} was copied successfully")
