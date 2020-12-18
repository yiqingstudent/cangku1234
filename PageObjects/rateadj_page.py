#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : rateadj_page.py
@Author: rebecca
@Date  : 2020/4/7 16:01
@Desc  : 
"""
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

from Common.basepage import BasePage
from PageLocators.rateadj_page_loc import RateAdjPageLoc as loc
from selenium.webdriver.common.keys import Keys

from Common.public_func import PublicFunc


class RateAdjPage(BasePage):
    def click_menu(self):
        self.move_to_click(loc.business_loc, "菜单-信贷业务")
        self.click_ele_success(loc.loc_formal, "菜单-执行利率调整")

    def query_loan(self):
        # 进入菜单主页面：第一个frame
        self.driver.switch_to.frame("content_iframe")
        self.click_ele_success(loc.loc_query, "执行利率调整页面")

    def choose_first_loan(self):
        # 客户列表中选择：可以选择第一条
        pass

    def add_request(self):
        self.click_ele_success(loc.loc_first_choose, "执行利率调整-选择第一条数据")
        self.click_ele_success(loc.loc_add, "执行利率调整-新增按钮")

    def input_data(self, rate, cur_effect=True, effDt=None):
        # 默认为当期登录
        if cur_effect:
            # 先选择“是否当期生效”
            self.click_ele_success(loc.loc_cur_effect, "新增页面-当期生效")
            # 触发一次生效日期的输入框
            self.click_ele_success(loc.loc_eff_date, "新增页面-生效日期")
            # 输入生效日期的js用法
            js_effDt = """
                    var b = arguments[0]
                    b.readOnly = false;
                    b.value = arguments[1];
                    """
            self.driver.execute_script(js_effDt, self.get_element_success(loc.loc_eff_date, "新增页面-生效日期元素"), effDt)
            self.input_element_value(loc.loc_rate_adj, rate, "新增页面-输入利率")
            self.click_ele_success(loc.loc_month, "新增页面-单击月利率")
        else:
            self.click_ele_success(loc.loc_next_effect, "新增页面-下期生效")
            self.input_element_value(loc.loc_rate_adj, rate, "新增页面-输入利率")
            self.click_ele_success(loc.loc_month, "新增页面-单击月利率")
        # 点击生成还款计划表
        self.click_ele_success(loc.loc_btnGenSchd, "新增页面-点击生成还款计划表")
        # 点击保存按钮
        self.execute_scroll_view(loc.loc_save, "新增页面-保存按钮在最下方")
        # e = self.get_element_success(loc.loc_save, "新增页面-拖到最下方")
        # self.driver.execute_script("arguments[0].scrollIntoView();", e)
        self.click_ele_success(loc.loc_save, "新增页面-单击保存按钮")

    def get_message_from_save(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.loc_success_info))
        return self.driver.find_element(*loc.loc_success_info).text

    def get_message_from_submit(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.loc_submit))
        return self.driver.find_element(*loc.loc_submit).text

    def save_submit(self):
        # 点击提示信息的确定按钮
        self.driver.find_element(*loc.loc_sure).click()
        # 点击提示信息的“是”
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.loc_yes))
        self.driver.find_element(*loc.loc_yes).click()
        # 进入审批页面
        self.driver.switch_to.frame("submitPage.WorkflowSubmitWin")
        # 选择岗位审批
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.loc_posts))
        self.driver.find_element(*loc.loc_posts).click()
        # 选中岗位输入框，单击，触发下拉框出现
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.loc_approver))
        self.driver.find_element(*loc.loc_approver).click()
        # 选择决策岗
        self.driver.switch_to.frame("dpdownUserRole$X3")
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.loc_decision))
        element_decison = self.driver.find_element(*loc.loc_decision)
        ActionChains(self.driver).double_click(element_decison).perform()
        print("#"*20)
        # 提交按钮
        self.driver.switch_to.parent_frame()
        self.driver.find_element(*loc.loc_buttonSubmit).click()
        # 最后一步：操作系统提示信息
        # 1、windows的页面弹出框，而非页面元素，右键无法检查的
        # 2、等待30秒，隔1秒检查一次.直到期望的条件--弹出框存在
        WebDriverWait(self.driver, 30, 1).until(expected_conditions.alert_is_present())
        # 点击确定
        res = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        print("执行利率调整流程{} 提交成功，流程结束！".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        print(res)

























