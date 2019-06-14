# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 13:18:13 2019

@author: Hp
"""

import re
#n= int(input("enter the numbers of card number:"))
card=[]
while True:
    s=input("Enter the card numbers:")
    if not s:
        break
    card.append(s)
print(card)

for i in card:
    valid_num = re.match(r'^[456](\d{15}|\d{3}\-(\d{4}\-){2}\d{4})$',i)
    con_num = re.search(r'(\d)\1{3,}',i.replace("-",""))
    if valid_num and not con_num:
        print("Valid")
    else:
        print("Invalid")

