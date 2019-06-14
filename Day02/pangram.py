# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:11:10 2019

@author: Hp
"""

input_string = input("Enter the string :")
count = 0
list = []
lower = input_string.lower()
for alpha in lower:
    list.append(alpha)

final_list = []    

for num in list: 
 if num not in final_list: 
  final_list.append(num) 
    
for elements in final_list:
    if elements in 'abcdefghijklmnopqrstuvwxyz':
        count += 1
if count == 26:
    print ("Pangram")
else:
    print ("Not Pangram")
    