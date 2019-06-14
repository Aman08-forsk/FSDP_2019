# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:11:10 2019

@author: Hp
"""

student_list = []

while True:
    user_input = input("Enter name, age and score:")
    
    if not user_input:
        break
    
name, age, marks = user_input.split(",")
    
student_list.append( (name, int(age), int(marks) ) )

student_list.sort()
print (student_list)
