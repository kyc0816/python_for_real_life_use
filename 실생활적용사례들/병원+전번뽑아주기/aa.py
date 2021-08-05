import json
import os

jsonfile = open('./aaa.json')

jsonfile = json.load(jsonfile)

for i in jsonfile:
    print(i['orgnm'] , i['orgTlno'])