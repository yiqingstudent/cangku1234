#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : login_datas.py
@Author: rebecca
@Date  : 2020/4/2 11:25
@Desc  : 
"""
# 成功用例-数据
from TestDatas.Common_Datas import CommonDatas


class LoginDatas:
    success_data = {"user_name": "J3205823010050", "password": "123123", "check_url": CommonDatas.home_url}

    # 错误用例-数据
    wrong_datas = [
        {"user_name": "J3205823010050", "password": "345556", "check—info": "抱歉:用户名或密码不正确"},
        {"user_name": "hello", "password": "123123", "check—info": "抱歉:用户名或密码不正确"},
        {"user_name": "J3205823010050", "password": "3455", "check—info": "提示:密码输入格式错误"},
        {"user_name": "J3205823010050", "password": "", "check—info": "提示:用户名或密码是空"},
        {"user_name": " ", "password": "123123", "check—info": "提示:用户名或密码是空"}
    ]
