#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import  requests,json
def add_user(stuInfo,enclosure,access_token):
    url='https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add?access_token='+access_token
    data={
        'user_id':stuInfo['id'],
        'group_id':'stu_'+enclosure,
        'image_type':'BASE64',
        'image':stuInfo['img'],
        'user_info':stuInfo['name']
    }
    response=requests.post(url=url,data=data)
    return json.dumps(response.json())
