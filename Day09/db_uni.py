# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:09:36 2019

@author: Hp
"""

import sqlite3
from pandas import DataFrame

conn=sqlite3.connect("db_university")
c=conn.cursor()

#c.execute("""DROP TABLE db_university""")

c.execute("""CREATE TABLE db_university(
        Student_Name TEXT,
        Student_Age INTEGER,
        Student_Roll_no INTEGER,
        Student_Branch TEXT)""")

c.execute("INSERT INTO db_university VALUES ('aman', 21, 014, 'cs')")
c.execute("INSERT INTO db_university VALUES ('ritika', 19, 126, 'commerce')")
c.execute("INSERT INTO db_university VALUES ('appu', 21, 027, 'ME')")
c.execute("INSERT INTO db_university VALUES ('akki', 18, 001, 'cs')")
c.execute("INSERT INTO db_university VALUES ('aditi', 20, 007, 'cs')")
c.execute("INSERT INTO db_university VALUES ('ambuj', 21, 018, 'cs')")
c.execute("INSERT INTO db_university VALUES ('shiv', 21, 198, 'cs')")
c.execute("INSERT INTO db_university VALUES ('kritik', 21, 215, 'me')")
c.execute("INSERT INTO db_university VALUES ('yash', 20, 167, 'cs')")
c.execute("INSERT INTO db_university VALUES ('milan', 21, 200, 'cs')")

c.execute("SELECT * FROM db_university")
print ( c.fetchall() )

c.execute("SELECT * FROM db_university")
df=DataFrame(c.fetchall())
df.columns = ["Student_Name","Student_Age","Student_Roll_no","Student_Branch"]

conn.commit()
conn.close()


