#   Metasnatch 0.5.7
#   RedDevRedemption

# Importing libraries lol
import requests as rq
from time import sleep
import os
import json

a = 0
while a == 0:
    # Doing magic config stuff
    with open("metasnatch.json", "r") as jsonfile:
        settings = json.load(jsonfile)
    defaultStation = settings["defaultStation"]
    jsonfile.close()
    # Get input
    os.system('clear')
    print("\033[96m - Metasnatch 0.5.7 - \033[00m")
    print("h | help")
    station = input("Enter Station ID | ")
    if station == "":
        station = defaultStation
    url = "https://api.iheart.com/api/v3/live-meta/stream/" + str(station) + "/trackHistory?limit=1"
    i = 10
    err = 0
    oldtitle = "a"
    os.system('clear')
    if station == "h":
        while i > -1:
            os.system('clear')
            print("The station ID is the last 4 numbers in the link of your iHeart radio station.")
            print("iheart.com/full-metal-jackie-6225 | The ID is 6225")
            print("Hopefully that clears things up")
            print("[Clearing in " + str(i) + "]")
            i = i - 1
            sleep(1)
        os.system('clear')
    if station != "h":
        a = a + 1

# Let's get groovy!
while a != 0:
    data = rq.get(url)
    stat = data
    info = data.json()['data']
    data = info[0]
    if stat.status_code == 200:
        artist = data['artist']
        title = data['title']
        err = 0
        if oldtitle != title:
            os.system('clear')
            print("\033[92m")
            print("-----------" + "\033[96m")
            print("Now Playing")
            print(artist + " - " + title + "\033[00m" + "\033[92m")
            print("-----------" + "\033[94m")
            print("iHeart Radio | Channel ID " + str(station) + "\033[92m")
            print("Metasnatch 0.5.7 | RedDevRedemption")
            oldtitle = title
    elif err == 0:
        os.system('clear')
        print("\033[96m" + "Thanks for listening! (No Song Metadata) | " + "Channel ID " + str(station))
        print("\033[98m" + "If you're seeing this, there's either no song playing, the metadata on the api hasn't updated yet, or you entered an invalid station ID.")
        print("Worst case scenario I fucked up and my code doesn't work.")
        err = 1
    sleep(5)
