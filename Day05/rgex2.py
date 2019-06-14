# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:04:32 2019

@author: Hp
"""

import re
str3=[]
while True:
    user=input("Enter the strings:")
    str3.append(user)
    if not user:
        break
str1=[]
str2=[]
for i in str3:
    if re.search(r'^[a-z0-9_-]+\@[a-z0-9]+\.[a-z]{2,4}$',i):
        str1.append(i)
    else:
        str2.append(i)
print("sorted vlaid id are :")
print(sorted(str1))