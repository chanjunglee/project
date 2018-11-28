from Db_Server import db_server
from Model import *
# from pprint import pprint
from Utill import geocoding_address
from time import sleep
import re

db_server.db_connect()

end = len(Old_Building.Old_building().select().tuples())

for j in range(1, 2770, 1):

    for i in Old_Building.Old_building.select().order_by(Old_Building.Old_building.id).paginate(j,100):

        if i.LONG == 0 and i.LAT==0:

            print(re.sub('번지','',i.LAND_LOC))

            geogeo = geocoding_address.reverse_geocoding(re.sub('번지','',i.LAND_LOC))
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

        else:
            pass

