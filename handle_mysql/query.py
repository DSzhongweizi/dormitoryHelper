#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import  pymysql,json
from flask import  request,jsonify
def query_stuInfo(object):
    db = pymysql.connect("148.70.98.130", "root", "00544", "students", charset='utf8')
    cursor = db.cursor()
    if(object == 'bedmakerStatus'):
        addressID=request.form['addressID']
        sql = "SELECT * FROM stuInfo WHERE addressID='%s'" % addressID
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                if (row[8] == 1):
                    return "false"
                else:
                    pass
            db.close()
            return "true"
        except Exception as e:
            db.rollback()
            print(e.args)
            db.close()
            return "false"
    elif(object == 'noBackStu'):
        stuInfos=[]
        grade=request.form['grade']+'级'
        academy=request.form['academy']
        sql = "SELECT * FROM stuInfo WHERE backDormitoryStatus=0 AND grade='%s' AND academy='%s'"%(grade,academy)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                stuInfo = {}#局部变量的好处
                stuInfo.update(name=row[1])
                stuInfo.update(phone=row[4])
                stuInfos.append(stuInfo)
            db.close()
            return jsonify(tuple(stuInfos)),200,{"name": "name_and_phone"}
        except Exception as e:
            db.rollback()
            print(e.args)
            db.close()
            return "false"
    elif (object == 'stuInfo'):
        id=request.form['id']
        stuInfo={}
        sql = "SELECT * FROM stuInfo WHERE id=%s" % id
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            # stuInfos = [] # 局部变量的好处
            for row in results:
                # stuInfo = {}  # 局部变量的好处
                # global stuInfo
                stuInfo.update(id=row[0])
                stuInfo.update(name=row[1])
                stuInfo.update(grade=row[2])
                stuInfo.update(academy=row[3])
                stuInfo.update(phone=row[4])
                stuInfo.update(avatars=str(row[5], encoding="utf-8"))
                stuInfo.update(addressID=row[6])
                stuInfo.update(address=row[7])
                stuInfo.update(bedmakerStatus=row[8])
            db.close()
            if(len(stuInfo)>0):
                return json.dumps(stuInfo)
            else:
                return "false"
        except Exception as e:
            db.rollback()
            print(e.args)
            db.close()
            return "false"
    elif (object == 'historyRecord'):
        id=request.form['id']
        historyRecord={}
        sql = "SELECT * FROM stuInfo WHERE id=%s" % id
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            # stuInfos = [] # 局部变量的好处
            for row in results:
                # stuInfo = {}  # 局部变量的好处
                historyRecord.update(historyRecord=row[10])
            db.close()
            if(len(historyRecord['historyRecord'])>0):
                return json.dumps(historyRecord)
            else:
                return "false"
        except Exception as e:
            db.rollback()
            print(e.args)
            db.close()
            return "false"
def query_teaInfo(object):
    db = pymysql.connect("148.70.98.130", "root", "00544", "teachers", charset='utf8')
    cursor = db.cursor()
    if(object == 'teaInfo'):
        id=request.form['id']
        sql = "SELECT * FROM teachers WHERE id=%s" % id
        teaInfo={}
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                teaInfo.update(id=str(row[0], encoding="utf-8"))
                teaInfo.update(grade=str(row[1], encoding="utf-8"))
                teaInfo.update(academy=str(row[2], encoding="utf-8"))
                teaInfo.update(enclosure=str(row[3], encoding="utf-8"))
            db.close()
            return json.dumps(teaInfo)
        except Exception as e:
            db.rollback()
            print(e.args)
            db.close()
            return "false"
def query_image(object):
    db = pymysql.connect("148.70.98.130", "root", "00544", "images", charset='utf8')
    cursor = db.cursor()
    if(object =='dormitoryImage'):
        addressID=request.form['addressID']
        sql = "SELECT * FROM dorImg WHERE addressID=%s" % addressID
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            images={}
            for row in results:
                # byte转str
                images.update(imgA=str(row[1], encoding="utf-8"))
                images.update(imgB=str(row[2], encoding="utf-8"))
                images.update(imgC=str(row[3], encoding="utf-8"))
                images.update(imgLivingRoom=str(row[4], encoding="utf-8"))
                images.update(imgToilet=str(row[5], encoding="utf-8"))
            db.close()
            return json.dumps(images)
        except Exception as e:
            db.rollback()
            print(e.args)
            db.close()
            return  "false"
    elif (object == 'historyRecord'):
        historyRecords = []
        grade = request.form['grade'] + '级'
        academy = request.form['academy']
        sql = "SELECT * FROM stuInfo WHERE  grade='%s' AND academy='%s'" % (grade, academy)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                historyRecord = {}  # 局部变量的好处
                historyRecord.update(name=row[0])
                historyRecord.update(checkNum=row[6])
                historyRecord.update(supportNum=row[7])
                historyRecords.append(historyRecord)
            db.close()
            return jsonify(tuple(historyRecords)), 200, {"name": "name_and_phone"}
        except Exception as e:
            db.rollback()
            print(e.args)
            db.close()
            return "false"
