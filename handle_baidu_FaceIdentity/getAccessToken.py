#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import  requests
def get_access_token():
    url ='https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=hqoGjSrOnMwvugxma4GmLNXm&client_secret=tAnVE29OHgcKp4PiTfwaYf5glTbSVQNN'
    # header={
    #     'Content-Type': 'application/json'
    # }
    response = requests.post(url=url)
    return  response.json()['access_token']