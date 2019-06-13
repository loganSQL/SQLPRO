from os import getenv
import pymssql

# This can use local envs
# Or using python config filr
#server = getenv("PYMSSQL_SERVER")
#user = getenv("PYMSSQL_USER")
#password = getenv("PYMSSQL_PASSWORD")

# pymssql_env.ps1
server='172.23.31.164'
user='sa'
password='Xmas2017'

conn = pymssql.connect(server, user, password, "tempdb")
# 1. create a table and inserts
cursor = conn.cursor()
cursor.execute("""
IF OBJECT_ID('persons', 'U') IS NOT NULL
    DROP TABLE persons
CREATE TABLE persons (
    id INT NOT NULL,
    name VARCHAR(100),
    salesrep VARCHAR(100),
    PRIMARY KEY(id)
)
""")
cursor.executemany(
    "INSERT INTO persons VALUES (%d, %s, %s)",
    [(1, 'John Smith', 'John Doe'),
     (2, 'Jane Doe', 'Joe Dog'),
     (3, 'Mike T.', 'Sarah H.')])
# you must call commit() to persist your data if you don't set autocommit to True
conn.commit()

# 2. Get one row
cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
row = cursor.fetchone()
while row:
    print("ID=%d, Name=%s" % (row[0], row[1]))
    row = cursor.fetchone()

# 3. Iterating through results
# Iterators are a pymssql extension to the DB-API.
cursor.execute('SELECT * FROM persons')
for row in cursor:
    print('row = %r' % (row,))

# 4. Important: A connection can have only one cursor with an active query at any time
c1 = conn.cursor()
c1.execute('SELECT * FROM persons')

c2 = conn.cursor()
c2.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')

print( "all persons" )
print( c1.fetchall() )  # shows result from c2 query!

print( "John Doe" )
print( c2.fetchall() )  # shows no results at all! (unexpect)

# 5 To walkaround, use a list variable
c1 = conn.cursor()
c1.execute('SELECT * FROM persons')
c1_list = c1.fetchall()

c2 = conn.cursor()
c2.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
c2_list = c2.fetchall()

print( "all persons from c1_list  " )
print( c1_list )  # shows result from c2 query!

print( "John Doe from c2_list" )
print( c2_list)  # shows no results at all! (unexpect)

# 6. Rows as dictionaries
cursor = conn.cursor(as_dict=True)
print( "Rows as dictionaries" )
cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
for row in cursor:
    print("ID=%d, Name=%s" % (row['id'], row['name']))

# 7. with statement (context managers)
print( "with statement (context managers)" )
with conn.cursor(as_dict=True) as cursor:
    cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
    for row in cursor:
        print("ID=%d, Name=%s" % (row['id'], row['name']))

# 8. Calling stored procedures
print( "Calling stored procedures" )
with conn.cursor(as_dict=True) as cursor:
    cursor.execute("""
    CREATE PROCEDURE FindPerson
        @name VARCHAR(100)
    AS BEGIN
        SELECT * FROM persons WHERE name = @name
    END
    """)
    cursor.callproc('FindPerson', ('Jane Doe',))
    for row in cursor:
        print("ID=%d, Name=%s" % (row['id'], row['name']))
conn.close()