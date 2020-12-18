#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : 333.py
@Author: rebecca
@Date  : 2020/9/8 11:18
@Desc  :
"""
import logging
from logging.handlers import RotatingFileHandler
import time
import datetime
import cx_Oracle
fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'

handler_1 = logging.StreamHandler()

curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())
# 设置 rootlogger 的输出内容形式，输出渠道
logging.basicConfig(format=fmt,datefmt=datefmt,level=logging.INFO,handlers=[handler_1])

conn_01 = cx_Oracle.connect('afdz_jnmf/password@172.31.19.72:1521/ora10g', encoding='utf-8')
curs_01 = conn_01.cursor() # 方法打开语句要使用的游标(返回连接的游标对象)
sql_01 = "select *  from PUB_FEE_PARAM t where t.org_typ='02'"  # 老机构sql语句1
sql_02 = "select *  from PUB_FEE_PARAM t where t.org_typ='93'"  # 老机构sql语句1

curs_01.execute(sql_01)
list1 = curs_01.fetchall()

print("02类型的所有old记录为：", list1)
print("********************开始对02类型的所有的old记录进行修改********************")
# 对02的文件进行修改：
list_tuple = []
for i in list1:
    new_list = list(i)
    new_list[1] = '93'
    list_tuple.append(tuple(new_list))
print("02的修改之后的列表为：", list_tuple)

curs_01.execute(sql_02)
list2 = curs_01.fetchall()
print("93的所有查询结果为：", list2)
curs_01.close()
conn_01.commit()
conn_01.close()

set1 = set(list_tuple)
set2 = set(list2)
iset = set1.intersection(set2)
if set1 ^ set2 == set():
    print("********************新旧数据比对完全一致！********************")
else:
    print("********************新旧数据比对！********************")
print("两个列表相同的地方为：", iset)
print("取交集：", set1 & set2)
print("取并集：", set1 | set2)
print("取并集：", set1.union(set2))
print("取差集s1中有，s2中无：", set1-set2)  # set1中有的，但是set2中是没有的
print("取差集s1中有，s2中无：", set1.difference(set2))  # set1中有的，但是set2中是没有的
print("取差集s2中有，s1中无：", set2-set1)  # set2中有的，但是set1中是没有的
print("取对称差集：", set1 ^ set2)  # 取s2, s3 中不同时存在的元素
print(set1.symmetric_difference(set2))  # 对称差集，就是把两个集合中相同的去掉










# a = [x for x in rows_01 if x in rows_02]  # 两个列表中都存在
# print("a的返回结果为：",a)
# print("相同的结果为：", sorted(a))
# b = [y for y in (rows_01 + rows_02) if y not in a]  # 两个列表中的不同元素
# print("b的返回结果为：", b)
# print("不同的结果为：", sorted(b))

#
# conn = cx_Oracle.connect('afdz_jnmf/password@172.31.19.72:1521/ora10g', encoding='utf-8')
# curs = conn.cursor() # 方法打开语句要使用的游标(返回连接的游标对象)
# f = open('table.sql')
# full_sql = f.read()
# sql_commands = full_sql.split(';')
#
#
# for sql_command in sql_commands:
#     print("sql命令为：", sql_command)
#     curs.execute(sql_command)
#     row = curs.fetchall()
#     print("返回结果为：", row)
#

# print(row_01[0])
#
# for i in range(len(row_01)):
#     for j in range(len(row_02)):
#         if row_01[i] == row_02[j]:
#             print("yes")
#             print("i:",i)
#             print("j:",j)
#             print("\n")
#         else:
#             print("no")
#             print("s:", i)
#             print("h:", j)


list1 = [1,21,'a1','b1',5,67,78,99,"ji"]

list2 = [1,"a","b",2,87,34,67,"ji",89]
set1 = set(list1)
set2 = set(list2)
iset = set1.intersection(set2)
print("两个列表相同的地方为：",iset)



#
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if list1[i] == list2[j]:#元素相等时
#             print("yes")
#             print("i:",i)
#             print("j:",j)
#             print("\n")
#
#         elif list1[i] != list2[j]:#元素不相等时
#             print("no")
#             print("s:",i)
#             print("h:",j)
#
# for i in range(len(list1)):
#     print(i)
#     if list1[i]==list2[i]:
#         print(f"相等元素值为",list1[i])

