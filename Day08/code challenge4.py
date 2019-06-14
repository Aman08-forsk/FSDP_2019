# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 13:16:53 2019

@author: Hp
"""


from bs4 import BeautifulSoup
import requests
cricketodi = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi" 
source = requests.get(cricketodi).text

soup = BeautifulSoup(source,"lxml")

print (soup.prettify())

right_table=soup.find('table', class_='table')

print (right_table.prettify())

A=[]
B=[]
C=[]
D=[]
E=[]
for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())


from collections import OrderedDict

col_name = ["position","teams","matches","points","rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))


import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("iccodi.csv")

import sqlite3
from pandas import DataFrame

conn = sqlite3.connect ( 'iccodi.db' )
c = conn.cursor()
#c.execute("DROP TABLE iccodi;" )
c.execute ("""CREATE TABLE iccodi(
          positions INTEGER,
          teams  TEXT,
          matches INTEGER,
          points INTEGER,
          rating INTEGER
          )""")

for i in range(0,len(A)):
    c.execute("INSERT INTO iccodi VALUES('{}','{}','{}','{}','{}')".format(A[i],B[i],C[i],D[i],E[i]))
    
df = DataFrame(c.fetchall())
c.execute("SELECT * FROM iccodi")
df.columns=["positions","teams","matches", "points", "rating"]







