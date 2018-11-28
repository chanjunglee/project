# -*- coding: utf-8 -*-

from peewee import *
from Db_Server import db_server
import csv
import os

class Living_Pop(Model):
    # 순번 = IntegerField(null=True)
    HJD_CODE = IntegerField(null=True)
    HJD = CharField(null=True)
    BJD = CharField(null=True)
    CNT = IntegerField(null=True)
    TIME = IntegerField(null=True)


    class Meta:
        database = db_server.psql_db  # This model uses the "people.db" database.


def table_create():
    # db_server.db_connect()

    db_server.table_create(Living_Pop)

def table_drop():
    # db_server.db_connect()

    db_server.table_drop(Living_Pop)


def insert_interest():


    path = 'C:\\yang\\living_pop_0\\'
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
                Living_Pop.insert(HJD_CODE=row[0], HJD=row[1], BJD=row[2], CNT=row[3],
                                  TIME=row[4]).execute()

def loader():
    metro_list = []

    for i in Living_Pop.select().tuples():
        metro_list.append(i)

    return metro_list










