import json

#followers
f = open("followers_1.json")
 
data = json.load(f)

follower = []

for a in data:
    for b in a["string_list_data"]:
        follower.append(b["value"])

# following
f = open("following.json")

data = json.load(f)

following = []

for a in data ["relationships_following"]:
    for b in a["string_list_data"]:
        following.append(b["value"])

orang_baik = []

for a in following:
    if a in follower:
        orang_baik.append(a)

for a in following:
    if a not in orang_baik:
        print("https://www.instagram.com/" + a)