
import mysql.connector
__cnx = None


def get_sql_connections():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='root',  host='127.0.0.1', database='parlor')
    return __cnx
