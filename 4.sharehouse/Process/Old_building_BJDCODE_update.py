#
# ## pgadmin4에서 BJD_CODE라는 컬럼을 생성한 후 실행.
#
# # from peewee import *
# #
# # psql_db = PostgresqlDatabase('my_database',
# #                              user='postgres',
# #                              password='share',
# #                              host='localhost')
# #
# #
# #
# # class Old_building(Model):
# #     LAND_LOC = CharField(null=True)
# #     SIGUNGU_CODE = IntegerField(null=True)
# #     BJD_S_CODE = IntegerField(null=True)
# #     BJD_CODE = IntegerField(null=True)
# #     ROAD_LOC = CharField(null=True)
# #     B_NAME = CharField(null=True)
# #     L_AREA = FloatField(null=True)
# #     ARCH_AREA = FloatField(null=True)
# #     BC_RAT = FloatField(null=True)
# #     TOTAREA = FloatField(null=True)
# #     VL_RAT_ESTM_TOTAREA = FloatField(null=True)
# #     VL_RAT= FloatField(null=True)
# #     STRCT_CD_NM = CharField(null=True)
# #     MAIN_PURPS_CD_NM = CharField(null=True)
# #     ETC_PURPS = CharField(null=True)
# #     HHLD_CNT = IntegerField(null=True)
# #     FMLY_CNT= IntegerField(null=True)
# #     GRND_FLR_CNT = IntegerField(null=True)
# #     UND_FLR_CNT = IntegerField(null=True)
# #     USEAPR_DAY = CharField(null=True)
# #
# #     class Meta:
# #         database = psql_db  # This model uses the "people.db" database.
# #
# #
# # psql_db.connect()
# #
#
#
# from Db_Server import db_server
#
# from Model import *
#
# from Execl import *
#
# db_server.db_connect()
#
#
#
# Old_Building.loader()
#
#
# class Old_update(Old_Building):
#
#     old_lit = []
#
#     for old in Old_building.select().tuples():
#         # print(sang)
#         old_lit.append('%d%d' %(old[2],old[3]))
#
#
#     #test
#     # cnt = 0
#     # for i in old_lit:
#     #
#     #     if cnt == 45:
#     #
#     #         break
#     #
#     #     print(i)
#     #
#     #     cnt += 1
#
#
#
#     cnt_j = 1
#     for j in old_lit:
#         print(j)
#         q= Old_building.update(BJD_CODE = j).where(Old_building.id == cnt_j)
#         q.execute()
#
#         cnt_j += 1
