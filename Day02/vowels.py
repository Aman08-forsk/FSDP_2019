# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:11:10 2019

@author: Hp
"""

state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']

vowels = list('aeiouAIEOU')

final_list = []

for name in state_name:
    temp_list = []
    for char in name:
        if char not in vowels:
            temp_list.append(char)
    final_list.append("".join(temp_list))

print (final_list)            


