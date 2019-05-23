#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask,request
import config
import json
from crawler import login, getInfo
from handle_mysql import insert,delete,update,query
from handle_baidu_FaceIdentity import addUser,getAccessToken,identifyFace
app = Flask(__name__)
app.config.from_object(config)

stuInfo={}
# 登录接口
@app.route("/dormitoryHelper/api/v1.0/login/<object>", methods=['GET', 'POST'])
def Login(object):
    global stuInfo
    if(object == 'teacher'):
        return login.jwc_login(object)
    elif(object == 'student'):
        s=login.jwc_login(object) # 获取登录cookie
        stuInfo=getInfo.get_stuInfo(s)# 获取学生学籍信息
        return  stuInfo# 返回数据给前端
#人脸识别操作
@app.route("/dormitoryHelper/api/v1.0/face_recognition/<object>", methods=['GET', 'POST'])
def faceRecognition(object):
    global stuInfo
    access_token=getAccessToken.get_access_token()
    enclosure=request.form['enclosure']
    if(object == 'add_user'):
        return addUser.add_user(json.loads(stuInfo[0]),enclosure,access_token)
    elif(object == 'identify_face'):
        base64=request.form['img']
        id = request.form['id']
        enclosure=enclosure[0:1]
        return identifyFace.identify(id, base64, enclosure, access_token)
# 插入接口
@app.route("/dormitoryHelper/api/v1.0/insert/<database>/<object>", methods=['GET', 'POST'])
def Insert(database,object):
    global stuInfo
    if(database == 'students'):
        return insert.insert_stuInfo(json.loads(stuInfo[0]),object)  # 数据库操作
    elif(database =='teachers'):
        return insert.insert_teaInfo(object)
# 删除接口
# @app.route("/dormitoryHelper/api/v1.0/delete/<object>/<info>/<keyMysql>", methods=['GET', 'POST'])
# def Delete(object,info,enclosure):
#     if(object == 'bedmaker'):
#         return delete.delete_bedmaker(json.loads(info),enclosure)  # 数据库操作
# # 更新接口
@app.route("/dormitoryHelper/api/v1.0/update/<database>/<object>", methods=['GET', 'POST'])
def Update(database,object):
    enclosure=request.form['enclosure']
    if(database == 'students'):
        return update.update_stuInfo(object,enclosure)
    elif(database =='teachers'):
        return update.update_teacherInfo(object)
    elif(database == 'images'):
        return update.update_image(object,enclosure)

# 查询接口
@app.route("/dormitoryHelper/api/v1.0/query/<database>/<object>", methods=['GET', 'POST'])
def Query(database,object):
    enclosure = request.form['enclosure']
    if (database == 'students'):
        return query.query_stuInfo(object, enclosure)
    elif(database == 'teachers'):
        return query.query_teaInfo(object)
    elif (database == 'images'):
        return query.query_image(object, enclosure)
if __name__ == '__main__':
    app.run()
