#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : 111.py
@Author: rebecca
@Date  : 2020/4/27 16:51
@Desc  : 可以当作自定义的模块，文件
"""
#
# sys = {'name': '张三',
#        'age': '十八',
#        'gender': 'man'}
# print(sys.values())
# #  单独打印出排序后的key值
# sys_sorted = sorted(sys)
# print(sys_sorted)
#
# print(sys['name'])
# """
# """
#
# # 打印排序后的value值
# # 根据key的升序排列，把key value都打印出来
# print(sys.items())
# news = sorted(sys.items(), key=lambda d: d[0], reverse=False)
# print(news)
#
#
# # 单独打印出排序后的value值
# new_sys1 = sorted(sys.values())
# print(new_sys1)
#
# news = sorted(sys.items(), key=lambda d: d[1], reverse=False)
# print(news)


# import datetime
# from dateutil.relativedelta import *
#
# time = "2014-05-19"
# time = datetime.datetime.strptime(time, "%Y-%m-%d")
# time_new = time + datetime.timedelta()  # 直接加天数的
# print(time)
#
# time1 = time + relativedelta(months=+30)
# print(time1)
#
# time2 = time + datetime.timedelta(30)
# print(time2)
# #
#
# test_info = {'check—info': '56', 'password': '34', 'user_name': 'J3205823010050'}
# a = test_info['check—info']
# b = test_info["password"]
#
#
# def sum(a, b):
#     print(a+"fff"+b)
#
# sum(a,b)

# from faker import Faker
# fake = Faker(locale='zh_CN')
# # 地址类
# print("地址类".center(20, "-"))
# print(fake.address())  # 完整地址，比如海南省成市丰都深圳路p座 425541
# print(fake.street_address())  # 街道+地址，比如兴城路A座
# print(fake.street_name())  # 街道名，比如宜都街
# print(fake.city_name(), fake.city())  # 城市名,比如兰州 城市,比如兰州市
# print(fake.province())  # 省份名,比如陕西省
# # 公司类：
# print("公司类".center(20, "-"))
# print(fake.company())  # 公司名:惠派国际公司信息有限公司
# print(fake.company_suffix())  # 公司名后缀(公司性质)，比如网络有限公司
# print(fake.company_prefix())  # 公司名前缀，比如鑫博腾飞
# # 个人信息类
# print("个人信息类".center(20, "-"))
# print(fake.name())  # 姓名
# print(fake.simple_profile())  # 简略个人信息，包括用户名，姓名，性别，地址，邮箱，出生日期
# print(fake.user_name(), fake.password(special_chars=False))
# print(fake.profile(fields=None, sex=None))  # 详略个人信息，比简略个人信息多出公司名、血型、工作、位置、域名等等信息。
# print(fake.job())  # 工作
# # 文章类
# print("文章类".center(20, "-"))
# print(fake.word())  # 随机词语
# print(fake.words(3))  # 随机多个词语，nb是数量，对于words来说是返回多少个词语
# print(fake.sentence(3))  # 随机短语（会包括短语结束标志点号）
# print(fake.paragraph())  # 随机段落
# # 日期类
# print(fake.date(pattern="%Y-%m-%d", end_datetime=None))
# print(fake.year())  # 随机年份
# print(fake.day_of_week())  # 随机星期数
# print(fake.time(pattern="%H:%M:%S", end_datetime=None))  # 随机时间
#
# # 数据类型类
# print(fake.pystr(min_chars=None, max_chars=20))  # 自定义长度的随机字符串
# print(fake.pyint())  # :随机整数

# result = 0
# for i in range(2,101,2):
#     result = result + i
# print(result)

# for i in range(1,10):
#     if i==5:
#         break
#     print(i)

# func = lambda x,y:x+y
# print(func(3,6))
#
# list1 = [27, 4, 5, 6, 7]
# list1.append(2)
# print(list1)
# list1.sort()
#
# print(list1)
#
#
# list1.insert(1, 22)
# print(list1)
#
# list1.remove(2)
# print(list1)
#
# print(list1.pop(1))
#
# print(list1)
#
# list1.reverse()
# print(list1)

# list1.sort(reverse=True)
# print(list1)
# list1 = []
# for i in range(4):
#     list1.append(i**2)
# print(list1)

# list1 = [i**2 for i in range(1, 4) if i != 1]
# print("list1:", list1)

#
# list1 = []
# for i in range(1, 4):
#     if i!=1:
#         list1.append(i**2)
# print(list1)
#
# list4 = []
# for i in range(1,4):
#     for j in range(1,4):
#         list4.append(i*j)
# print(list4)

# list4 = [i*j for i in range(1, 4) for j in range(1, 4)]
# print(list4)

# tuple_hi = (1,2,3)
# # # print(type(tuple_hi))
# # #
# # # print(tuple_hi.count(2))

# a = {1,3,4}
# c = {1,2,3}
# print(a.union(c))
# print(a.intersection(c))
# print(a.difference(c))
# a.add(99)
# print(a)

# print({i for i in "adasdakjfsjdfhsjdfd"})
#
# c = "akdhsadjakjdad"
# print(set(c))
#
# print({i:i*2 for i in range(1,5)})

import os
# # os.mkdir("testdir")
# list1 = os.listdir("./")
# print(os.listdir("./"))
# print(list1)
#
# print(os.getcwd())
#
# print(os.path.exists("testdir"))
# if os.path.exists("testdir"):
#     os.removedirs("testdir")  # OSError: [WinError 145] 目录不是空的。: 'testdir'
#
# if not os.path.exists("testdir"):
#     os.mkdir("testdir")
# if not os.path.exists("testdir/test0819.txt"):
#     f = open("testdir/test0819.txt","w")
#     f.write("hello,test os!!!")
#     f.close()
# print(os.path.exists("testdir"))
# if  os.path.exists("testdir"):
#    print("hello world")

# print(time.asctime())  # 国外的时间格式，国内一般不用
# print(time.time())  # 1597890444.194442  1597890771.9167297
# print(time.localtime()) # 元组的形式
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
#
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# import time
# now = time.time()
# print(now)
# new_time = now - 60*60*24*2
# print(new_time)
# time_tuple = time.localtime(new_time)
# print(time_tuple)
# print(time.strftime("%Y-%m-%d %H:%M:%S", time_tuple))
# import urllib.request
# res = urllib.request.urlopen("https://www.baidu.com")
# print(res.status)
# print(res.read().decode('utf-8'))
# print(res.headers)

# import copy
#
# alist = ['a', 'b', 'c']
# b = alist
# c = copy.copy(alist)
# d = copy.deepcopy(alist)  # 深度拷贝, a 和 b 完全拷贝了父对象及其子对象，两者是完全独立的。
# alist.append(5)
# print(alist)
# print(b)
# print(c)
# print(d)
#
# print(id(alist))
# print(id(b))
# print(id(c))
# print(id(d))
# import logging
# import time
# import _thread
# logging.basicConfig(level=logging.INFO)
#
#
# def loop0():
#     logging.info("start loop0 at" + time.ctime())
#     time.sleep(4)
#     logging.info("end loop0 at "+ time.ctime())
#
#
# def loop1():
#     logging.info("start loop1 at" + time.ctime())
#     time.sleep(3)
#     logging.info("end loop1 at " + time.ctime())
#
#
# def main():
#     logging.info("start all at" + time.ctime())
#
#     _thread.start_new_thread(loop0,())
#     _thread.start_new_thread(loop1,())
#     time.sleep(7)
#     logging.info("end all at " + time.ctime())
#
#
# if __name__ == '__main__':
#     main()


# def func(a, b, x):
#     if ( a > 1 and b==0 ):
#         x = x/a
#     if (a==2 or x > 1):
#         x = x + 1
#     return x
#
#
# print(func(3, 0, 4))

import cx_Oracle
# def diff_content(list1,list2):
#     diff_tmp = []
#     for i in list1:
#         if i in list2:
#             pass
#         else:
#             diff_tmp.append(i)
#     return diff_tmp
#
#
conn_01 = cx_Oracle.connect('pub_plat/password@172.31.19.96:1521/ora10g', encoding='utf-8')
sql = 'SELECT * FROM PUB_SYSPARAM'  # sql语句
curs_01 = conn_01.cursor() # 方法打开语句要使用的游标(返回连接的游标对象)
curs_01.execute(sql)
rows_01 = curs_01.fetchall()
rows_01_01 = curs_01.fetchone()
print(rows_01_01)
#
# conn_02 = cx_Oracle.connect('pub_plat/password@172.31.19.72:1521/ora10g', encoding='utf-8')
# sql = 'SELECT * FROM PUB_SYSPARAM'  # sql语句
# curs_02 = conn_02.cursor()  # 方法打开语句要使用的游标(返回连接的游标对象)
# curs_02.execute(sql)
# rows_02 = curs_02.fetchall()
#
# print(rows_01)
# print(type(rows_01))
#
# print(rows_02)
# #
# a = [x[0] for x in rows_01 if x in rows_02]  # 两个列表中都存在
# print("a的返回结果为：",a)
# print("相同的结果为：", sorted(a))
# b = [y[0] for y in (rows_01 + rows_02) if y not in a]  # 两个列表中的不同元素
# print("b的返回结果为：", b)
# print("不同的结果为：", sorted(b))

# a = [822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 833, 834, 510, 512, 513, 855, 837, 838, 846, 847, 848, 849, 850, 851, 852, 853, 854, 835, 836, 845, 839, 840, 841, 842, 843, 844, 10, 9, 2, 3, 4, 5, 6, 7, 12, 8, 15, 13, 14, 16, 500, 501, 502, 20, 503, 22, 23, 24, 505, 506, 508, 509, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867]
#
# b = [868, 869, 870, 871, 872, 874, 875, 876, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 833, 834, 510, 511, 512,
#      513, 855, 837, 838, 846, 847, 848, 849, 850, 851, 852, 853, 854, 835, 836, 845, 839, 840, 841, 842, 843, 844, 1, 10,
#      9, 2, 3, 4, 5, 6, 7, 12, 8, 15, 13, 14, 16, 500, 501, 502, 20, 503, 22, 23, 24, 25, 504, 505, 506, 507, 508, 509,
#      800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 856,
#      857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 877, 878, 873, 881, 880, 861, 862, 863, 864, 865, 876, 877,
#      878, 866, 867, 885, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 833, 834, 510, 511, 512, 513, 855, 837, 838,
#      846, 847, 848, 849, 850, 851, 852, 853, 854, 835, 836, 845, 839, 840, 841, 842, 843, 844,
#      1, 10, 9, 2, 3, 4, 5, 6,
#      7, 12, 8, 15, 13, 14, 16, 500, 501, 502, 20, 503, 22, 23, 24, 25, 504, 505, 506,
#      507, 508, 509, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812,
#      813, 814, 815, 816, 817, 818, 819, 820, 821, 856, 857, 858, 859, 860, 890, 891,
#      892, 893, 894, 886, 887, 888, 889]
#
# c = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 12, 12, 13, 13, 14, 14,
#       15, 15, 16, 16, 20, 20, 22, 22, 23, 23, 24, 24, 25, 25, 500, 500, 501, 501, 502, 502,
#       503, 503, 504, 504, 505, 505, 506, 506, 507, 507, 508, 508, 509, 509,
#       510, 510, 511, 511, 512, 512, 513, 513, 800, 800, 801, 801, 802, 802,
#       803, 803, 804, 804, 805, 805, 806, 806, 807, 807, 808, 808, 809, 809,
#       810, 810, 811, 811, 812, 812, 813, 813, 814, 814, 815, 815, 816, 816,
#       817, 817, 818, 818, 819, 819, 820, 820, 821, 821, 822, 822, 823, 823,
#       824, 824, 825, 825, 826, 826, 827, 827, 828, 828, 829, 829, 830, 830,
#       831, 831, 833, 833, 834, 834, 835, 835, 836, 836, 837, 837, 838, 838,
#       839, 839, 840, 840, 841, 841, 842, 842, 843, 843, 844, 844, 845, 845,
#       846, 846, 847, 847, 848, 848, 849, 849, 850, 850, 851, 851, 852, 852,
#       853, 853, 854, 854, 855, 855, 856, 856, 857, 857, 858, 858, 859, 859,
#       860, 860, 861, 861, 862, 862, 863, 863, 864, 864, 865, 865, 866, 866,
#       867, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 876, 877, 877,
# #       878, 878, 880, 881, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894]
# # print(set(c))
#
# l1 = [1,2,3]
# l2 = [3,4,5]
# l1.append(4)
# print(l1)
# l1.append(l2)
# print(l1)

