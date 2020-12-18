#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : test_wgdlc.py
@Author: rebecca
@Date  : 2020/5/29 15:16
@Desc  : 
"""
import logging
import unittest
from time import sleep

from selenium import webdriver
from TestDatas.Common_Datas import CommonDatas
from PageObjects.login_page import LoginPage
from PageObjects.wgdqxlc_page import WgdqxPage
from TestDatas import wgdlc_datas as wd


class TestEnterMain(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(CommonDatas.login_url_zjtj)
        LoginPage(self.driver).login(CommonDatas.zjtj_name, CommonDatas.zjtj_password)
        self.wgdlc = WgdqxPage(self.driver)

    def tearDown(self) -> None:
        # wind10会自动关闭的，但是我们还是要主动关闭
        # 多线程调用SW中关闭浏览器的最佳方式是使用close，这样就不会出现上述问题.chrome.quit();实际上去试图关闭所有的windows
        self.driver.quit()

    # 正常场景01-新增组织机构代码证的启用数据
    def test_add_success_01(self):
        logging.info("******正常场景01：新增固定理财登记成功******")
        self.wgdlc.click_menu()
        self.wgdlc.add_licai_name_data(wd.success_wgdlc_data["lc_name"], wd.success_wgdlc_data["money"], wd.success_wgdlc_data["remark"])
        # 开始断言
        self.assertEqual(self.wgdlc.get_message_from_save_success(),wd.success_wgdlc_data["check—info"])



