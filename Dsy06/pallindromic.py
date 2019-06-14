# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:41:54 2019

@author: Hp
"""
user=input("enter the numbers:").split(',')
print (user)
pallindrome=[True if i==i[::-1] else False for i in user]
print (any(pallindrome))