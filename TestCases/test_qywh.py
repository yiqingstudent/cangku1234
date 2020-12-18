#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : test_qywh.py
@Author: rebecca
@Date  : 2020/4/24 11:07
@Desc  : 
"""
import logging
import unittest
from time import sleep

from selenium import webdriver
from TestDatas.Common_Datas import CommonDatas
from TestDatas import qywh_datas as qd
from PageObjects.login_page import LoginPage
from PageObjects.qywh_page import EnterpriseMain


class TestEnterMain(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(CommonDatas.login_url)
        LoginPage(self.driver).login(CommonDatas.administrator_name, CommonDatas.administrator_password)
        self.qywh = EnterpriseMain(self.driver)

    def tearDown(self) -> None:
        # wind10会自动关闭的，但是我们还是要主动关闭
        # 多线程调用SW中关闭浏览器的最佳方式是使用close，这样就不会出现上述问题.chrome.quit();实际上去试图关闭所有的windows
        self.driver.quit()

    # 正常场景01-新增组织机构代码证的启用数据
    def test_add_success_01(self):
        logging.info("******正常场景01：默认输入组织机构代码证，默认启用状态******")
        self.qywh.click_menu()
        self.qywh.add_input_data(qd.success_org_data["qy_name"], qd.success_org_data["org_code"], "备注-哈哈")
        # 开始断言
        # self.assertEqual(self.qywh.get_message_from_please_sure(), "请确认是否保存!")
        self.assertEqual(self.qywh.get_message_from_save_success(), "保存成功！")

    def test_add_success_02(self):
        logging.info("******正常场景02：默认输入统一社会信用代码证，默认启用状态******")
        self.qywh.click_menu()
        self.qywh.add_input_data(qd.success_social_data["qy_name"], qd.success_social_data["social_code"], '备注哈哈', 'Y')
        # 开始断言
        # self.assertEqual(self.qywh.get_message_from_please_sure(), "请确认是否保存!")
        self.assertEqual(self.qywh.get_message_from_save_success(), "保存成功！")

    # 正常场景03-查询出想要的结果
    def test_query_success_03(self):
        logging.info("******正常场景03：查询成功******")
        self.qywh.click_menu()
        self.qywh.query_loan("测试-核心企业20200424")
        sleep(1)
        # 重点
        # 对比数据库数据与列表数据
        self.assertIn('47411155-4', self.qywh.get_value_from_query())


