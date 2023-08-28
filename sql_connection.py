import datetime
import mysql.connector

__cnx = None

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
    __cnx  = mysql.connector.connect(
        host='containers-us-west-136.railway.app',
        user='root',
        password='ODQdfkMDBAdqParIUm9d',
        database='store'
    )

  return __cnx

