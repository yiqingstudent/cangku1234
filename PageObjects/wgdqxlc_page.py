#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : rateadj_page.py
@Author: rebecca
@Date  : 2020/4/7 16:01
@Desc  : 
"""
from selenium import webdriver
from PageLocators.WgdqxlcAction import WgdqxLc_loc as loc
from Common.basepage import BasePage


class WgdqxPage(BasePage):
    def click_menu(self):
        self.move_to_click(loc.zjyw_loc, "菜单-资金业务")
        self.execute_scroll_view(loc.loc_wgdlc, "菜单-无固定期限理财登记")
        self.click_ele_success(loc.loc_wgdlc, "菜单-无固定期限理财登记")

    # 查询操作，新增结束之后，进行查找
    def query_loan(self, name):
        self.driver.switch_to.frame("content_iframe")
        self.input_element_value(loc.loc_query_lcname, name, "理财名称-输入框")
        self.click_ele_success(loc.loc_query, "无固定理财期限登记查询功能")

    # 新增操作:进入新的frame，点击新增按钮，输入正确的数据
    def add_licai_name_data(self, name, money, remark):
        self.driver.switch_to.frame("content_iframe")
        self.click_ele_success(loc.loc_add, "无固定理财-新增按钮")
        self.input_element_value(loc.loc_lcmc, name, "新增页面-输入理财名称")
        self.click_ele_success(loc.loc_jg, "无固定理财-触发机构按钮")
        self.click_ele_success(loc.loc_bank, "无固定理财-选择机构：银行")

        self.click_ele_success(loc.loc_lclx, "无固定理财-触发理财类型")
        self.click_ele_success(loc.loc_T0, "无固定理财-选择理财类型：T+0")

        self.click_ele_success(loc.loc_djlx, "无固定理财-触发登记类型")
        self.click_ele_success(loc.loc_sg, "无固定理财-选登记类型：申购")

        self.input_element_value(loc.loc_jyje, money, "新增页面-输入交易金额")

        self.input_element_value(loc.loc_remark, remark, "新增页面-输入备注，不超500个汉字")
        self.click_ele_success(loc.loc_save, "新增页面-保存按钮")

    def get_message_from_save_success(self):
        return self.get_element_text(loc.loc_success_info, "新增页面-保存成功的提示框内容")

    def get_value_from_query(self):
        return self.get_elements_texts(loc.loc_number, "获取码值有几个")


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://172.31.19.71:80/pubsys/login.jsp")




















