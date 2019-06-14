# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:44:35 2019

@author: Hp
"""


import json
import requests

Host = "https://en5ibhuuti1nk.x.pipedream.net"

data = {"firstname":"dev","language":"English"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )


