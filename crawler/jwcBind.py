#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from  flask import  request
import  requests
#登录
def jwc_bind(object):
    login_url = 'http://zhjw.scu.edu.cn/login/j_spring_security_check'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6821.400 QQBrowser/10.3.3040.400'
    }
    user_data = {
        'j_username': request.form['j_username'],
        'j_password': request.form['j_password'],
        'j_captcha': request.form['j_captcha']
    }
    s = requests.session()  # 创建一个session对象
    response = s.post(url=login_url, headers=headers, data=user_data)  # 设置cookie
    cookies = requests.utils.dict_from_cookiejar(s.cookies)
    return s