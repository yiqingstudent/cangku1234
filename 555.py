#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : 555.py
@Author: rebecca
@Date  : 2020/9/13 21:00
@Desc  : 
"""
import heapq
#
# string1 = input()
# upper_list = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J',
#                 'K','L','Z','X','C','V','B','N','M']
# lower_list = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j',
#                 'k','l','z','x','c','v','b','n','m']
# list=[]
# for i in string1:
#     i_asc = ord(i)
#     if i_asc>=65 and i_asc<91:
#         new_num = upper_list[i_asc-65]
#     elif i_asc>96 and i_asc<123:
#         new_num = lower_list[i_asc-97]
#     elif i_asc == 32:
#         new_num = ' '
#     else:
#         pass
#     list.append(new_num)
# # print(list)
# for j in list:
#     print(" ".join(j), end="")

list = [1,3,4,5,666,77,67,78,888,8999]
print(heapq.nsmallest(3,list))
print(heapq.nlargest(4,list))

print(min(list))
print(max(34234, 234234))
print(max('34234'))
print(max({"a":3, "b":'56'}))


nums = [2, 3, 5, 1, 54, 23, 132]
heap = []
for num in nums:
    heapq.heappush(heap, num)  # 加入堆

print("堆栈第一个:", heap[0])  # 如果只是想获取最小值而不是弹出，使用heap[0]
print("堆栈:", heap)  # 如果只是想获取最小值而不是弹出，使用heap[0]

