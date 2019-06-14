# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:16:24 2019

@author: Hp
"""
import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']


  #  for i in range(len(names)):
   #     names[i] = random.choice(code_names)

    #print (names)
rand=map(lambda i: random.choice(code_names),names)
print(list(rand))