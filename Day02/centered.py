# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:11:10 2019

@author: Hp
"""

user_input = input("Enter comma seperated Numbers: ").split(",")

user_list = []

for i in user_input:
    user_list.append(int(i))

user_list.sort()

final_list = user_list[1:-1]

average = sum( final_list ) / len( final_list )

print ("Average is :", int( average ))
