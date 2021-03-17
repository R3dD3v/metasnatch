import requests as rq
from time import sleep
import os
url = "https://api.iheart.com/api/v3/live-meta/stream/6225/currentTrackMeta"
i = 1
err = 0
oldtitle = "a"
while i < 10:
    data = rq.get(url)
    if data.status_code == 200:
        artist = data.json()['artist']
        title = data.json()['title']
        err = 0
        if oldtitle != title:
            os.system('clear')
            print("\033[92m")
            print("-----------" + "\033[96m")
            print("Now Playing")
            print(artist + " - " + title + "\033[00m" + "\033[92m")
            print("-----------" + "\033[94m")
            print("iHeart Radio | Full Metal Jackie")
            oldtitle = title
    elif err == 0:
        os.system('clear')
        print("\033[96m" + "Thanks for listening to Full Metal Jackie (No Song Metadata)")
        err = 1
    sleep(5)
