import json
import urllib.request as request
from time import sleep
import random


def geocoding(lat, lng):
    header = {
        "Authorization": "KakaoAK 326e38503f420e1f0088dab1f46dc0c7",
        "KA": "sdk/4.0.9 os/javascript lang/ko-KR device/MacIntel origin/http%3A%2F%2Fapis.map.daum.net",
        "Origin": "http://apis.map.daum.net",
        "Referer": "http://apis.map.daum.net/web/sample/coord2addr/",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36"
    }
    url = "http://dapi.kakao.com/v2/local/geo/coord2address.json?x={0}&y={1}".format(lat, lng)
    req = request.Request(url, headers=header)
    return json.load(request.urlopen(req))

# if __name__ == "__main__":
#     result = geocoding(126.97894091821667, 37.56674091239783)
#     print(result)


import csv
filesource = 'C:\\seoul_bigdata\\sanggwan_m1.csv'

geo_list = []

with open(filesource, 'r') as f:
    reader = list(csv.reader(f, delimiter=',', quotechar='"'))
    reader.remove(reader[0])

    for i in reader:

        # print(geocoding(i[1],i[2]))
        geo_list.append(geocoding(i[3],i[4]))
        sleep(random.uniform(0,1))

dong_list = []

for i in range(len(geo_list)):

    dong_list.append(geo_list[i]['documents'][0]['address']['region_3depth_name'])