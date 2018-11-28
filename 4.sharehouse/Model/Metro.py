# -*- coding: utf-8 -*-
from peewee import *
from Db_Server import db_server
import csv

class Metro(Model):
    # 순번 = IntegerField(null=True)
    STA = CharField(null=True)
    STA_CODE = IntegerField(null=True)
    LINE = CharField(null=True)
    ADDRESS = CharField(null=True)
    LAT = DoubleField(null=True)
    LONG = DoubleField(null=True)

    class Meta:
        database = db_server.psql_db  # This model uses the "people.db" database.


def table_create():
    # db_server.db_connect()

    db_server.table_create(Metro)

def table_drop():
    # db_server.db_connect()

    db_server.table_drop(Metro)


def insert_interest():

    with open("d:\\ob\\aaa.csv") as data_file:
        reader = list(csv.reader(data_file, delimiter=',', quotechar='"'))
        reader.remove(reader[0])

        for row in reader:
            Metro.insert(STA=row[0], STA_CODE=row[1], LINE=row[2], ADDRESS=row[3], LAT=row[4], LONG=row[5]).execute()

def loader():
    metro_list = []

    for i in Metro.select().tuples():
        metro_list.append(i)

    return metro_list

