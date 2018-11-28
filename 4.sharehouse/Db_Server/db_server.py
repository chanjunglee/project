# -*- coding: utf-8 -*-
from peewee import *

# psql_db = PostgresqlDatabase('shk_bigdata',  # Required by Peewee.
#                              user='bigdata',  # Will be passed directly to psycopg2.
#                              password='bigdata',  # Ditto.
#                              host='sharekim.com')

psql_db = PostgresqlDatabase('peewee_db',  # Required by Peewee.
                             user='postgres',  # Will be passed directly to psycopg2.
                             password='dlckswnd',  # Ditto.
                             host='localhost')

def db_connect():

    psql_db.connect()

def table_create(table):

    psql_db.create_tables([table])

def table_drop(table):

    psql_db.drop_tables([table])

