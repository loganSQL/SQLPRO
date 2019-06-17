# with standard error handling

import mysql.connector
from mysql.connector import Error

config = {
  'user': 'testuser',
  'password': 'testuser',
  'host': '172.16.40.143',
  'port':'3306',
  'database': 'logandb',
  'raise_on_warnings': True
}
cnx = cnx = mysql.connector.connect(**config)

try:
 #   cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    query = ("SELECT version() AS version, SUBSTRING_INDEX(USER(), '@', -1) AS ip,  @@hostname as hostname, @@port as port, DATABASE() as current_database, user() as user;")
    cursor.execute(query)
    records = cursor.fetchall()
    for row in records:
        print("version = ", row[0], )
        print("ip = ", row[1], )
        print("hostname = ", row[2], )
        print("port = ", row[3], )
        print("current_database = ", row[4])
        print("user = ", row[5], )
    cursor.close()
   
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(cnx.is_connected()):
        cnx.close()
        print("MySQL connection is closed")