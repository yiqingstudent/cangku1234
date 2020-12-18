#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : login_page_loc.py
@Author: rebecca
@Date  : 2020/4/13 11:08
@Desc  : 
"""
from selenium.webdriver.common.by import By


class LoginPageLoc:
    # 元素定位-用户名
    loc_username = (By.ID, 'username')
    # 元素定位-密码
    loc_password = (By.ID, 'pswd')
    # 登录按钮
    loc_login = (By.XPATH, '//div[@class="txt7"]')
    #  错误提示框
    loc_error = (By.XPATH, '//div[@class="txt5"]')
