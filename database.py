import mysql.connector
from mysql.connector import Error
import os

host = os.environ['host']
database = os.environ['database']
user = os.environ['user']
pass_w = os.environ['pass']


print(host)
try:
  connection = mysql.connector.connect(
    host=host,
    database=database,
    user=user,
    password=pass_w)
  if connection.is_connected():

    cursor = connection.cursor()

    query = ("SELECT * FROM jobs;")
    cursor.execute(query)
except Error as e:
  print("Error while connecting to MySQL", e)
# finally:
#   if connection.is_connected():
#     cursor.close()
#     connection.close()
#     print("MySQL connection is closed")
