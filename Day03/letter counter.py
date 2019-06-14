# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:48:25 2019

@author: Hp
"""

dict={'letters':0,'digits':0}
string=input("enter the string:")
for i in string:
    if i in "qwertyuioplkjhgfdsazxcvbnm":
        dict['letters']+=1
    else:
        dict['digits']+=1
print("number of letters andn digits in string are:" +  str(dict))
    