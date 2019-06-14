# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:28:33 2019

@author: Hp
"""




import requests

url1 = "https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=2f149528bfa6e0b2b144"


print (url1)

response = requests.get(url1)
# requests.get(url,params={"q":"Jaipur", "appid"="e9185b28e9969fb7a300801eb026de9c"})
response.content