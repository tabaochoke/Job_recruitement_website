import mysql.connector
from mysql.connector import Error
import os

host = os.environ['host']
database = os.environ['database']
user = os.environ['user']
pass_w = os.environ['pass']

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
    JOBS = []
    for row in cursor:
      job = {}
      job['id'] = int(row[0]) - 1
      job['title'] = row[1]
      job['location'] = row[2]
      job['salary'] = row[3]
      job['repon'] = row[5]
      job['require'] = row[6]
      job['create'] = row[7]
      job['update'] = row[8]
      JOBS.append(job)

except Error as e:
  print("Error while connecting to MySQL", e)
finally:
  if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection is closed")



def insert_job (first_name, last_name, user_name, email, address, cv_url, country, state, zip) :
  try:
    connection = mysql.connector.connect(
    host=host,
    database=database,
    user=user,
    password=pass_w)
    if connection.is_connected():
      cursor = connection.cursor()
      query = ( """INSERT INTO application2
      (first_name, last_name, user_name, email, address, cv_url, country, state, zip)
 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""  )
      
      value = (first_name, last_name, user_name, email, address, cv_url, country, state, zip)
      cursor.execute(query , value)
      emp_no = cursor.lastrowid
      connection.commit ()
      print (query)
  except Error as e:
    print("Error while connecting to MySQL", e)

  cursor.close()
  connection.close()
  print("MySQL connection is closed")
# finally:
#   if connection.is_connected():
#     cursor.close()
#     connection.close()
#     print("MySQL connection is closed")
