#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : test_jhxd_apply.py
@Author: rebecca
@Date  : 2020/6/3 11:04
@Desc  : 
"""
import logging

import pytest

from Common import logger
import unittest
from time import sleep
from TestDatas import jhxd_datas as jd
from selenium import webdriver
from TestDatas.Common_Datas import CommonDatas
from PageObjects.login_page import LoginPage
from PageObjects.jhxd_page import JianHuaXdMain


class TestEnterMain(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(CommonDatas.login_url)
        LoginPage(self.driver).login(CommonDatas.user_name, CommonDatas.password)
        self.jhxd = JianHuaXdMain(self.driver)

    def tearDown(self) -> None:
        # wind10会自动关闭的，但是我们还是要主动关闭
        # 多线程调用SW中关闭浏览器的最佳方式是使用close，这样就不会出现上述问题.chrome.quit();实际上去试图关闭所有的windows
        self.driver.quit()

    # 正常场景01：等额本息-简化信贷-长期
    def test_add_success_01(self):
        logging.info("******正常场景01：新建客户--选择产品（简化信贷）--贷款申请--长期贷款--按揭类******")
        self.jhxd.click_menu()
        self.jhxd.add_cust_data(jd.success_customer_data[0]["cname"],
                                jd.success_customer_data[0]["paperNo"],
                                jd.success_customer_data[0]["phoneNo"])
        sleep(0.5)
        self.jhxd.enter_choose_product()
        sleep(1)
        # 进入简化信贷的保存页面
        self.jhxd.loan_apply_detail(25000, 24, "备注哈哈哈哈")
        # 开始断言
        self.assertEqual(self.jhxd.get_message_from_save_success(), "保存成功")
        sleep(1)
        self.jhxd.save_sure_submit()
        sleep(3)
        # 进入简化信贷--》调查录入页面--》贷款基本信息模块
        self.jhxd.loan_data_basic('20140115', '20160115', 1, 1, 2)
        # 进入简化信贷--》调查录入页面--》还款属性模块
        self.jhxd.loan_data_repayTyp(16, 22, 25, 1, 1, 1)
        # 进入简化信贷--》调查录入页面--》业务性质模块
        self.jhxd.loan_data_businessnature('是', '11312313123', '担保111111111', 'zfbw332432424', 1, 1, 2)
        # 进入简化信贷 - -》调查录入页面 - -》生成还款计划表
        self.jhxd.gen_reapy_sch()
        # 开始断言 贷款申请成功
        self.assertEqual(self.jhxd.get_message_from_loan_Save_success(), "请确认以上贷款信息，是否保存？")
        self.jhxd.save_success_click()
        # 开始断言
        self.assertTrue(self.jhxd.check_qianyue_exist())
        # 进入简化信贷--》签约页面,进行签约操作
        self.jhxd.contract_sign()

    # 正常场景02
    def test_add_success_02(self):
        logging.info("******正常场景02：新建客户--选择产品（简化信贷）--贷款申请--短期贷款--非按揭类******")
        self.jhxd.click_menu()
        sleep(1)
        self.jhxd.add_cust_data(jd.success_customer_data[1]["cname"],
                                jd.success_customer_data[1]["paperNo"],
                                jd.success_customer_data[1]["phoneNo"])
        self.jhxd.enter_choose_product()
        sleep(1)
        # 进入简化信贷的保存页面
        self.jhxd.loan_apply_detail(5000, 6, "备注哈哈哈哈")
        # 开始断言
        self.assertEqual(self.jhxd.get_message_from_save_success(), "保存成功")
        sleep(1)
        self.jhxd.save_sure_submit()
        sleep(3)
        # 进入简化信贷--》调查录入页面--》贷款基本信息模块
        self.jhxd.loan_data_basic('20140508', '20141108', 2, 2)
        # 进入简化信贷--》调查录入页面--》还款属性模块
        self.jhxd.loan_data_repayTyp(20, 8, 7, 3, 1, 1)
        # 进入简化信贷--》调查录入页面--》业务性质模块
        self.jhxd.loan_data_businessnature('是', '11312313123', '担保111111111', 'zfbw332432424', 1, 1, 2)
        # 进入简化信贷 - -》调查录入页面 - -》生成还款计划表
        self.jhxd.gen_reapy_sch()
        # 开始断言 贷款申请成功
        self.assertEqual(self.jhxd.get_message_from_loan_Save_success(), "请确认以上贷款信息，是否保存？")
        self.jhxd.save_success_click()
        # 开始断言
        self.assertTrue(self.jhxd.check_qianyue_exist())
        # 进入简化信贷--》签约页面,进行签约操作
        self.jhxd.contract_sign()

    # 正常场景03
    def test_add_success_03(self):
        logging.info("******正常场景03：个人客户--自营--起息期小于账务日期--短期贷款--非按揭类******")
        self.jhxd.click_menu()
        sleep(1)
        self.jhxd.add_cust_data(jd.success_customer_data[2]["cname"],
                                jd.success_customer_data[2]["paperNo"],
                                jd.success_customer_data[2]["phoneNo"])
        self.jhxd.enter_choose_product()
        sleep(1)
        # 进入简化信贷的保存页面
        self.jhxd.loan_apply_detail(500, 6, "备注哈哈哈哈")
        # 开始断言
        self.assertEqual(self.jhxd.get_message_from_save_success(), "保存成功")
        sleep(1)
        self.jhxd.save_sure_submit()
        sleep(3)
        # 进入简化信贷--》调查录入页面--》贷款基本信息模块
        self.jhxd.loan_data_basic('20140501', '20141101', 3, 3)
        # 进入简化信贷--》调查录入页面--》还款属性模块
        self.jhxd.loan_data_repayTyp(20, 8, 7, 3, 1, 1)
        # 进入简化信贷--》调查录入页面--》业务性质模块
        self.jhxd.loan_data_businessnature('是', '11312313123', '担保111111111', 'zfbw332432424', 1, 1, 2)
        # 进入简化信贷 - -》调查录入页面 - -》生成还款计划表
        self.jhxd.gen_reapy_sch()
        # 开始断言 贷款申请成功
        self.assertEqual(self.jhxd.get_message_from_loan_Save_success(), "请确认以上贷款信息，是否保存？")
        self.jhxd.save_success_click()
        # 开始断言
        self.assertTrue(self.jhxd.check_qianyue_exist())
        # 进入简化信贷--》签约页面,进行签约操作
        self.jhxd.contract_sign()

    # 正常场景04
    def test_add_success_04(self):
        logging.info("******正常场景04：个人客户--第三方--起息日小于账务日期--短期贷款--非按揭类******")
        self.jhxd.click_menu()
        sleep(1)
        self.jhxd.add_cust_data(jd.success_customer_data[3]["cname"],
                                jd.success_customer_data[3]["paperNo"],
                                jd.success_customer_data[3]["phoneNo"],
                                2)
        self.jhxd.enter_choose_product()
        sleep(1)
        # 进入简化信贷的保存页面
        self.jhxd.loan_apply_detail(561, 6, "备注哈哈哈哈")
        # 开始断言
        self.assertEqual(self.jhxd.get_message_from_save_success(), "保存成功")
        sleep(1)
        self.jhxd.save_sure_submit()
        sleep(3)
        # 进入简化信贷--》调查录入页面--》贷款基本信息模块
        self.jhxd.loan_data_basic('20140501', '20141001', 3, 3)
        # 进入简化信贷--》调查录入页面--》还款属性模块
        self.jhxd.loan_data_repayTyp(20, 8, 7, 3, 1, 1)
        # 进入简化信贷--》调查录入页面--》业务性质模块
        self.jhxd.loan_data_businessnature('是', '11312313123', '担保111111111', 'zfbw332432424', 1, 1, 2)
        # 进入简化信贷 - -》调查录入页面 - -》生成还款计划表
        self.jhxd.gen_reapy_sch()
        # 开始断言 贷款申请成功
        self.assertEqual(self.jhxd.get_message_from_loan_Save_success(), "请确认以上贷款信息，是否保存？")
        self.jhxd.save_success_click()
        # 开始断言
        self.assertTrue(self.jhxd.check_qianyue_exist())
        # 进入简化信贷--》签约页面,进行签约操作
        self.jhxd.contract_sign()

    # 正常场景05
    def test_add_success_05(self):
        logging.info("******正常场景05：个人客户--第三方--起息日小于账务日期--短期贷款--非按揭类******")
        self.jhxd.click_menu()
        sleep(1)
        self.jhxd.query_customer_loan("个人客户")
        # 开始断言
        sleep(1)
        self.assertTrue(len(self.jhxd.get_customer_count()) >= 1)
        a = self.jhxd.get_customer_count()
        print(a)
        print(a[0])

    # 正常场景06
    def test_add_success_06(self):
        logging.info("******正常场景06：若申请当日为某期次应还款日-1，则不能指定为方式当期生效******")
        self.jhxd.click_menu()
        sleep(1)
        self.jhxd.add_cust_data(jd.success_customer_data[4]["cname"],
                                jd.success_customer_data[4]["paperNo"],
                                jd.success_customer_data[4]["phoneNo"],
                                2)
        self.jhxd.enter_choose_product()
        sleep(1)
        # 进入简化信贷的保存页面
        self.jhxd.loan_apply_detail(561, 3, "备注哈哈哈哈")
        # 开始断言
        self.assertEqual(self.jhxd.get_message_from_save_success(), "保存成功")
        sleep(1)
        self.jhxd.save_sure_submit()
        sleep(3)
        # 进入简化信贷--》调查录入页面--》贷款基本信息模块
        self.jhxd.loan_data_basic('20140401', '20140801', 3, 3)
        # 进入简化信贷--》调查录入页面--》还款属性模块
        self.jhxd.loan_data_repayTyp(9, 8, 7, 3, 1, 1)
        # 进入简化信贷--》调查录入页面--》业务性质模块
        self.jhxd.loan_data_businessnature('是', '11312313123', '担保111111111', 'zfbw332432424', 1, 1, 2)
        # 进入简化信贷 - -》调查录入页面 - -》生成还款计划表
        self.jhxd.gen_reapy_sch()
        # 开始断言 贷款申请成功
        self.assertEqual(self.jhxd.get_message_from_loan_Save_success(), "请确认以上贷款信息，是否保存？")
        self.jhxd.save_success_click()
        # 开始断言
        self.assertTrue(self.jhxd.check_qianyue_exist())
        # 进入简化信贷--》签约页面,进行签约操作
        self.jhxd.contract_sign()

    # 正常场景07
    def test_add_success_07(self):
        logging.info("******正常场景07：贷款末期起息日<= 申请日<贷款到期日-1，则不能选择方式下期生效******")
        self.jhxd.click_menu()
        sleep(1)
        self.jhxd.add_cust_data(jd.success_customer_data[5]["cname"],
                                jd.success_customer_data[5]["paperNo"],
                                jd.success_customer_data[5]["phoneNo"],
                                2)
        self.jhxd.enter_choose_product()
        sleep(1)
        # 进入简化信贷的保存页面
        self.jhxd.loan_apply_detail(5610, 12, "备注哈哈哈哈")
        # 开始断言
        self.assertEqual(self.jhxd.get_message_from_save_success(), "保存成功")
        sleep(1)
        self.jhxd.save_sure_submit()
        sleep(3)
        # 进入简化信贷--》调查录入页面--》贷款基本信息模块
        self.jhxd.loan_data_basic('20130510', '20140510', 3, 3)
        # 进入简化信贷--》调查录入页面--》还款属性模块
        self.jhxd.loan_data_repayTyp(20, 34, 35, 3, 1, 1)
        # 进入简化信贷--》调查录入页面--》业务性质模块
        self.jhxd.loan_data_businessnature('是', '11312313123', '担保111111111', 'zfbw332432424', 1, 1, 2)
        # 进入简化信贷 - -》调查录入页面 - -》生成还款计划表
        self.jhxd.gen_reapy_sch()
        # 开始断言 贷款申请成功
        self.assertEqual(self.jhxd.get_message_from_loan_Save_success(), "请确认以上贷款信息，是否保存？")
        self.jhxd.save_success_click()
        # 开始断言
        self.assertTrue(self.jhxd.check_qianyue_exist())
        # 进入简化信贷--》签约页面,进行签约操作
        self.jhxd.contract_sign()

    # 正常场景08：非按揭-中长期-简化信贷的模板，默认为简化信贷的模板
    def test_add_success_08(self):
        logging.info("******正常场景08：非按揭-中长期-简化信贷的模板******")
        self.jhxd.click_menu()
        sleep(1)
        self.jhxd.add_cust_data(jd.success_customer_data[6]["cname"],
                                jd.success_customer_data[6]["paperNo"],
                                jd.success_customer_data[6]["phoneNo"],
                                2)
        sleep(1)  # 这三个元素需要等待一下
        self.jhxd.enter_choose_product(1)
        sleep(1)
        # 进入简化信贷的保存页面
        self.jhxd.loan_apply_detail(12345, 24, "备注哈哈哈哈")
        # 开始断言
        self.assertEqual(self.jhxd.get_message_from_save_success(), "保存成功")
        sleep(1)
        self.jhxd.save_sure_submit()
        sleep(3)
        # 进入简化信贷--》调查录入页面--》贷款基本信息模块
        self.jhxd.loan_data_basic('20130510', '20150510', 3, 3, 2)
        # 进入简化信贷--》调查录入页面--》还款属性模块
        self.jhxd.loan_data_repayTyp(20, 34, 35, 3, 1, 1)
        # 进入简化信贷--》调查录入页面--》业务性质模块
        self.jhxd.loan_data_businessnature('是', '11312313123', '担保111111111', 'zfbw332432424', 1, 1, 2)
        # 进入简化信贷 - -》调查录入页面 - -》生成还款计划表
        self.jhxd.gen_reapy_sch()
        # 开始断言 贷款申请成功
        self.assertEqual(self.jhxd.get_message_from_loan_Save_success(), "请确认以上贷款信息，是否保存？")
        self.jhxd.save_success_click()
        # 开始断言
        self.assertTrue(self.jhxd.check_qianyue_exist())
        # 进入简化信贷--》签约页面,进行签约操作
        self.jhxd.contract_sign()

    # 正常场景09：非按揭（按期还息到期还本）-中长期-产品类型为6开头的模板
    def test_add_success_09(self):
        logging.info("******正常场景09：非按揭-中长期-产品代码6开头的******")
        self.jhxd.click_menu()
        sleep(1)
        self.jhxd.add_cust_data(jd.success_customer_data[7]["cname"],
                                jd.success_customer_data[7]["paperNo"],
                                jd.success_customer_data[7]["phoneNo"],
                                2)
        sleep(1)  # # 这三个元素需要等待一下
        self.jhxd.enter_choose_product(2)
        sleep(1)
        # 进入简化信贷的保存页面
        self.jhxd.loan_apply_detail(5610, 24, "备注哈哈哈哈")
        # 开始断言
        self.assertEqual(self.jhxd.get_message_from_save_success(), "保存成功")
        sleep(1)
        self.jhxd.save_sure_submit()
        sleep(3)
        # 进入简化信贷--》调查录入页面--》贷款基本信息模块
        self.jhxd.loan_data_basic('20130510', '20150510', 3, 3, 2)
        # 进入简化信贷--》调查录入页面--》还款属性模块
        self.jhxd.loan_data_repayTyp(20, 34, 35, 3, 1, 1)
        # 进入简化信贷--》调查录入页面--》业务性质模块
        self.jhxd.loan_data_businessnature('是', '11312313123', '担保111111111', 'zfbw332432424', 1, 1, 2)
        # 进入简化信贷 - -》调查录入页面 - -》生成还款计划表
        self.jhxd.gen_reapy_sch()
        # 开始断言 贷款申请成功
        self.assertEqual(self.jhxd.get_message_from_loan_Save_success(), "请确认以上贷款信息，是否保存？")
        self.jhxd.save_success_click()
        # 开始断言
        self.assertTrue(self.jhxd.check_qianyue_exist())
        # 进入简化信贷--》签约页面,进行签约操作
        self.jhxd.contract_sign()

    # 正常场景10：非按揭-短期-简化信贷的模板，默认为简化信贷的模板
    def test_add_success_10(self):
        logging.info("******正常场景10：非按揭-短期-简化信贷的模板-*申请日>=贷款到期日-1然后展期*****")
        self.jhxd.click_menu()
        sleep(1)
        self.jhxd.add_cust_data(jd.success_customer_data[8]["cname"],
                                jd.success_customer_data[8]["paperNo"],
                                jd.success_customer_data[8]["phoneNo"],
                                2)
        sleep(1)  # 这三个元素需要等待一下
        self.jhxd.enter_choose_product(1)
        sleep(1)
        # 进入简化信贷的保存页面
        self.jhxd.loan_apply_detail(12345, 4, "备注哈哈哈哈")
        # 开始断言
        self.assertEqual(self.jhxd.get_message_from_save_success(), "保存成功")
        sleep(1)
        self.jhxd.save_sure_submit()
        sleep(3)
        # 进入简化信贷--》调查录入页面--》贷款基本信息模块
        self.jhxd.loan_data_basic('20140109', '20140509', 3, 3, 1)
        # 进入简化信贷--》调查录入页面--》还款属性模块
        self.jhxd.loan_data_repayTyp(20, 8, 7, 3, 1, 1)
        # 进入简化信贷--》调查录入页面--》业务性质模块
        self.jhxd.loan_data_businessnature('是', '11312313123', '担保111111111', 'zfbw332432424', 1, 1, 2)
        # 进入简化信贷 - -》调查录入页面 - -》生成还款计划表
        self.jhxd.gen_reapy_sch()
        # 开始断言 贷款申请成功
        self.assertEqual(self.jhxd.get_message_from_loan_Save_success(), "请确认以上贷款信息，是否保存？")
        self.jhxd.save_success_click()
        # 开始断言
        self.assertTrue(self.jhxd.check_qianyue_exist())
        # 进入简化信贷--》签约页面,进行签约操作
        self.jhxd.contract_sign()

    # 正常场景11：非按揭-短期-简化信贷的模板，默认为简化信贷的模板
    def test_add_success_11(self):
        logging.info("******正常场景11：非按揭-短期-简化信贷的模板-*申请日为0509，到期日为0511*****")
        self.jhxd.click_menu()
        sleep(1)
        self.jhxd.add_cust_data(jd.success_customer_data[9]["cname"],
                                jd.success_customer_data[9]["paperNo"],
                                jd.success_customer_data[9]["phoneNo"],
                                2)
        sleep(1)  # 这三个元素需要等待一下
        self.jhxd.enter_choose_product(1)
        sleep(1)
        # 进入简化信贷的保存页面
        self.jhxd.loan_apply_detail(12345, 4, "备注哈哈哈哈")
        # 开始断言
        self.assertEqual(self.jhxd.get_message_from_save_success(), "保存成功")
        sleep(1)
        self.jhxd.save_sure_submit()
        sleep(3)
        # 进入简化信贷--》调查录入页面--》贷款基本信息模块
        self.jhxd.loan_data_basic('20140111', '20140511', 3, 3, 1)
        # 进入简化信贷--》调查录入页面--》还款属性模块
        self.jhxd.loan_data_repayTyp(20, 8, 7, 3, 1, 1)
        # 进入简化信贷--》调查录入页面--》业务性质模块
        self.jhxd.loan_data_businessnature('是', '11312313123', '担保111111111', 'zfbw332432424', 1, 1, 2)
        # 进入简化信贷 - -》调查录入页面 - -》生成还款计划表
        self.jhxd.gen_reapy_sch()
        # 开始断言 贷款申请成功
        self.assertEqual(self.jhxd.get_message_from_loan_Save_success(), "请确认以上贷款信息，是否保存？")
        self.jhxd.save_success_click()
        # 开始断言
        self.assertTrue(self.jhxd.check_qianyue_exist())
        # 进入简化信贷--》签约页面,进行签约操作
        self.jhxd.contract_sign()

    # 正常场景12：非按揭-短期-简化信贷的模板，默认为简化信贷的模板
    def test_add_success_12(self):
        logging.info("******正常场景12：非按揭-短期-简化信贷的模板-*申请日为0509，到期日为0512*****")
        self.jhxd.click_menu()
        sleep(1)
        self.jhxd.add_cust_data(jd.success_customer_data[10]["cname"],
                                jd.success_customer_data[10]["paperNo"],
                                jd.success_customer_data[10]["phoneNo"],
                                2)
        sleep(1)  # 这三个元素需要等待一下
        self.jhxd.enter_choose_product(1)
        sleep(1)
        # 进入简化信贷的保存页面
        self.jhxd.loan_apply_detail(12345, 4, "备注哈哈哈哈")
        # 开始断言
        self.assertEqual(self.jhxd.get_message_from_save_success(), "保存成功")
        sleep(1)
        self.jhxd.save_sure_submit()
        sleep(3)
        # 进入简化信贷--》调查录入页面--》贷款基本信息模块
        self.jhxd.loan_data_basic('20140112', '20140512', 3, 3, 1)
        # 进入简化信贷--》调查录入页面--》还款属性模块
        self.jhxd.loan_data_repayTyp(20, 8, 7, 3, 1, 1)
        # 进入简化信贷--》调查录入页面--》业务性质模块
        self.jhxd.loan_data_businessnature('是', '11312313123', '担保111111111', 'zfbw332432424', 1, 1, 2)
        # 进入简化信贷 - -》调查录入页面 - -》生成还款计划表
        self.jhxd.gen_reapy_sch()
        # 开始断言 贷款申请成功
        self.assertEqual(self.jhxd.get_message_from_loan_Save_success(), "请确认以上贷款信息，是否保存？")
        self.jhxd.save_success_click()
        # 开始断言
        self.assertTrue(self.jhxd.check_qianyue_exist())
        # 进入简化信贷--》签约页面,进行签约操作
        self.jhxd.contract_sign()

    # 正常场景13：非按揭-短期-简化信贷的模板，默认为简化信贷的模板
    def test_add_success_13(self):
        logging.info("******正常场景13：非按揭-短期-简化信贷的模板-*申请日为0510，到期日为0715*****")
        self.jhxd.click_menu()
        sleep(1)
        self.jhxd.add_cust_data(jd.success_customer_data[11]["cname"],
                                jd.success_customer_data[11]["paperNo"],
                                jd.success_customer_data[11]["phoneNo"],
                                2)
        sleep(1)  # 这三个元素需要等待一下
        self.jhxd.enter_choose_product(1)
        sleep(1)
        # 进入简化信贷的保存页面
        self.jhxd.loan_apply_detail(12345, 6, "备注哈哈哈哈")
        # 开始断言
        self.assertEqual(self.jhxd.get_message_from_save_success(), "保存成功")
        sleep(1)
        self.jhxd.save_sure_submit()
        sleep(3)
        # 进入简化信贷--》调查录入页面--》贷款基本信息模块
        self.jhxd.loan_data_basic('20140115', '20140715', 3, 3, 1)
        # 进入简化信贷--》调查录入页面--》还款属性模块
        self.jhxd.loan_data_repayTyp(20, 8, 7, 3, 1, 1)
        # 进入简化信贷--》调查录入页面--》业务性质模块
        self.jhxd.loan_data_businessnature('是', '11312313123', '担保111111111', 'zfbw332432424', 1, 1, 2)
        # 进入简化信贷 - -》调查录入页面 - -》生成还款计划表
        self.jhxd.gen_reapy_sch()
        # 开始断言 贷款申请成功
        self.assertEqual(self.jhxd.get_message_from_loan_Save_success(), "请确认以上贷款信息，是否保存？")
        self.jhxd.save_success_click()
        # 开始断言
        self.assertTrue(self.jhxd.check_qianyue_exist())
        # 进入简化信贷--》签约页面,进行签约操作
        self.jhxd.contract_sign()

    # 正常场景14：非按揭-短期-简化信贷的模板，默认为简化信贷的模板
    # 若申请当日为某期次结息日，则不能指定为方式1、当期生效。申请日期为16号，那么应还款日设置为16
    # 检查结果怎么样
    @pytest.mark.smoke
    def test_add_success_14(self):
        logging.info("******正常场景14：非按揭-短期-简化信贷的模板-若申请当日为某期次结息日，则不能指定为方式1、当期生效*****")
        self.jhxd.click_menu()
        sleep(1)
        self.jhxd.add_cust_data(jd.success_customer_data[12]["cname"],
                                jd.success_customer_data[12]["paperNo"],
                                jd.success_customer_data[12]["phoneNo"],
                                2)
        sleep(1)  # 这三个元素需要等待一下
        self.jhxd.enter_choose_product(1)
        sleep(1)
        # 进入简化信贷的保存页面
        self.jhxd.loan_apply_detail(5678, 6, "备注哈哈哈哈")
        # 开始断言
        self.assertEqual(self.jhxd.get_message_from_save_success(), "保存成功")
        sleep(1)
        self.jhxd.save_sure_submit()
        sleep(3)
        # 进入简化信贷--》调查录入页面--》贷款基本信息模块
        self.jhxd.loan_data_basic('20140115', '20140715', 3, 3, 1)
        # 进入简化信贷--》调查录入页面--》还款属性模块
        self.jhxd.loan_data_repayTyp(16, 8, 7, 3, 1, 1)
        # 进入简化信贷--》调查录入页面--》业务性质模块
        self.jhxd.loan_data_businessnature('是', '11312313123', '担保111111111', 'zfbw332432424', 1, 1, 2)
        # 进入简化信贷 - -》调查录入页面 - -》生成还款计划表
        self.jhxd.gen_reapy_sch()
        # 开始断言 贷款申请成功
        self.assertEqual(self.jhxd.get_message_from_loan_Save_success(), "请确认以上贷款信息，是否保存？")
        self.jhxd.save_success_click()
        # 开始断言
        self.assertTrue(self.jhxd.check_qianyue_exist())
        # 进入简化信贷--》签约页面,进行签约操作
        self.jhxd.contract_sign()

    # 正常场景15：按揭:等额本息-短期-简化信贷的模板，默认为简化信贷的模板
    @pytest.mark.smoke
    def test_add_success_15(self):
        logging.info("******正常场景15：按揭-短期-简化信贷的模板*****")
        self.jhxd.click_menu()
        sleep(1)
        self.jhxd.add_cust_data(jd.success_customer_data[13]["cname"],
                                jd.success_customer_data[13]["paperNo"],
                                jd.success_customer_data[13]["phoneNo"],
                                2)
        sleep(1)  # 这三个元素需要等待一下
        self.jhxd.enter_choose_product(1)
        sleep(1)
        # 进入简化信贷的保存页面
        self.jhxd.loan_apply_detail(1234, 6, "备注哈哈哈哈")
        # 开始断言
        self.assertEqual(self.jhxd.get_message_from_save_success(), "保存成功")
        sleep(1)
        self.jhxd.save_sure_submit()
        sleep(3)
        # 进入简化信贷--》调查录入页面--》贷款基本信息模块
        self.jhxd.loan_data_basic('20140115', '20140715', 3, 3, 1)
        # 进入简化信贷--》调查录入页面--》还款属性模块
        self.jhxd.loan_data_repayTyp(16, 8, 7, 1, 1, 1)
        # 进入简化信贷--》调查录入页面--》业务性质模块
        self.jhxd.loan_data_businessnature('是', '11312313123', '担保111111111', 'zfbw332432424', 1, 1, 2)
        # 进入简化信贷 - -》调查录入页面 - -》生成还款计划表
        self.jhxd.gen_reapy_sch()
        # 开始断言 贷款申请成功
        self.assertEqual(self.jhxd.get_message_from_loan_Save_success(), "请确认以上贷款信息，是否保存？")
        self.jhxd.save_success_click()
        # 开始断言
        self.assertTrue(self.jhxd.check_qianyue_exist())
        # 进入简化信贷--》签约页面,进行签约操作
        self.jhxd.contract_sign()

    # 正常场景16：非逾期、非按揭:利随本清-短期（就一期）-简化信贷的模板，默认为简化信贷的模板
    @pytest.mark.smoke
    @pytest.mark.zhanqi
    def test_add_success_16(self):
        logging.info("******正常场景16：非按揭:利随本清-简化信贷的模板*****")
        self.jhxd.click_menu()
        sleep(1)
        self.jhxd.add_cust_data(jd.success_customer_data[14]["cname"],
                                jd.success_customer_data[14]["paperNo"],
                                jd.success_customer_data[14]["phoneNo"],
                                2)
        sleep(1)  # 这三个元素需要等待一下
        self.jhxd.enter_choose_product(1)
        sleep(1)
        # 进入简化信贷的保存页面
        self.jhxd.loan_apply_detail(1234, 6, "备注哈哈哈哈")
        # 开始断言
        self.assertEqual(self.jhxd.get_message_from_save_success(), "保存成功")
        sleep(1)
        self.jhxd.save_sure_submit()
        sleep(3)
        # 进入简化信贷--》调查录入页面--》贷款基本信息模块
        self.jhxd.loan_data_basic('20131218', '20140618', 3, 3, 1)
        # 进入简化信贷--》调查录入页面--》还款属性模块
        self.jhxd.loan_data_repayTyp(16, 8, 7, 4, 1, 1)
        # 进入简化信贷--》调查录入页面--》业务性质模块
        self.jhxd.loan_data_businessnature('是', '11312313123', '担保111111111', 'zfbw332432424', 1, 1, 2)
        # 进入简化信贷 - -》调查录入页面 - -》生成还款计划表
        self.jhxd.gen_reapy_sch()
        # 开始断言 贷款申请成功
        self.assertEqual(self.jhxd.get_message_from_loan_Save_success(), "请确认以上贷款信息，是否保存？")
        self.jhxd.save_success_click()
        # 开始断言
        self.assertTrue(self.jhxd.check_qianyue_exist())
        # 进入简化信贷--》签约页面,进行签约操作
        self.jhxd.contract_sign()

    # 正常场景17：按揭:等额本息-中长期-简化信贷的模板，默认为简化信贷的模板！！！！
    @pytest.mark.smoke
    def test_add_success_17(self):
        logging.info("******正常场景17：按揭-中长期-简化信贷的模板*****")
        self.jhxd.click_menu()
        sleep(1)
        self.jhxd.add_cust_data(jd.success_customer_data[15]["cname"],
                                jd.success_customer_data[15]["paperNo"],
                                jd.success_customer_data[15]["phoneNo"],
                                2)
        sleep(1)  # 这三个元素需要等待一下
        self.jhxd.enter_choose_product(1)
        sleep(1)
        # 进入简化信贷的保存页面
        self.jhxd.loan_apply_detail(1234, 30, "备注哈哈哈哈")
        # 开始断言
        self.assertEqual(self.jhxd.get_message_from_save_success(), "保存成功")
        sleep(1)
        self.jhxd.save_sure_submit()
        sleep(3)
        # 进入简化信贷--》调查录入页面--》贷款基本信息模块
        self.jhxd.loan_data_basic('20140227', '20160827', 3, 3, 2)
        # 进入简化信贷--》调查录入页面--》还款属性模块
        self.jhxd.loan_data_repayTyp(16, 25, 35, 1, 1, 1)
        # 进入简化信贷--》调查录入页面--》业务性质模块
        self.jhxd.loan_data_businessnature('是', '11312313123', '担保111111111', 'zfbw332432424', 1, 1, 2)
        # 进入简化信贷 - -》调查录入页面 - -》生成还款计划表
        self.jhxd.gen_reapy_sch()
        # 开始断言 贷款申请成功
        self.assertEqual(self.jhxd.get_message_from_loan_Save_success(), "请确认以上贷款信息，是否保存？")
        self.jhxd.save_success_click()
        # 开始断言
        self.assertTrue(self.jhxd.check_qianyue_exist())
        # 进入简化信贷--》签约页面,进行签约操作
        self.jhxd.contract_sign()

    # 正常场景18：非逾期、非按揭:利随本清-短期（就一期）-简化信贷的模板，默认为简化信贷的模板
    @pytest.mark.smoke
    @pytest.mark.zhanqi
    def test_add_success_18(self):
        logging.info("******正常场景18：非按揭:利随本清-简化信贷的模板*****")
        self.jhxd.click_menu()
        sleep(1)
        self.jhxd.add_cust_data(jd.success_customer_data[14]["cname"],
                                jd.success_customer_data[14]["paperNo"],
                                jd.success_customer_data[14]["phoneNo"],
                                2)
        sleep(1)  # 这三个元素需要等待一下
        self.jhxd.enter_choose_product(1)
        sleep(1)
        # 进入简化信贷的保存页面
        self.jhxd.loan_apply_detail(1234, 6, "备注哈哈哈哈")
        # 开始断言
        self.assertEqual(self.jhxd.get_message_from_save_success(), "保存成功")
        sleep(1)
        self.jhxd.save_sure_submit()
        sleep(3)
        # 进入简化信贷--》调查录入页面--》贷款基本信息模块
        self.jhxd.loan_data_basic('20131217', '20140617', 3, 3, 1)
        # 进入简化信贷--》调查录入页面--》还款属性模块
        self.jhxd.loan_data_repayTyp(16, 8, 7, 4, 1, 1)
        # 进入简化信贷--》调查录入页面--》业务性质模块
        self.jhxd.loan_data_businessnature('是', '11312313123', '担保111111111', 'zfbw332432424', 1, 1, 2)
        # 进入简化信贷 - -》调查录入页面 - -》生成还款计划表
        self.jhxd.gen_reapy_sch()
        # 开始断言 贷款申请成功
        self.assertEqual(self.jhxd.get_message_from_loan_Save_success(), "请确认以上贷款信息，是否保存？")
        self.jhxd.save_success_click()
        # 开始断言
        self.assertTrue(self.jhxd.check_qianyue_exist())
        # 进入简化信贷--》签约页面,进行签约操作
        self.jhxd.contract_sign()

    # 正常场景19：非逾期、非按揭:按期还息到期还本-短期-简化信贷的模板，默认为简化信贷的模板
    @pytest.mark.smoke
    def test_add_success_19(self):
        logging.info("******正常场景19：非按揭:按期还息到期还本-简化信贷的模板*****")
        self.jhxd.click_menu()
        sleep(1)
        self.jhxd.add_cust_data(jd.success_customer_data[14]["cname"],
                                jd.success_customer_data[14]["paperNo"],
                                jd.success_customer_data[14]["phoneNo"],
                                2)
        sleep(1)  # 这三个元素需要等待一下
        self.jhxd.enter_choose_product(1)
        sleep(1)
        # 进入简化信贷的保存页面
        self.jhxd.loan_apply_detail(1234, 6, "备注哈哈哈哈")
        # 开始断言
        self.assertEqual(self.jhxd.get_message_from_save_success(), "保存成功")
        sleep(1)
        self.jhxd.save_sure_submit()
        sleep(3)
        # 进入简化信贷--》调查录入页面--》贷款基本信息模块
        self.jhxd.loan_data_basic('20140125', '20140725', 1, 1, 1)
        # 进入简化信贷--》调查录入页面--》还款属性模块
        self.jhxd.loan_data_repayTyp(25, 8, 7, 3, 1, 1)
        # 进入简化信贷--》调查录入页面--》业务性质模块
        self.jhxd.loan_data_businessnature('是', '11312313123', '担保111111111', 'zfbw332432424', 1, 1, 2)
        # 进入简化信贷 - -》调查录入页面 - -》生成还款计划表
        self.jhxd.gen_reapy_sch()
        # 开始断言 贷款申请成功
        self.assertEqual(self.jhxd.get_message_from_loan_Save_success(), "请确认以上贷款信息，是否保存？")
        self.jhxd.save_success_click()
        # 开始断言
        self.assertTrue(self.jhxd.check_qianyue_exist())
        # 进入简化信贷--》签约页面,进行签约操作
        self.jhxd.contract_sign()

    # 正常场景20：逾期、非按揭:按期还息到期还本-短期-简化信贷的模板，默认为简化信贷的模板
    @pytest.mark.smoke
    def test_add_success_20(self):
        logging.info("******正常场景20：非按揭:按期还息到期还本-简化信贷的模板*****")
        self.jhxd.click_menu()
        sleep(1)
        self.jhxd.add_cust_data(jd.success_customer_data[14]["cname"],
                                jd.success_customer_data[14]["paperNo"],
                                jd.success_customer_data[14]["phoneNo"],
                                2)
        sleep(1)  # 这三个元素需要等待一下
        self.jhxd.enter_choose_product(1)
        sleep(1)
        # 进入简化信贷的保存页面
        self.jhxd.loan_apply_detail(1234, 6, "备注哈哈哈哈")
        # 开始断言
        self.assertEqual(self.jhxd.get_message_from_save_success(), "保存成功")
        sleep(1)
        self.jhxd.save_sure_submit()
        sleep(3)
        # 进入简化信贷--》调查录入页面--》贷款基本信息模块
        self.jhxd.loan_data_basic('20140227', '20140827', 3, 3, 1)
        # 进入简化信贷--》调查录入页面--》还款属性模块
        self.jhxd.loan_data_repayTyp(16, 8, 7, 3, 1, 1)
        # 进入简化信贷--》调查录入页面--》业务性质模块
        self.jhxd.loan_data_businessnature('是', '11312313123', '担保111111111', 'zfbw332432424', 1, 1, 2)
        # 进入简化信贷 - -》调查录入页面 - -》生成还款计划表
        self.jhxd.gen_reapy_sch()
        # 开始断言 贷款申请成功
        self.assertEqual(self.jhxd.get_message_from_loan_Save_success(), "请确认以上贷款信息，是否保存？")
        self.jhxd.save_success_click()
        # 开始断言
        self.assertTrue(self.jhxd.check_qianyue_exist())
        # 进入简化信贷--》签约页面,进行签约操作
        self.jhxd.contract_sign()

    # 正常场景21：展期：非逾期-非按揭（按期还息到期还本）-中长期-产品类型为6开头的模板（有问题）
    def test_add_success_21(self):
        logging.info("******正常场景21：展期-非按揭-中长期-产品代码6开头的******")
        self.jhxd.click_menu()
        sleep(1)
        self.jhxd.add_cust_data(jd.success_customer_data[7]["cname"],
                                jd.success_customer_data[7]["paperNo"],
                                jd.success_customer_data[7]["phoneNo"],
                                2)
        sleep(1)  # # 这三个元素需要等待一下
        self.jhxd.enter_choose_product(2)
        sleep(1)

    # 正常场景22：普通按揭:利随本清-短期-简化信贷的模板，默认为简化信贷的模板
    @pytest.mark.smoke
    def test_add_success_22(self):
        logging.info("******正常场景22：非按揭:i随本清-简化信贷的模板*****")
        self.jhxd.click_menu()
        sleep(1)
        self.jhxd.add_cust_data(jd.success_customer_data[14]["cname"],
                                jd.success_customer_data[14]["paperNo"],
                                jd.success_customer_data[14]["phoneNo"],
                                2)
        sleep(1)  # 这三个元素需要等待一下
        self.jhxd.enter_choose_product(1)
        sleep(1)
        # 进入简化信贷的保存页面
        self.jhxd.loan_apply_detail(1234, 6, "备注哈哈哈哈")
        # 开始断言
        self.assertEqual(self.jhxd.get_message_from_save_success(), "保存成功")
        sleep(1)
        self.jhxd.save_sure_submit()
        sleep(3)
        # 进入简化信贷--》调查录入页面--》贷款基本信息模块
        self.jhxd.loan_data_basic('20130102', '20140702', 28, 28, 1)
        # 进入简化信贷--》调查录入页面--》还款属性模块
        self.jhxd.loan_data_repayTyp(16, 8, 7, 4, 1, 1)
        # 进入简化信贷--》调查录入页面--》业务性质模块
        self.jhxd.loan_data_businessnature('是', '11312313123', '担保111111111', 'zfbw332432424', 1, 1, 2)
        # 进入简化信贷 - -》调查录入页面 - -》生成还款计划表
        self.jhxd.gen_reapy_sch()
        # 开始断言 贷款申请成功
        self.assertEqual(self.jhxd.get_message_from_loan_Save_success(), "请确认以上贷款信息，是否保存？")
        self.jhxd.save_success_click()
        # 开始断言
        self.assertTrue(self.jhxd.check_qianyue_exist())
        # 进入简化信贷--》签约页面,进行签约操作
        self.jhxd.contract_sign()
