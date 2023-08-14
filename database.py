import mysql.connector
from mysql.connector import Error

try:
  connection = mysql.connector.connect(
    host='aws.connect.psdb.cloud',
    database='website_test_db',
    user='3a90179ffah7xxq81do9',
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
