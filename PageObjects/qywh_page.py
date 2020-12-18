#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : qywh_page.py
@Author: rebecca
@Date  : 2020/4/24 10:02
@Desc  : 
"""
from selenium import webdriver
from PageLocators.qywh_page_loc import EnterprisePageLoc as loc
from Common.basepage import BasePage
from selenium.webdriver.remote.webdriver import WebDriver


class EnterpriseMain(BasePage):
    # 继承了basepage的类，就可以直接使用里面的函数了~
    # 申明是webdriver的类型，就可以直接使用self.
    # def __init__(self, driver:WebDriver):
    #     self.driver = driver
    #     self.BasePage = BasePage(self.driver)

    # 进入菜单：菜单-监管评级-供应链核心企业维护
    def click_menu(self):
        self.move_to_click(loc.jg_menu_loc, "菜单-监管评级")
        self.click_ele_success(loc.qywh_meun_loc, "菜单-供应链核心企业维护")

    # 查询操作，新增结束之后，进行查找
    def query_loan(self, name):
        self.driver.switch_to.frame("content_iframe")
        self.input_element_value(loc.qy_name_loc, name, "供应链核心企业名称-输入框")
        self.click_ele_success(loc.loc_query, "供应链核心企业维护")

    # 新增操作:进入新的frame，点击新增按钮，输入正确的数据
    def add_input_data(self, name, code, remark, flag='N'):
        self.driver.switch_to.frame("content_iframe")
        self.click_ele_success(loc.loc_add, "供应链核心企业维护-新增按钮")
        # 默认组织机构代码证和启用状态
        if flag == 'N':
            self.input_element_value(loc.loc_name, name, "新增页面-输入核心企业名称")
            self.input_element_value(loc.loc_cLiceNo, code, "新增页面-输入组织机构代码证")
            self.input_element_value(loc.loc_remark, remark, "新增页面-输入备注，不超500个汉字")
            self.click_ele_success(loc.loc_save, "新增页面-保存按钮")
            self.click_ele_success(loc.loc_sure_yes, "提示框-是")
            # self.click_ele_success(loc.loc_confirm, "提示框-确认")
        else:
            self.input_element_value(loc.loc_name, name, "新增页面-输入核心企业名称")
            self.click_ele_success(loc.loc_liceNo_yes, "新增页面-选择三证合一：是")
            self.input_element_value(loc.loc_liceNo, code, "新增页面-输入社会统一信息代码证")
            # self.click_ele_success(loc.loc_isEnable_yes, "新增页面-是否：是")  默认为：是
            self.input_element_value(loc.loc_remark, remark, "新增页面-输入备注，不超500个汉字")
            self.click_ele_success(loc.loc_save, "新增页面-保存按钮")
            self.click_ele_success(loc.loc_sure_yes, "提示框-是")
            # self.click_ele_success(loc.loc_confirm, "提示框-确认")

    def get_message_from_please_sure(self):
        return self.get_element_text(loc.loc_save_text, "新增页面-请确认是否保存的提示信息")

    def get_message_from_save_success(self):
        return self.get_element_text(loc.loc_success_info, "新增页面-保存成功的提示框内容")

    def get_value_from_query(self):
        return self.get_elements_texts(loc.loc_number, "获取码值有几个")


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://172.31.19.96:80/pubsys/login.jsp")




