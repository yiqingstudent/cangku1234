#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : 444.py
@Author: rebecca
@Date  : 2020/9/8 11:51
@Desc  : 
"""
# s = input("input:")
# print(len(s.split(' ')[-1]))

# s = input("")
# a = input("")
# count = s.lower().replace(' ', '').count(a.lower())
# print(count)

# str = 'hello every body'
# result= {}
# for i in str:
#     result[i] = str.count(i)
# print(result)
from random import randint

# list = []
# # for i in range(1000):
# #     s = randint(1, 1000)
# #     list.append(s)
# # list_new = sorted(set(list))
# # print(list_new)
# # print(len(list_new))

# a = input()
# list = []
# for i in range(int(a)):
#     s = input()
#     list.append(int(s))
#
# list_new = sorted(set(list))
# for j in list_new:
#     print(j)
#
#
# while True:
#     try:
#         n=int(input())
#         arr=[]
#         for i in range(n):
#             arr.append(int(input()))
#         setA=set(arr)
#         for i in sorted(setA):
#             print(i)
#     except:
#         break
# No.3:连续输入字符串(输入2次,每个字符串长度小于100)
# # 输出到长度为8的新字符串数组
# str = 'abcdedghijklmn'
# print(str[:3]) # step=1，从左往右取值，从“起点”开始一直取到end_index=3。
# print(str[1:2:1])


# a = []
# for i in range(2):
#     a.append(input())
# print(a)
# for s in a:
#     while len(s) > 8:
#         print(s[:8])
#         s = s[8:]
#
#     if len(s) <= 8:
#         print(s + '0'*(8 - len(s)))

# 输入一个十六进制的数值字符串。输出该数值的十进制字符串。 int,bin,oct,hex
"""
bin():（十进制转换二进制）
oct()（十进制转换到八进制）
hex()（十进制转换到十六进制）
int()（其他进制转换到十进制）

"""
# ten = 18
# sixteen = hex(ten)
# print("二进制为：", bin(ten))
# print("八进制为：", oct(ten))
# print("十六进制为：", hex(ten))
# print("进制为：", int('0xA', base=16))
# print(eval(sixteen))


# while True:
#     try:
#         str1 = input()
#         print(int(str1, base=16))
#     except:
#         break
# """
# 质子取数规则
# """
# x = int(input())
# y = 2
# z = []
# while x != y:
#     if x % y == 0:
#         z.append(y)
#         x = x/y
#     else:
#         y += 1
# z.append(int(x))
# for i in z:
#     print(i, end=" ")

# print("NI是张三")
# print("你是王二麻子")
# print("你是李四")
#
# print("NI是张三", end=" ")
# print("你是王二麻子", end=" ")  # 不换行，直接加个空格即可
# print("你是李四", end=" ")
#
# print(7/3)
# print(7%4) #取余数

# a = float(input())
# print(int(a+0.5))
# 数据表记录包含表索引和数值（int范围的整数），
# 请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
# num = input()
# dict = {}
# for i in range(int(num)):
#     ab = input().split(" ")
#     a, b = int(ab[0]), int(ab[1])
#     if a not in dict.keys():
#         dict[a] = b
#     else:
#         dict[a]=dict[a]+b
#
# for k,y in sorted(dict.items()):
#     print(k, y)




# dict = {'a': 1, 'b': 2, 'c': '3'}
# if 1 in dict.values():
#     print("hello")
# else:
#     print("error")

# """
# 题目描述
# 输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
# """
#
# # reversed()函数是返回序列seq的反向访问的迭代子。参数可以是列表，元组，字符串，不改变原对象。
# num = input()
# list_01 = list(reversed(num))
# result = []
# for i in list_01:
#     if i not in result:
#         result.append(i)
#     else:
#         pass
# print(result)
# print("".join(result))  # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
#
# s = '222234325435'
# s1 = s[::-1]
# result = []
# for i in s1:
#     if i not in result:
#         result.append(i)
# print("".join(result))

# str = 'hello world'
# result = set(list(str))
# count = 0
# for i in result:
#     if ord(i) >0 and ord(i) <= 127:
#         count += 1
#     else:
#         pass
# print(count)

# a = input()
# for i in list(a)[::-1]:
#     print("".join(i),end="")

# string = "i am a boy"
# print(string.split(" ")[::-1])
# print(" ".join(string.split(" ")[::-1]))

# while True:
#     try:
#         a = input()
#         list=[]
#         for i in range(int(a)):
#             list.append(input())
#         list.sort()
#         for j in list:
#             print(j)
#     except:
#         break


# # a = int(input())
# count = 0
# for i in bin(12345):
#     if '1' in i:
#         print(type(i))
#         count +=1
# print(count)
#
#
# print(1 in 1)























