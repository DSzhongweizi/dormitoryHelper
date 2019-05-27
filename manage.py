#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask,request
import config
import json
from crawler import jwcBind, getInfo
from handle_mysql import insert,delete,update,query
from handle_baidu_FaceIdentity import addUser,getAccessToken,identifyFace
from handle_weixin import login
app = Flask(__name__)
app.config.from_object(config)
stuInfo={}
# 绑定接口
@app.route("/dormitoryHelper/api/v1.0/school_bind/<object>", methods=['GET', 'POST'])
def schoolBind(object):
    global stuInfo
    if(object == 'teacher'):
        return jwcBind.jwc_bind(object)
    elif(object == 'student'):
        s = jwcBind.jwc_bind(object) # 获取登录cookie
        stuInfo = getInfo.get_stuInfo(s)# 获取学生学籍信息
        return  stuInfo# 返回数据给前端
# 登录接口
@app.route("/dormitoryHelper/api/v1.0/login/<object>", methods=['GET', 'POST'])
def Login(object):
    if(object == 'teacher'):
        pass
    elif(object == 'student'):
        return  login.getOpenID()
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
    elif(database =='images'):
        return insert.insert_imgInfo(object)
# 删除接口
# @app.route("/dormitoryHelper/api/v1.0/delete/<object>/<info>/<keyMysql>", methods=['GET', 'POST'])
# def Delete(object,info,enclosure):
#     if(object == 'bedmaker'):
#         return delete.delete_bedmaker(json.loads(info),enclosure)  # 数据库操作
# # 更新接口
@app.route("/dormitoryHelper/api/v1.0/update/<database>/<object>", methods=['GET', 'POST'])
def Update(database,object):
    if(database == 'students'):
        return update.update_stuInfo(object)
    elif(database =='teachers'):
        return update.update_teacherInfo(object)
    elif(database == 'images'):
        return update.update_image(object)

# 查询接口
@app.route("/dormitoryHelper/api/v1.0/query/<database>/<object>", methods=['GET', 'POST'])
def Query(database,object):
    if (database == 'students'):
        return query.query_stuInfo(object)
    elif(database == 'teachers'):
        return query.query_teaInfo(object)
    elif (database == 'images'):
        return query.query_image(object)
if __name__ == '__main__':
    app.run()
