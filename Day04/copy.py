# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:23:26 2019

@author: Hp
"""

with open('words.txt','rt') as rf:
    with open('new.txt','wt') as wf:
        for i in rf:
            wf.write(i)
with open('new.txt','rt')as rf:
    for line in rf:
        print(line)
        
