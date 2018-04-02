# Question 4
# Write a simple employee management program. It should have common features
# like getting input about details of employees and storing those details to database
# and file. Implement a loop to get the input till the user wants.



import pymysql

# define the credentials and database details
HOSTNAME = 'localhost'
USER = 'root'
PW = 'root'
TABLE = 'employee'
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