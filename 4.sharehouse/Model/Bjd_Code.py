# -*- coding: utf-8 -*-
from peewee import *
from Db_Server import db_server
import csv

class Bjd_code(Model):
    # 순번 = IntegerField(null=True)
    SIGUNGU = CharField(null=True)
    BJD = CharField(null=True)
    BJD_CODE = IntegerField(primary_key=True)

    class Meta:
        database = db_server.psql_db

def table_create():
    # db_server.db_connect()

    db_server.table_create(Bjd_code)

def table_drop():
    # db_server.db_connect()

    db_server.table_drop(Bjd_code)

def insert_interest():

    with open("C:\\yang\\BJD_0\\BJD_CODE.csv") as data_file:
        reader = list(csv.reader(data_file, delimiter=',', quotechar='"'))
        reader.remove(reader[0])
        for row in reader:
            Bjd_code.insert(SIGUNGU=row[0], BJD=row[1], BJD_CODE=row[2]).execute()

def loader():

    bjd_list = []

    for i in Bjd_code.select().tuples():

        bjd_list.append(i)

    return bjd_list