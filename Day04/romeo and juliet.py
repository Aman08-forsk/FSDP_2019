# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:29:34 2019

@author: Hp
"""
file= open('romeo.txt','rt')
lines=file.readlines()
print(lines)
file.close()
    
file1=open('romeo.txt','rt')
fill=file1.read().split()
count={}
for i in fill:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(str(count))
file.close()

