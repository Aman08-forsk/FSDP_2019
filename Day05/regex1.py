# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:44:09 2019

@author: Hp
"""

import re
n=int(input("Enter the numbers:"))
for i in range(n):
    s=input("Enter the input:")
    print(bool(re.search(r'^[-+.]?[0-9]*\.[0-9]+$',s)))