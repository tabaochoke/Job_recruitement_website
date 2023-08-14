import mysql.connector
from mysql.connector import Error
import os

host = os.environ['host']
database = os.environ['database']
user = os.environ['user']
print(host)
try:
  connection = mysql.connector.connect(
    host=host,
    database=database,
    user=user,
    password='pscale_pw_uWGgz0ePGJAs8gG41PyxMd4effsi5Ndogu3K7NkFV2r')
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
