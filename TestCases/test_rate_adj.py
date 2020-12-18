#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : test_rate_adj.py
@Author: rebecca
@Date  : 2020/4/2 17:05
@Desc  : 
"""
import logging
import unittest
from selenium import webdriver
from TestDatas.Common_Datas import CommonDatas
from PageObjects.login_page import LoginPage
from PageObjects.rateadj_page import RateAdjPage


class TestRateAdj(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(CommonDatas.login_url)
        LoginPage(self.driver).login(CommonDatas.user_name, CommonDatas.password)
        self.rateajd = RateAdjPage(self.driver)

    def tearDown(self) -> None:
        # wind10会自动关闭的，但是我们还是要主动关闭
        # 多线程调用SW中关闭浏览器的最佳方式是使用close，这样就不会出现上述问题.chrome.quit();实际上去试图关闭所有的windows
        self.driver.quit()

    # 正常场景01
    def test_rate_adj_success_01(self):
        logging.info("******正常场景01：当期生效，输入生效日期，然后输入年利率，月利率会自动生成******")
        # 当期生效的测试案例
        # 进入菜单：利率调增
        self.rateajd.click_menu()
        self.rateajd.query_loan()
        self.rateajd.add_request()
        self.rateajd.input_data('25', True, '2014-05-15')
        # 开始断言
        self.assertEqual(self.rateajd.get_message_from_save(), "保存成功！")

    def test_rate_adj_success_02(self):
        # 下期生效的测试案例
        # 进入菜单：利率调增
        self.rateajd.click_menu()
        self.rateajd.query_loan()
        self.rateajd.add_request()
        self.rateajd.input_data('25', False)
        # 开始断言
        self.assertEqual(self.rateajd.get_message_from_save(), "保存成功！")
        self.rateajd.save_submit()

    # 正常场景03
    def test_rateadj_failed(self):
        """
        1、登录网址
        2、输入用户名和密码，点击登录按钮
        3、断言
        :return:
        """
        pass
