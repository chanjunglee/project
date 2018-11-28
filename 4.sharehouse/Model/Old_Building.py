# -*- coding: utf-8 -*-
from peewee import *
from Db_Server import db_server
import csv
import os
import random

class Old_building(Model):
    # 순번 = IntegerField(null=True)
    LAND_LOC = CharField(null=True)
    SIGUNGU_CODE = IntegerField(null=True)
    BJD_S_CODE = IntegerField(null=True)
    ROAD_LOC = CharField(null=True)
    B_NAME = CharField(null=True)
    L_AREA = DoubleField(null=True)
    ARCH_AREA = DoubleField(null=True)
    BC_RAT = DoubleField(null=True)
    TOTAREA = DoubleField(null=True)
    VL_RAT_ESTM_TOTAREA = DoubleField(null=True)
    VL_RAT= DoubleField(null=True)
    STRCT_CD_NM = CharField(null=True)
    MAIN_PURPS_CD_NM = CharField(null=True)
    ETC_PURPS = CharField(null=True)
    HHLD_CNT = IntegerField(null=True)
    FMLY_CNT= IntegerField(null=True)
    GRND_FLR_CNT = IntegerField(null=True)
    UND_FLR_CNT = IntegerField(null=True)
    USEAPR_DAY = CharField(null=True)
    LONG = DoubleField(null=True)
    LAT = DoubleField(null=True)

    class Meta:
        database = db_server.psql_db

def table_create():
    # db_server.db_connect()

    db_server.table_create(Old_building)

def table_drop():
    # db_server.db_connect()

    db_server.table_drop(Old_building)

def insert_interest():
    # db_server.db_connect()

    path = 'C:\\yang\\old_building_0\\'
    gu_lst = []

    for file_or_dir in os.listdir(path):  # 입력한 경로의 파일과 폴더 목록 리스트를 loop문 돌림
        # print('$',file_or_dir)

        abs_path = os.path.abspath(file_or_dir)
        s = os.path.splitext(abs_path)

        if '.csv' in os.path.split(s[1]):
            s = os.path.split(s[0])
            gu_lst.append((s[1]))

    for i in gu_lst:

        with open(path + i +".csv") as data_file:
            reader = list(csv.reader(data_file, delimiter=',', quotechar='"'))
            reader.remove(reader[0])
            for row in reader:
                Old_building.insert(LAND_LOC=row[0], SIGUNGU_CODE=row[1], BJD_S_CODE=row[2], ROAD_LOC=row[3],
                                    B_NAME=row[4], L_AREA=row[5], ARCH_AREA=row[6], BC_RAT=row[7], TOTAREA=row[8],
                                    VL_RAT_ESTM_TOTAREA=row[9], VL_RAT=row[10], STRCT_CD_NM=row[11],
                                    MAIN_PURPS_CD_NM=row[12], ETC_PURPS=row[13], HHLD_CNT=row[14], FMLY_CNT=row[15],
                                    GRND_FLR_CNT=row[16], UND_FLR_CNT=row[17], USEAPR_DAY=row[18]).execute()

def loader():
    old_list = []

    for i in Old_building.select().tuples():
        old_list.append(i)

    return old_list



def sample_loader(number):
    old_list = []
    rand_list = []

    for i in Old_building.select().tuples():
        old_list.append(i)

    for j in random.sample(old_list,number):
        rand_list.append(j)

    # return old_list
    return rand_list




