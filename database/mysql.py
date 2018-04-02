

import pymysql

# define the credentials and database details
HOSTNAME = 'localhost'
USER = 'root'
PW = ''
TABLE = 'test_table'
DB = 'test'

insert_queries = []

# establish connection
conn = pymysql.connect(host=HOSTNAME, user=USER, password=PW, db=DB)


def create_tbl_stmt():
    return "create table if not exists {0}" \
           "(id int(20) NOT NULL AUTO_INCREMENT PRIMARY KEY, name varchar(20), " \
"address varchar(20), position varchar(20), salary float(20));".format(TABLE)


def create_table():
    print(create_tbl_stmt())

    with conn.cursor() as cursor:
        cursor.execute(create_tbl_stmt())