# -*- coding: utf-8 -*-
from peewee import *
from Db_Server import db_server
import csv

class Univ(Model):
    UNIV_NAME = CharField(null=True)
    ADDRESS = CharField(null=True)
    LAT = DoubleField(null=True)
    LONG = DoubleField(null=True)

    class Meta:
        database = db_server.psql_db  # This model uses the "people.db" database.


def table_create():
    # db_server.db_connect()

    db_server.table_create(Univ)


def table_drop():
    # db_server.db_connect()

    db_server.table_drop(Univ)


def insert_interest():
    with open("C:\\yang\\university\\UNIV.csv") as data_file:
        reader = list(csv.reader(data_file, delimiter=',', quotechar='"'))
        # reader.remove(reader[0])
        for row in reader:
            Univ.insert(UNIV_NAME=row[0], ADDRESS=row[1], LAT=row[2], LONG=row[3]).execute()


def loader():
    univ_list = []

    for i in Univ.select().tuples():
        univ_list.append(i)

    return univ_list