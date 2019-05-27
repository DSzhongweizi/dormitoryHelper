#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import  pymysql
from flask import request
#上传数据库
def insert_stuInfo(stuInfo,object):
    # 打开数据库连接
    db = pymysql.connect("148.70.98.130", "root", "00544", "students", charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    if(object =='stuInfo'):
        # SQL 插入语句(id, name, academy, grade, major, class, campus, phone, address)
        sql = "INSERT INTO stuInfo VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s','%s','%s', '%s', '%s', '%s','%s','%s','%s','%s')"%\
                (stuInfo['id'],stuInfo['name'],stuInfo['grade'],stuInfo['academy'],"","",stuInfo['avatars'],"","",
                0, 0,stuInfo['major'],stuInfo['class'],stuInfo['campus'],"","")
    return assistFun(db, cursor, sql)
def insert_teaInfo(object):
    db = pymysql.connect("148.70.98.130", "root", "00544", "teachers", charset='utf8')
    cursor = db.cursor()
    if(object =='teaInfo'):
        id = request.form['id']
        grade = request.form['grade']
        academy = request.form['academy']
        enclosure = request.form['enclosure']
        sql = "INSERT INTO teachers VALUES('%s', '%s', '%s','%s')"%(id,grade,academy,enclosure)
    return assistFun(db, cursor, sql)
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
        return  "flase"