def distance(lat1, lon1, lat2, lon2):
    from math import cos, asin, sqrt
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))




from Db_Server import db_server
from Model import *
from Utill import geocoding_address
from pprint import pprint
import random



db_server.db_connect()

min_dist_lit =[]

for i in Old_Building.sample_loader(1000):

    long = i[20]
    lat = i[21]

    # print(i[1])

    if lat == 0 and long == 0:
        pass

    else:
        dist_lit = []
        for j in Univ.Univ.select().order_by(Univ.Univ.id):
            dist_lit.append(distance(lat, long, j.LAT, j.LONG) )


        min_dist_lit.append(min(dist_lit))


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
import seaborn as sns
sns.distplot(min_dist_lit, rug=True)
plt.show()


plt.plot(min_dist_lit)
plt.show()

min_dist_lit.sort()
print(min_dist_lit[200],min_dist_lit[400],min_dist_lit[600],min_dist_lit[800])

# from scipy import stats as sp
# rv = sp.stats.normaltest(min_dist_lit,axis=0)
# print(rv)
# print(sp.stats.describe(min_dist_lit))
# xx = np.linspace(0, 4, 30)
# plt.plot(xx, rv.pdf(xx))
# plt.ylabel("p(x)")
# plt.title("정규 분포의 확률 밀도 함수(pdf)")
# plt.show()

# import seaborn as sns
# sns.distplot(min_dist_lit, rug=True)
# plt.show()


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