#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import  pymysql
from flask import  request
#更新学生信息
def update_stuInfo(object,enclosure):
    db = pymysql.connect("148.70.98.130", "root", "00544", "students", charset='utf8')
    cursor = db.cursor()
    id = request.form['id']
    if  (object == 'bedmakerStatus'):
        bedmakerStatus=request.form['bedmakerStatus']
        sql = "UPDATE %s" % enclosure+" SET bedmakerStatus=%s  WHERE id=%s" % (bedmakerStatus,id)
    elif(object == 'phone'):
        phone=request.form['phone']
        sql = "UPDATE %s" % enclosure+ " SET phone=%s WHERE id=%s" % (phone, id)
    elif(object == 'dormitory'):
        dormitory=request.form['dormitory']
        sql = "UPDATE %s" % enclosure + " SET dormitory=%s WHERE id=%s" % (dormitory, id)
    elif (object == 'openid'):
        session_key=request.form['session_key']
        openid = request.form['openid']
        sql = "UPDATE %s" % enclosure + " SET session_key='%s',openid='%s' WHERE id='%s'" % (session_key, openid, id)
    return assistFun(db,cursor,sql)
#更新老师信息
def update_teacherInfo(object):
    db = pymysql.connect("148.70.98.130", "root", "00544", "teachers", charset='utf8')
    cursor = db.cursor()
    id = request.form['id']
    if(object == 'grade'):
        grade=request.form['grade']
        sql = "UPDATE teachers SET phone=%s WHERE id=%s" % (grade,id)
    elif(object =='academy'):
        academy = request.form['academy']
        sql = "UPDATE teachers SET phone=%s WHERE id=%s" % (academy, id)
    elif(object =='enclosure'):
        enclosure = request.form['enclosure']
        sql = "UPDATE teachers SET phone=%s WHERE id=%s" % (enclosure, id)
    return assistFun(db, cursor, sql)
#更新寝室图片信息
def update_image(object,enclosure):
    db = pymysql.connect("148.70.98.130", "root", "00544", "images", charset='utf8')
    cursor = db.cursor()
    unit_dormitory = request.form['unit_dormitory']
    if (object == 'dorImg'):
        base64 = request.form['base64']
        obj = request.form['obj']
        sql = "UPDATE %s" % enclosure + " SET %s" % ('img' + obj) + "='%s' WHERE unit_dormitory='%s'" %(base64, unit_dormitory)
    elif(object =='supportNum'):
        sql = "UPDATE %s" % enclosure + " SET supportNumber=supportNumber+1 WHERE unit_dormitory='%s'" %unit_dormitory
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
