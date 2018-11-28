# -*- coding: utf-8 -*-
from peewee import *
from Db_Server import db_server
import csv

class Inter_code(Model):
    # 순번 = IntegerField(null=True)
    SIGUNGU = CharField(null=True)
    HJD = CharField(null=True)
    BJD= CharField(null=True)
    HJD_CODE= IntegerField(null=True)
    BJD_CODE = IntegerField(null=True)

    class Meta:
        database = db_server.psql_db

def table_create():

    # db_server.db_connect()

    db_server.table_create(Inter_code)

def table_drop():

    # db_server.db_connect()

    db_server.table_drop(Inter_code)

def insert_interest():

    # db_server.db_connect()
    with open("C:\\yang\\BJD_0\\INTER_CODE.csv") as data_file:
        reader = list(csv.reader(data_file, delimiter=',', quotechar='"'))
        reader.remove(reader[0])
        for row in reader:
            Inter_code.insert(SIGUNGU=row[0], HJD=row[2], BJD=row[3],
                              HJD_CODE=int(str(row[5])[:len(str(row[5])) - 2]), BJD_CODE=row[6]).execute()

def loader():
    code_list = []

    for i in Inter_code.select().tuples():
        code_list.append(i)

    return code_list

