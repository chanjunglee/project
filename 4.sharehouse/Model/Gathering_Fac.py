# -*- coding: utf-8 -*-
from peewee import *
from Db_Server import db_server
import csv

class Gathering_fac(Model):
    # 순번 = IntegerField(null=True)
    G_TYPE = CharField(null=True)
    GU = CharField(null=True)
    BJD =  CharField(null=True)
    LONG= DoubleField(null=True)
    LAT = DoubleField(null=True)
    G_NAME = CharField(null=True)
    class Meta:
        database = db_server.psql_db  # This model uses the "people.db" database.

def table_create():
    # db_server.db_connect()

    db_server.table_create(Gathering_fac)

def table_drop():
    # db_server.db_connect()

    db_server.table_drop(Gathering_fac)

def insert_interest():

    with open("C:\\yang\\gathering_fac_0\\GATHERING_F.csv") as data_file:
        reader = list(csv.reader(data_file, delimiter=',', quotechar='"'))
        reader.remove(reader[0])
        for row in reader:
            Gathering_fac.insert(G_TYPE=row[0], GU=row[1], BJD=row[2], LONG=row[3], LAT=row[4], G_NAME=row[5]).execute()

def loader():
    fac_list = []

    for i in Gathering_fac.select().tuples():
        fac_list.append(i)

    return fac_list