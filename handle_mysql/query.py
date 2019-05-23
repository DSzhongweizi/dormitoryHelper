#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import  pymysql,json
from flask import  request,jsonify
def query_stuInfo(object,enclosure):
    db = pymysql.connect("148.70.98.130", "root", "00544", "students", charset='utf8')
    cursor = db.cursor()
    if(object == 'bedmaker'):
        dormitory=request.form['dormitory']
        sql = "SELECT * FROM %s"%enclosure+" WHERE dormitory=%s" % dormitory
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                if (row[9] == 1):
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
        sql = "SELECT * FROM %s" % enclosure + " WHERE backDormitoryStatus=0 AND grade='%s' AND academy='%s'"%(grade,academy)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()

            for row in results:
                stuInfo = {}#局部变量的好处
                stuInfo.update(name=row[1])
                stuInfo.update(phone=row[7])
                stuInfos.append(stuInfo)
            db.close()
            return jsonify(tuple(stuInfos)),200,{"name": "name_and_phone"}
        except Exception as e:
            db.rollback()
            print(e.args)
            db.close()
            return "false"
def query_teaInfo(object,enclosure):
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
def query_image(object,enclosure):
    db = pymysql.connect("148.70.98.130", "root", "00544", "images", charset='utf8')
    cursor = db.cursor()
    if(object =='dormitoryImage'):
        unit_dormitory=request.form['unit_dormitory']
        sql = "SELECT * FROM %s"%enclosure+" WHERE unit_dormitory=%s" % unit_dormitory
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
