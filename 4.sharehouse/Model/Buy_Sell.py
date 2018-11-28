# -*- coding: utf-8 -*-
from peewee import *
from Db_Server import db_server
import os
import csv
import re

class Buy_sell(Model):
    # 순번 = IntegerField(null=True)
    SIGUNGU = CharField(null=True)
    BON_BUN = IntegerField(null=True)
    BU_BUN = IntegerField(null=True)
    AREA_NAME = CharField(null=True)
    PRI_MSR= DoubleField(null=True)
    L_AREA= DoubleField(null=True)
    CONT_MONTH = CharField(null=True)
    CONT_TERM = CharField(null=True)
    CONT_PRICE = BigIntegerField(null=True)
    FLOOR = IntegerField(null=True)
    CONST_Y= CharField(null=True)
    B_TYPE = CharField(null=True)

    class Meta:
        database = db_server.psql_db

def table_create():
    # db_server.db_connect()

    db_server.table_create(Buy_sell)

def table_drop():
    # db_server.db_connect()

    db_server.table_drop(Buy_sell)

def insert_interest():

    path = 'C:\\yang\\buy_sell_0\\'
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

                if row[6] is None or len(row[6]) <= 0: row[6] = 0.0

                Buy_sell.insert(SIGUNGU=row[0], BON_BUN=row[2], BU_BUN=row[3],
                                 AREA_NAME=row[4], PRI_MSR=row[5], L_AREA=row[6], CONT_MONTH=row[7], CONT_TERM=row[8],
                                 CONT_PRICE=re.sub(',', '', row[9]), FLOOR=row[10], CONST_Y=row[11],
                                 B_TYPE=row[13]).execute()


def loader():
    buy_sell_list = []

    for i in Buy_sell.select().tuples():
        buy_sell_list.append(i)

    return buy_sell_list