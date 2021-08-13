import json
import os

jsonfile = open('./aaa.json') # 이건 예시이고, 본인 지역 데이터를 json으로 저장하고 그걸 불러주면 됨

jsonfile = json.load(jsonfile)

for i in jsonfile:
    print(i['orgnm'] , i['orgTlno'])