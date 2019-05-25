#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from  flask import  request
import  requests,json

def getOpenID():
    code=request.form['code']
    url='https://api.weixin.qq.com/sns/jscode2session?appid=wx78cc956434e73454&secret=9775b04149ae610d1292b99ff14904f2&js_code='+code+'&grant_type=authorization_code'
    response=requests.get(url=url)
    print(response.json())
    return json.dumps(response.json())