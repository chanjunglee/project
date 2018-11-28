from Db_Server import db_server
from Model import *

db_server.db_connect()

cnt = 0

for i in Metro.loader():

    if i == 30:

        break

    print(i)

    cnt += 1



