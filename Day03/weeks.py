# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:46:07 2019

@author: Hp
"""
c=0
input_string=input("Enter the days:")
list1=input_string.split(",")
print(list1)
for i in list1:
    c+=1
if c==7:
    print("all days present")
else:
    w=7-c
    print(str(w)+"days are missing")
        
