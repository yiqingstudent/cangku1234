#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : organization_code_check.py
@Author: rebecca
@Date  : 2020/4/24 13:47
@Desc  : 
"""
import string
# 用数字与大写字母拼接成code_map，每个字符的index就是代表该字符的值
code_map = string.digits + string.ascii_uppercase
# 加权因子列表
WMap = [3, 7, 9, 10, 5, 8, 4, 2]

def get_c9(bref):
    # C9=11-MOD（∑Ci(i=1→8)×Wi,11）
    # 通过本地计算出C9的值
    sum = 0
    for ind, i in enumerate(bref):
        Ci = code_map.index(i)
        Wi = WMap[ind]
        sum += Ci * Wi

    C9 = 11 - (sum % 11)
    if C9 == 10:
        C9 = 'X'
    elif C9 == 11:
        C9 = '0'
    return str(C9)


def check_organizationcode(code):
    # 输入组织机构代码进行判断，如果正确，则输出'验证通过，组织机构代码证格式正确！'，错误则返回错误原因
    ERROR = '组织机构代码证错误!'
    if '-' in code:
        bref, C9_check = code.split('-')
    else:
        bref = code[:-1]
        C9_check = code[-1:]

    if len(bref) != 8 or len(C9_check) != 1:
        return ERROR + '（本体或校验码长度不符合要求）'
    else:
        try:
            C9_right = get_c9(bref)
        except ValueError:
            return ERROR + '(本体错误)'
        if C9_check != C9_right:
            return ERROR + '（校验码错误）'
        else:
            return '验证通过，组织机构代码证格式正确！'


if __name__ == '__main__':
    print(check_organizationcode('WV0X1KYT-X'))  # 正确
    print(check_organizationcode('WV0X1KYT5'))  # 正确
    print(check_organizationcode('WV0X1KYT-5')) # 校验码错误
    print(check_organizationcode('WV0X1K-5'))  # 本体长度太短
    print(check_organizationcode('WV0X1KYT-50')) # 校验码长度太长
    print(check_organizationcode('WV0X1KY@-5'))  # 本体中有特殊字符
