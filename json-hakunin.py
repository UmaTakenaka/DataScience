import urllib.request as req
import os.path, random
import json

url = "http://api.aoikujira.com/hyakunin/get.php?fmt=json"
savename = "hyakunin.json"
if not os.path.exists(url):
    req.urlretrieve(url, savename)

s = open(savename, "r", encoding="utf-8").read()
data = json.loads(s)

# print(data)
r = random.choice(data)
print("No.", r['no'],r['kami'],r['simo'])