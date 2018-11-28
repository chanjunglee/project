# from peewee import *
#
#
# import csv
# import os
# import random
#
# #
# from Db_Server import db_server
# from Model import *
#
#

# 263289

# db_server.db_connect()

# cnt =0
# for i in Old_Building.Old_building.select().dicts():

#     if cnt < 11:

#         print(i)
#         cnt =cnt+1
#     else:
#         break

# print(len(Old_Building.Old_building.select().tuples()))

# for i in Old_Building.Old_building.select().order_by(Old_Building.Old_building.id).paginate(1,10):

#     print(i.Old_building)

# cnt=1
# for i in Old_Building.loader():
#     print(i)
#     print(cnt)
#     cnt =cnt +1

from Db_Server import db_server
from Model import *
# from pprint import pprint
from Utill import geocoding_address
# from time import sleep
# import random

db_server.db_connect()

end= len(Old_Building.Old_building().select().tuples())
# print(end)
# print(round(end/100))
# end2 = round((end-123052)/100)
# print(end2)

#276891 # 263289
# j= 2768

for j in range(2632, 2000, -1):


    for i in Old_Building.Old_building.select().order_by(Old_Building.Old_building.id).paginate(j,100):


        geogeo = geocoding_address.reverse_geocoding(i.LAND_LOC)
        print(geogeo)
        try:
            long = float(geogeo["documents"][0]['address']['x'])
            lat = float(geogeo["documents"][0]['address']['y'])
            # sleep(random.uniform(0, 1))

            q = Old_Building.Old_building.update(LONG= long , LAT= lat).where(Old_Building.Old_building.id == i)
            q.execute()

        except:
            q = Old_Building.Old_building.update(LONG=0, LAT=0).where(Old_Building.Old_building.id == i)
            q.execute()
            print('$$$$$$$$$$$$$$ abnormal data occured!!$$$$$$$$$$$$$$$$')

        print(i)