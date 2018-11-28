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





db_server.db_connect()
geogeo = geocoding_address.reverse_geocoding(Old_Building.loader()[0][1])
# pprint(geogeo)

LONG = float(geogeo["documents"][0]['address']['x'])
LAT = float(geogeo["documents"][0]['address']['y'])

share_cnt = 0
old_completed = 0
for i in Old_Building.loader():

    try:
        geogeo = geocoding_address.reverse_geocoding(i[1])
        print(geogeo)
        # pprint(geogeo)

        LONG = float(geogeo["documents"][0]['address']['x'])
        LAT = float(geogeo["documents"][0]['address']['y'])

        cnt=0

        for j in Comm_Reg.loader():

            if cnt == 261:
                print('@ old '+ old_completed +'completed')
                old_completed = old_completed +1
            # print(i)
            # print(i[5])
            if distance(LAT, LONG, float(j[5]), float(j[4])) <= 1:

                share_cnt = share_cnt+1

            cnt = cnt + 1
        print(share_cnt)

    except:
        print("abnormal data occured")




    #
    # if cnt == 1:
    #
    #     break
    # print(i)
    # # print(i[5])
    # print(distance(LAT,LONG,float(i[5]),float(i[4]) ) )
    # cnt=cnt+1
    #
    #


# sleep(random.uniform(0,1))











# print(LONG + ','+LAT)

cnt=0
for i in Comm_Reg.loader():

    if cnt == 1:

        break
    print(i)
    # print(i[5])
    print(distance(LAT,LONG,float(i[5]),float(i[4]) ) )
    cnt=cnt+1


# distance