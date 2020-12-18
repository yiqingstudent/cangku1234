#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : accounting_lending.py
@Author: rebecca
@Date  : 2020/6/4 15:09
@Desc  : 
"""
from PageLocators.jhxd_page_loc import JianXdPageLoc as loc
from Common.basepage import BasePage
from time import sleep


class AccountLending(BasePage):
    # 进入菜单：菜单-信贷业务-发放贷款
    def click_menu(self):
        self.move_to_click(loc.business_loc, "菜单-信贷业务")
        self.click_ele_success(loc.loc_yw_apply, "菜单-发放贷款")

    def test(self):
        pass
