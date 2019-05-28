#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import  pymysql
from flask import  request
#更新学生信息
def update_stuInfo(object):
    db = pymysql.connect("148.70.98.130", "root", "00544", "students", charset='utf8')
    cursor = db.cursor()
    id = request.form['id']
    if  (object == 'bedmakerStatus'):
        bedmakerStatus=request.form['bedmakerStatus']
        sql = "UPDATE stuInfo SET bedmakerStatus=%s  WHERE id=%s" % (bedmakerStatus,id)
    elif(object == 'phone'):
        phone=request.form['phone']
        sql = "UPDATE stuInfo SET phone=%s WHERE id=%s" % (phone, id)
    elif(object == 'dormitory'):
        dormitory=request.form['dormitory']
        sql = "UPDATE stuInfo SET dormitory=%s WHERE id=%s" % (dormitory, id)
    elif (object == 'address'):
        address = request.form['address']
        sql = "UPDATE stuInfo SET address='%s' WHERE id=%s" % (address, id)
    elif (object == 'addressID'):
        addressID = request.form['addressID']
        print(addressID)
        sql = "UPDATE stuInfo SET addressID=%s WHERE id=%s" % (addressID, id)
    elif (object == 'historyRecord'):
        historyRecord = request.form['historyRecord']
        print(historyRecord)
        print("---------------------")
        sql = "UPDATE stuInfo SET historyRecord='%s' WHERE id=%s" % (historyRecord, id)
    elif (object == 'openid'):
        session_key=request.form['session_key']
        openid = request.form['openid']
        sql = "UPDATE stuInfo SET session_key='%s',openid='%s' WHERE id='%s'" % (session_key, openid, id)
    return assistFun(db,cursor,sql)
#更新老师信息
def update_teacherInfo(object):
    db = pymysql.connect("148.70.98.130", "root", "00544", "teachers", charset='utf8')
    cursor = db.cursor()
    id = request.form['id']
    grade = request.form['grade']
    academy = request.form['academy']
    enclosure = request.form['enclosure']
    sql = "UPDATE teachers SET grade='%s',academy='%s',enclosure='%s' WHERE id=%s" % (grade,academy,enclosure,id)
    return assistFun(db, cursor, sql)
#更新寝室图片信息
def update_image(object):
    db = pymysql.connect("148.70.98.130", "root", "00544", "images", charset='utf8')
    cursor = db.cursor()
    addressID = request.form['addressID']
    if (object == 'dorImg'):
        base64 = request.form['base64']
        obj = request.form['obj']
        sql = "UPDATE dorImg SET %s" % ('img' + obj) + "='%s' WHERE addressID='%s'" %(base64, addressID)
    elif(object =='supportNum'):
        sql = "UPDATE dorImg SET supportNumber=supportNumber+1 WHERE addressID='%s'" %addressID
    elif (object == 'checkNum'):
        sql = "UPDATE dorImg SET checkNumber=checkNumber+1 WHERE addressID='%s'" % addressID
    return assistFun(db,cursor,sql)
# 辅助函数
def assistFun(db,cursor,sql):
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        return "true"
    except Exception as e:
        db.rollback()
        print(e.args)
        db.close()
        return  "false"
