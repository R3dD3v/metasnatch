#   Metasnatch 0.5.8
#   RedDevRedemption

# Importing libraries lol
import requests as rq
from time import sleep
import os, json

def setup():
    # Doing magic config stuff
    with open("metasnatch.json", "r") as jsonfile:
        settings = json.load(jsonfile)
    defaultStation = settings["defaultStation"]
    jsonfile.close()
    return defaultStation

def menu(channel=None):
    os.system('clear||cls')
    print("\033[96m - Metasnatch 0.5.8 - \033[00m")
    print("h - for help.")
    print("q - to quit.")
    if channel is None:
        station = input("Enter Station ID : ")
    else:
        station = channel
    if station == "":
        station = setup()
    url = f"https://api.iheart.com/api/v3/live-meta/stream/{str(station)}/trackHistory?limit=1"
    os.system('cls||clear')
    if station == "h":
        help()
    elif station != "h":
        display(url, station)
    elif station == "q":
        quit()

def quit():
    print("Exiting...")
    sleep(1)
    exit(1)

def help():
    i = 10
    while i > -1:
        os.system('cls||clear')
        print("The station ID is the last 4 numbers in the link of your iHeart radio station.")
        print("iheart.com/full-metal-jackie-6225 | The ID is 6225")
        print("Hopefully that clears things up")
        print(f"- Clearing in {str(i)} -")
        i = i - 1
        sleep(1)
    menu()
    
def display(url, station):
    viewing = True
    while viewing:
        try:
            try:
                data = rq.get(url)
                stat = data
                info = data.json()['data']
                data = info[0]
            except KeyError:
                if station == "q":
                    quit()
                i=3
                while i > -1:
                    os.system('cls||clear')
                    print("Channel not found.")
                    print(f" - Clearing in {str(i)} - ")
                    i=i-1
                    sleep(1)
                menu()
            
            if stat.status_code == 200:
                artist = data['artist']
                title = data['title']
                err = 0
                oldtitle = "a"
                if oldtitle != title:
                    os.system('cls||clear')
                    print("\033[92m")
                    print("----------- \033[96m")
                    print("Now Playing")
                    print(f"{artist} - {title} \033[00m \033[92m")
                    print("----------- \033[94m")
                    print(f"iHeart Radio | Channel ID {str(station)} \033[92m")
                    print("Metasnatch 0.5.8 | RedDevRedemption")
                    oldtitle = title
                    channel = input("Snatch another channel: ")
                    viewing = False
                    menu(channel)
            elif err == 0:
                os.system('cls||clear')
                print(f"\033[96m Thanks for listening! (No Song Metadata) | Channel ID {str(station)}")
                print("\033[98m If you're seeing this, there's either no song playing, the metadata on the api hasn't updated yet, or you entered an invalid station ID.")
                print("Worst case scenario I fucked up and my code doesn't work.")
                err = 1
                channel = input("Snatch another channel: ")
                viewing = False
                menu(channel)
            sleep(5)
        except Exception as e:
            print(e)
            quit()

if __name__ == '__main__':
    menu(None)
