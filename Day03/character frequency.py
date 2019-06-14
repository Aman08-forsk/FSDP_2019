# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:36:29 2019

@author: Hp
"""
freq={}
string=input("enter the string:")
for i in string:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print("count of all characters in string is" + str(freq))