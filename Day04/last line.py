# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:50:31 2019

@author: Hp
"""

file = open('romeo.txt','rt')
content=file.readlines()
print(content[-1])