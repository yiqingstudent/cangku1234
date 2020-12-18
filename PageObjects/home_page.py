#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : home_page.py
@Author: rebecca
@Date  : 2020/4/7 11:20
@Desc  : 
"""
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Common.basepage import BasePage
from PageLocators.home_page_loc import HomePageLoc as loc


class HomePage(BasePage):
    # 元素定位
    def check_user_exist(self):
        """
        如果退出元素存在，那么返回True，否则False
        :return:布尔值
        """
        return self.check_elements_exist(loc.loc_set, "主页面-检测登录用户名是否存在")






