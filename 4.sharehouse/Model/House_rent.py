# -*- coding: utf-8 -*-
from peewee import *
from Db_Server import db_server
import csv
import re
import os

class House_rent(Model):
    # 순번 = IntegerField(null=True)
    RESI_TYPE = CharField(null=True)
    SIGUNGU = CharField(null=True)
    BON_BUN = IntegerField(null=True)
    BU_BUN = IntegerField(null=True)
    AREA_NAME = CharField(null=True)
    RNT_TRD = CharField(null=True)
    PRI_MSR = DoubleField(null=True)
    # LOC_MSR = CharField(null=True)
    CONT_MONTH = CharField(null=True)
    CONT_TERM = CharField(null=True)
    PRICE = BigIntegerField(null=True)
    FEE = IntegerField(null=True)
    FLOOR = IntegerField(null=True)

    class Meta:
        database = db_server.psql_db  # This model uses the "people.db" database.

def table_create():
    # db_server.db_connect()

    db_server.table_create(House_rent)

def table_drop():
    # db_server.db_connect()

    db_server.table_drop(House_rent)


def insert_interest():

    path = 'C:\\yang\\rent\\'
    gu_lst = []
    for file_or_dir in os.listdir(path):  # 입력한 경로의 파일과 폴더 목록 리스트를 loop문 돌림
        # print('$',file_or_dir)

        abs_path = os.path.abspath(file_or_dir)
        s = os.path.splitext(abs_path)

        if '.csv' in os.path.split(s[1]):
            s = os.path.split(s[0])
            gu_lst.append((s[1]))

    for i in gu_lst:

        with open(path + i + ".csv") as data_file:

            reader = list(csv.reader(data_file, delimiter=',', quotechar='"'))
            reader.remove(reader[0])

            for row in reader:
                House_rent.insert(RESI_TYPE=row[0], SIGUNGU=row[1], BON_BUN=row[2], BU_BUN=row[3],
                                   AREA_NAME=row[4], RNT_TRD=row[5], PRI_MSR=row[6], # LOC_MSR=row[6],
                                   CONT_MONTH=row[7], CONT_TERM=row[8],
                                   PRICE=re.sub(',', '',row[9]), FEE=re.sub(',', '',row[10]), FLOOR=row[11]).execute()

def loader():
    rent_list = []

    for i in House_rent.select().tuples():
        rent_list.append(i)

    return rent_list