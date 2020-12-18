#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : wgdlc_datas.py
@Author: rebecca
@Date  : 2020/5/29 15:17
@Desc  : 
"""
from Common.create_number import CreateNumber
from TestDatas.Common_Datas import CommonDatas

success_wgdlc_data = {"lc_name": "理财名称哈哈哈哈哈", "money": "5555", "remark": "你好啊如下", "check—info": "操作成功！"}

# 错误用例-数据
wrong_wgdlc_datas = [
    {"user_name": "J3205823010050", "password": "345556", "check—info": "抱歉:用户名或密码不正确"},
    {"user_name": "hello", "password": "123123", "check—info": "抱歉:用户名或密码不正确"},
    {"user_name": "J3205823010050", "password": "3455", "check—info": "提示:密码输入格式错误"},
    {"user_name": "J3205823010050", "password": "", "check—info": "提示:用户名或密码是空"},
    {"user_name": " ", "password": "123123", "check—info": "提示:用户名或密码是空"}
]
