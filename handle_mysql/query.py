#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import  pymysql,json
from flask import  request
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
            if(row[9]==1):
                return "false"
            else:
                pass
        db.close()
        return "true"
    except Exception as e:
        db.rollback()
        print(e.args)
        db.close()
        return  "false"
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
