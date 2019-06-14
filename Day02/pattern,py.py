# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:48:33 2019

@author: Hp
"""

def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print ("*",end=" ")
        print ("\r")
    for i in range(n,0,-1):
        for j in range(0,i-1):
            print ("*",end=" ")
        print ("\r")
        
n=int(input("enter n"))
pattern(n)