# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:31:53 2019

@author: Hp
"""

def Leap_Year(year):
    if year%400==0 or year%4==0 and year%100!=0:
        print ("leap year")
    else:
        print ("not leap year")
            
year=int(input("enter year"))
Leap_Year(year)