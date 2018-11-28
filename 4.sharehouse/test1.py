def distance(lat1, lon1, lat2, lon2):
    from math import cos, asin, sqrt
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))

# for share_ind in range(len(share)):
#
#     share_cnt = 0
#
#     for subway_ind in range(len(subway)):
#
#         if distance(float(share[share_ind][3]), float(share[share_ind][4]), float(subway[subway_ind][7]),
# float(subway[subway_ind][8])) <= 1:
#
#             share_cnt += 1
#
#     near_subway.append(share_cnt)



from Db_Server import db_server
from Model import *
from Utill import geocoding_address
from pprint import pprint
import random


# 거리 계산하는 코드
db_server.db_connect()
# geogeo = geocoding_address.reverse_geocoding(Old_Building.loader()[0][1])
# # pprint(geogeo)
#
# LONG = float(geogeo["documents"][0]['address']['x'])
# LAT = float(geogeo["documents"][0]['address']['y'])

share_cnt_lit = []
# old_completed = 0



for i in Old_Building.sample_loader(100):

    share_cnt = 0

    geogeo = geocoding_address.reverse_geocoding(i[1])
    # print(geogeo)
    # pprint(geogeo)

    LONG = float(geogeo["documents"][0]['address']['x'])
    LAT = float(geogeo["documents"][0]['address']['y'])

    # cnt=0

    for j in Bus.loader():

        # if cnt == 260:
        #     print('@ old '+ old_completed +'completed')
        #     old_completed = old_completed +1
        # print(i)
        # print(i[5])
        if distance(LAT, LONG, float(j[3]), float(j[4])) <= 0.2:

            share_cnt = share_cnt+1

            # cnt = cnt + 1
            print(share_cnt)
        share_cnt_lit.append(share_cnt)

print(share_cnt_lit)

# 테이블에서 데이터 가져와서 분석


from Db_Server import db_server
from Model import *
from Utill import geocoding_address
from pprint import pprint
import random







# db_server.db_connect()
#
# dist_lit = []
# min_dist_lit =[]
#
# for i in Old_Building.sample_loader(100):
#
#     long = i[20]
#     lat = i[21]
#
#     if lat == 0 and long == 0:
#         pass
#
#     else:
#
#         for j in Comm_Reg.Comm_reg.select().order_by(Comm_Reg.Comm_reg.id):
#
#             dist_lit.append( distance(lat, long, j.LAT, j.LONG))
#
#         min_dist_lit.append(min(dist_lit))






#error ImportError: DLL load failed: 지정된 모듈을 찾을 수 없습니다.
#conda remove matplotlib
#pip install matplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
# print(dist_lit)
# plt.boxplot(dist_lit)
# plt.show()

print(min_dist_lit)
plt.plot(min_dist_lit)
plt.show()
# def normalFunS(x, mu,sd):
#     a=1/(sd*np.sqrt(2*np.pi))
#     b=np.exp(-(x-mu)**2/(2*sd**2))
#     return(a*b)
#
# n, bins, ig=plt.hist(dist_lit, bins=50, normed=True)
# mu=np.mean(dist_lit)
# sd=np.std(dist_lit)
# plt.plot(bins, normalFunS(bins, mu, sd), linewidth=2, color="r")
# plt.show()
