#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : oracle.py
@Author: rebecca
@Date  : 2020/4/13 16:04
@Desc  : 
"""
import cx_Oracle as oracle
from ecdsa.test_pyecdsa import Util


class DataBaseManager(object):
    def __init__(self, conf):
        self.util = Util()
        self.conf = conf
        self.db_ip = conf.dbConf[u'ip']
        self.db_sid = conf.dbConf[u'sid']
        self.db_port = conf.dbConf[u'port']
        self.db = None
        self.cursor = None

    def connectDB(self, user):
        # 连接数据库方法，变量为数据库用户，密码，IP地址和数据库SID
        (username, password) = user.split(u'+')
        self.db = oracle.connect(username, password, self.db_ip + u':' + self.db_port + u'/' + self.db_sid)
        self.cursor = self.db.cursor()

    def commitDB(self):
        # 提交数据库操作
        self.db.commit()

    def closeDB(self):
        # 关闭数据库
        self.db.close()

    def executeSQLArray(self, user, sql):
        # 执行sql数组
        self.connectDB(user)
        for i in sql:
            self.cursor.execute(i)
        self.commitDB()
        self.closeDB()

    def executePreparedSQL(self, user, sql, params):
        # 执行带参数的sql
        self.connectDB(user)
        results = self.cursor.execute(sql, params)
        self.commitDB()
        self.closeDB()
        return results

    def queryPreparedSQL(self, user, sql, params):
        '''
        执行带参数的sql
        '''
        self.connectDB(user)
        self.cursor.execute(sql, params)
        results = self.cursor.fetchall()
        self.commitDB()
        self.closeDB()
        return results

    def executeBatchPreparedSQL(self, user, sql, params):
        '''
        执行批量的带参数的sql
        '''
        self.connectDB(user)
        self.cursor.prepare(sql)
        results = self.cursor.executemany(None, params)
        self.commitDB()
        self.closeDB()
        return results

    def getInsttuIdByName(self, insttuName):
        return self.findBySQL(self.conf.dbConf[u'公共管理平台'],
                              u"select insttu_id from pub_insttu where cname='" + insttuName + u"'")



    def findBySQL(self, user, sql):
        '''
                            通过sql寻找值，第一个参数为连接的数据库，第二个为sql
        '''
        self.connectDB(user)
        self.cursor.execute(sql)
        sqlItem = self.cursor.fetchone()
        self.closeDB()
        if  sqlItem != None:
            return sqlItem[0]
        else:
            return u''

    def executeSQL(self, user, sql):
        '''
                             执行sql
        '''
        self.connectDB(user)
        self.cursor.execute(sql)
        self.commitDB()
        self.closeDB()

username = 'ml_jnmf'
password = 'password'
ip = '172.31.19.96'
port = '1521'
sidname = 'ora10g'
db = oracle.connect('ml_jnmf/password@172.31.19.96:1521/ora10g')

cursor = db.cursor()
cursor.execute('select *from pub_sys_param')
datas = cursor.fetchall()
print(datas)
cursor.close()
db.close()
print(datas)
list = [data for data in datas]
print(list)
