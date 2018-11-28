# # -*- coding: utf-8 -*-
# from peewee import *
# from used_file import geocoding_long_lat
#
# psql_db = PostgresqlDatabase('my_database',  # Required by Peewee.
#                              user='postgres',  # Will be passed directly to psycopg2.
#                              password='share',  # Ditto.
#                              host='localhost')
#
# psql_db.connect()
#
# class Comm_Reg(Model):
#     # 순번 = IntegerField(null=True)
#     TRD_ID = IntegerField(null=True)
#     TRD_NM = CharField(null=True)
#     SHAPE_AREA = FloatField(null=True)
#     LONG = FloatField(null=True)
#     LAT = FloatField(null=True)
#     BJD = CharField(null=True)
#
#     class Meta:
#         database = psql_db  # This model uses the "people.db" database.
#
#
#
#
# # Sangtest.update(Sangtest.BUB_D=i).where(Sangtest.id == j)
# # for sang in Sangtest.select().tuples():
# #     print(sang)
#     # sang_lit.append(sang)
#
# id_list = []
# for m in Comm_Reg.select().tuples():
#
#     id_list.append(m[0])
#
# print(id_list)
#
#
#
# # print(geocoding_long_lat.dong_list[0])
# # for i in geocoding_long_lat.dong_list:
# #     print(i)
#
#
#
#
#
#
#
# for j in id_list:
#     print(j)
#     q= Comm_Reg.update(BJD = geocoding_long_lat.dong_list[j-1]).where(Comm_Reg.id == j)
#     q.execute()
#
# #         # Sangtest.get(id=j).update(BUB_D= i).execute()
#
#     # Sangtest.insert(BUB_D = i).execute()
#
#
