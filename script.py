import re
import certifi
import os
import requests


def runServers():
    with open("docs/playlist2.m3u8", "w") as file:
        file.write("#EXTM3U\n")
    for i in range(len(hashCode)):
        print(f"{i+1}.{channels[i]}")
        server2(hashCode[i], channels[i])

    


def server2(hash, name):
    print("Running Server 2")
    res = requests.post(
        f"http://oxax.tv/(hash).html",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    data = res.json()
    k = data["kodk"]

    stream_url = f"https://s.oxax.tv/{name}/index.m3u8?k={k}"
    with open("docs/playlist2.m3u8", "a") as file:
        file.write(f"#EXTINF:-1,{name}\n")
        file.write(f"{stream_url}\n")
    # print(stream_url)





# for Server 2
hashCode = [
    "brazzers-tv",
    "playboy-tv",
    "erox-hd",
    "eroxxx-hd",
    "hot-pleasure",
    "xy-mix-hd",
    "xy-max-hd",
    "xy-plus-hd",
    "o-la-la",
    "barely-legal",
    "brazzers-tv-europe",
    "hustler-hd",
    "dorcel-tv",
    "vivid-red",
    "oh-ah",
    "blue-hustler",
    "kino-xxx",
    "penthouse-gold",
    "penthouse-2",
    "private-tv",
    "shalun",
    "redlight-hd",
    "xxl",
    "red-lips",
    "pink-o",
    "extasyhd",
    "babes-tv",
    "sl-hot1",
    "sl-hot2",
]


channels = [
    "46",
    "6",
    "9",
    "47",
    "52",
    "55",
    "43",
    "50",
    "17",
    "42",
    "2",
    "10",
    "21",
    "7",
    "1",
    "19",
    "49",
    "39",
    "16",
    "11",
    "20",
    "12",
    "30",
    "3",
    "22",
    "29",
    "14",
    "59",
    "58",
]

runServers() #Runs the function to start the servers!
