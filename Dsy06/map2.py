# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:52:15 2019

@author: Hp
"""


#      names = ['Mary', 'Isla', 'Sam']
#
 #   for i in range(len(names)):
  #      names[i] = hash(names[i])

   # print (names)\
names = ['Mary', 'Isla', 'Sam']
hashing=map(lambda i:hash(i),names)
print (list(hashing))