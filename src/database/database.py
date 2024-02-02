import pymysql
from pymysql import DatabaseError
from decouple import config

def db_connection():
    return pymysql.connect(
        host = config('MYSQL_HOST'),
        user = config('MYSQL_USER'),
        password = config('MYSQL_PASSWORD'),
        database = config('MYSQL_DATABASE')
    )