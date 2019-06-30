#!/usr/bin/python3
import mysql.connector as mysql

# RDS info
u='Enter master username of RDS'
p='Enter password'

db='adhoc'
h='Enter host'

# now connecting

conn=mysql.connect(user=u,password=p,database=db,host=h)
# now generating a sql language cursor
cur=conn.cursor()

# now we can write sql query
cur.execute("show tables;")


# now printing result
print(cur.fetchall())

# closing connection
conn.close()
