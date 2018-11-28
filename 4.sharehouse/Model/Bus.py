# -*- coding: utf-8 -*-
from peewee import *
from Db_Server import db_server
import csv

class Bus(Model):
    STOP_CODE = CharField(null=True) # IntegerField(null=True) 숫자인데 코드 앞에 0이 있어서 캐릭터로 함
    STOP_NAME = CharField(null=True)
    LONG = DoubleField(null=True)
    LAT = DoubleField(null=True)

    class Meta:
        database = db_server.psql_db  # This model uses the "people.db" database.

def table_create():
    # db_server.db_connect()

    db_server.table_create(Bus)
# table_create()
def table_drop():
    # db_server.db_connect()

    db_server.table_drop(Bus)
# table_drop()

def insert_interest():

    with open("C:\\yang\\bus\\BUS.csv") as data_file:
        reader = list(csv.reader(data_file, delimiter=',', quotechar='"'))
        reader.remove(reader[0])
        cnt = 0
        for row in reader:
            Bus.insert(STOP_CODE=row[0], STOP_NAME=row[1], LONG=row[2], LAT=row[3]).execute()
# insert_interest()
def loader():
    bus_list = []

    for i in Bus.select().tuples():
        bus_list.append(i)

    return bus_list