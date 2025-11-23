import re
import certifi
import os
import requests


def runServers():
    with open("docs/playlist1.m3u8", "w") as file:
        file.write("#EXTM3U\n")
    for i in range(len(lis)):
        print(f"{i+1}.{lis[i]}")
        server1(i + 1, lis[i])
        
    with open("docs/playlist2.m3u8", "w") as file:
        file.write("#EXTM3U\n")
    for i in range(len(hashCode)):
        print(f"{i+1}.{channels[i]}")
        server2(hashCode[i], channels[i])

    


def server1(i, name):
    print("Running Server 1")
    url = f"https://adult-tv-channels.com/tv/{name}.php"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://adult-tv-channels.com",
        "X-Requested-With": "XMLHttpRequest",
    }

    response = requests.get(url, headers=headers, verify=certifi.where())

    # Use regex to extract the source URL
    match = re.search(r'file:\s*"([^"]+playlist\.m3u8[^"]*)"', response.text)
    if match:
        stream_url = match.group(1)
        # print(stream_url)
        with open("docs/playlist1.m3u8", "a") as file:
            file.write(f"#EXTINF:-1,{name}\n")
            file.write(f"{stream_url}\n")

    else:
        print("No URL found.")


def server2(hash, name):
    print("Running Server 2")
    res = requests.post(
        f"http://oxax.tv/(hash).html",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    data = res.json()
    token = data["fileUrl"]

    stream_url = f"https://s.oxax.tv/{name}/index.m3u8?k={k}"
    with open("docs/playlist2.m3u8", "a") as file:
        file.write(f"#EXTINF:-1,{name}\n")
        file.write(f"{stream_url}\n")
    # print(stream_url)





# For Server 1
print("Available Channels\nSome links might not works!!!")
lis = [
    "brazzerstv",
    "hustlerhd",
    "hustlertv",
    "penthouse",
    "redlight",
    "penthousepassion",
    "vivid",
    "dorcel",
    "superone",
    "oxax",
    "passie",
    "eroxxx",
    "playboy",
    "pinko",
    "extasy",
    "penthousereality",
    "kinoxxx",
    "pinkerotic",
    "pinkerotic7",
    "pinkerotic8",
    "evilangel",
    "private",
    "beate",
    "meiden",
    "centoxcento",
    "barelylegal",
    "venus",
    "freextv",
    "erox",
    "passion",
    "satisfaction",
    "jasmin",
    "fap",
    "olala",
    "miamitv",
]

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
