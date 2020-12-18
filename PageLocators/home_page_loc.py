#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : home_page_loc.py
@Author: rebecca
@Date  : 2020/4/17 10:07
@Desc  : 
"""
from selenium.webdriver.common.by import By


class HomePageLoc:
    # 元素定位-退出按钮
    loc_set = (By.XPATH, '//a[text()="退出"]')
