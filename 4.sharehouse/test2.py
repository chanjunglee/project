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



db_server.db_connect()
# geogeo = geocoding_address.reverse_geocoding(Old_Building.loader()[0][1])
# # pprint(geogeo)
#
# LONG = float(geogeo["documents"][0]['address']['x'])
# LAT = float(geogeo["documents"][0]['address']['y'])

min_dist_lit = []
share_cnt=0
# old_completed = 0share_cnt_lit

for i in Old_Building.sample_loader(100):

    long = i[20]
    lat = i[21]

    # print(i[1])

    if lat == 0 and long == 0:
        pass

    else:
        share_cnt = 0
        for j in Bus.Bus.select().order_by(Bus.Bus.id):
            if distance(lat, long, j.LAT, j.LONG) <= 0.18:
                share_cnt = share_cnt + 1

            print(share_cnt)
        min_dist_lit.append(share_cnt)
    print('@@@@@',min_dist_lit)

min_dist_lit.append(share_cnt)

print(min_dist_lit)

min_dist_lit.sort()
print(min_dist_lit[200],min_dist_lit[400],min_dist_lit[600],min_dist_lit[800])

# print(len(share_cnt_lit))
# import numpy as np
# import matplotlib.pyplot as plt
#
# mu, sigma = np.mean(share_cnt_lit), np.std(share_cnt_lit)
# count, bins, ignored = plt.hist(share_cnt_lit, 5, normed=True)
# print(count)
# print(bins)
# print(ignored)

# sample들을 이용해서 Gaussian Distribution의 shape을 재구축해서 line으로 그린다.
# plt.scatter(bins,count)
# plt.xscale('log')

from scipy import stats as sp
rv = sp.stats.normaltest(share_cnt_lit,axis=0)
print(rv)
print(sp.stats.describe(share_cnt_lit))
# xx = np.linspace(0, 4, 30)
# plt.plot(xx, rv.pdf(xx))
# plt.ylabel("p(x)")
# plt.title("정규 분포의 확률 밀도 함수(pdf)")
# plt.show()

import seaborn as sns
sns.distplot(share_cnt_lit, rug=True)
plt.show()

# plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) *
#     np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)), linewidth=2, color='r')
# plt.show()

