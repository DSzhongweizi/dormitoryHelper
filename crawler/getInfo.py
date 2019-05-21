#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json,base64,os
from bs4 import BeautifulSoup

def get_stuInfo(s):
    student_info = s.get('http://zhjw.scu.edu.cn/student/rollManagement/rollInfo/index')
    student_info = BeautifulSoup(student_info.content, 'html.parser')
    info = {}
    for msg in student_info.select('#left_layout > div > div:nth-child(5) > div.col-xs-8 > div:nth-child(2) > div'):
        info["id"] = msg.select(".profile-info-value")[0].text.strip()
        info["name"] = msg.select(".profile-info-value")[1].text.strip()
        info["grade"] = msg.select(".profile-info-value")[6].text.strip()
        info["academy"] = msg.select(".profile-info-value")[7].text.strip()
        info["major"] = msg.select(".profile-info-value")[8].text.strip()
        info["class"] = msg.select(".profile-info-value")[10].text.strip()
        info["campus"] = msg.select(".profile-info-value")[11].text.strip()

    stuImg = s.get('http://zhjw.scu.edu.cn/student/rollInfo/img')
    path = os.getcwd()
    with open(path + "\img.png", "wb") as f:  # 保存的文件名 保存的方式（wb 二进制  w 字符串）
        f.write(stuImg.content)
    f.close()
    with open(path + "\img.png", "rb") as f:  # 转为二进制格式
        base64_data = base64.b64encode(f.read())  # 使用base64进行加密
        # print(base64_data)
        # file = open('1.txt', 'wt')  # 写成文本格式
        # file.write(base64_data)
        # file.close()
        info['img'] = str(base64_data)[2:-3]#去掉前导二进制符号和最后面的两个等号，防止前端json.parse解析失败
    if(len(info)>0):
        return json.dumps(info,ensure_ascii=False),201
    else:
        return "登录失败,请检查账号密码是否正确"

