# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:05:53 2019

@author: Hp
"""

file= open('absentee.txt','at')
while True:
    absents=input("Enter the names of absent students max 25:")
    file.write(absents + "\n")
    if not absents:
        break
file.close()
with open('absentee.txt','rt')as rf:
    for line in rf:
        print(line)

         