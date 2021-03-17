import requests as rq
from time import sleep
import os
print("To find station ID, look at the end of the link. iheart.com/live/the-new-93q-5892 as an example, the last 4 numbers is your station ID. So if I wanted to listen to Full Metal Jackie, I'd enter 6225. Or if I wanted to listen to The Vinyl Experience, I'd enter 6878.")
print("Enter 0 to listen to Full Metal Jackie, this only exists to make it easier for me to listen to FMJ lol")
station = int(input("Enter Station ID | "))
if station == 0:
    station = 6225
url = "https://api.iheart.com/api/v3/live-meta/stream/" + str(station) + "/currentTrackMeta"
i = 1
err = 0
oldtitle = "a"
os.system('clear')
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
            print("iHeart Radio | Channel ID " + str(station))
            oldtitle = title
    elif err == 0:
        os.system('clear')
        print("\033[96m" + "Thanks for listening! (No Song Metadata)")
        print("\033[98m" + "If you're seeing this, there's either no song playing, the metadata on the api hasn't updated yet, or you entered an invalid station ID.")
        print("Worst case scenario I fucked up and my code doesn't work.")
        err = 1
    sleep(5)
