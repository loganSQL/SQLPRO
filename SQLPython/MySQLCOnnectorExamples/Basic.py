# I am using MySQL docker
# testing from Windows WSL from another desktop
# https://github.com/loganSQL/SQLDocker/blob/master/mysql-linux-docker/MySQL_Linux_Docker_Note.md
# MySQL Connector from Oracle
# https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html
# pip install mysql-connector-python

import mysql.connector

config = {
  'user': 'testuser',
  'password': 'testuser',
  'host': '172.16.40.143',
  'port':'3306',
  'database': 'logandb',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
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
cnx.close()