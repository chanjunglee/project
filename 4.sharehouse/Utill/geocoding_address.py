# -*- coding: utf-8 -*-

# import json
# import urllib.request as request
# import urllib.parse as parse
# from time import sleep
# import random
#
#
# def reverse_geocoding(address):
#     address = parse.quote(address, encoding="utf8")
#
#     header = {
#         "Authorization": "KakaoAK 326e38503f420e1f0088dab1f46dc0c7",
#         "KA": "sdk/4.0.9 os/javascript lang/ko-KR device/MacIntel origin/http%3A%2F%2Fapis.map.daum.net",
#         "Origin": "http://apis.map.daum.net",
#         "Referer": "http://apis.map.daum.net/web/sample/coord2addr/",
#         "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36"
#     }
#     url = "http://dapi.kakao.com/v2/local/search/address.json?query={0}&page=1&size=10".format(address)
#     req = request.Request(url, headers=header)
#     return json.load(request.urlopen(req))
#
# if __name__ == "__main__":
#      result = reverse_geocoding("제주특별자치도 제주시 첨단로 242")
#      print(result)

import json
import urllib.request as request
import urllib.parse as parse
from time import sleep
import random


def reverse_geocoding(address):
    address = parse.quote(address, encoding="utf8")

    header = {
        "Authorization": "KakaoAK 68618be5e4685f82220b3333724033bc",
        "KA": "sdk/4.0.9 os/javascript lang/ko-KR device/MacIntel origin/http%3A%2F%2Fbigdata.sharekim.com",
        "Origin": "http://bigdata.sharekim.com",
        "Referer": "http://bigdata.sharekim.com",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36"
    }
    url = "http://dapi.kakao.com/v2/local/search/address.json?query={0}&page=1&size=10".format(address)
    req = request.Request(url, headers=header)
    return json.load(request.urlopen(req))

if __name__ == "__main__":
     result = reverse_geocoding("제주특별자치도 제주시 첨단로 242")
     print(result)


print(reverse_geocoding("서울특별시 강남구 일원동 611-1번지"))