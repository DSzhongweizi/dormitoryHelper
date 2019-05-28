#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import  requests
def identify(id,stuImage,enclosure,access_token):
    url='https://aip.baidubce.com/rest/2.0/face/v3/search?access_token='+access_token
    data={
        'user_id':id,
        'image_type':'BASE64',
        'image':stuImage,
        'group_id_list':'stu_'+enclosure,
    }
    response=requests.post(url=url,data=data)
    if(response.json()['result']['user_list'][0]['score']>=75):
        return response.json()['result']['user_list'][0]['user_info']
    else:
        return  "false"