#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : qywh_page_loc.py
@Author: rebecca
@Date  : 2020/4/24 10:07
@Desc  : 
"""
from selenium.webdriver.common.by import By


class EnterprisePageLoc:
    # 监管评级菜单
    jg_menu_loc = (By.XPATH, '//span[text()="监管评级"]')
    # 供应链核心企业菜单
    qywh_meun_loc = (By.XPATH, '//a[text()="供应链核心企业维护"]')
    # 查询条件-供应链核心企业名称输入框
    qy_name_loc = (By.ID, 'PartName.PartnerOrg')
    # 查询按钮
    loc_query = (By.XPATH, "//button[text()='查询']")
    # 新增按钮
    loc_add = (By.XPATH, '//button[text()="新增"]')
    # 新增页面-供应链核心企业输入框
    loc_name = (By.ID, 'partName.PartnerOrgWin')
    # 新增页面-社会统一信用代码证
    loc_liceNo = (By.ID, 'liceNo.PartnerOrgWin')
    # 新增页面-组织机构代码证
    loc_cLiceNo = (By.ID, 'cLiceNo.PartnerOrgWin')
    #  新增页面-营业执照号码 regNo.PartnerOrgWin
    loc_regNo = (By.ID, 'regNo.PartnerOrgWin')
    # 新增页面-备注
    loc_remark = (By.ID, 'remark.PartnerOrgWin')
    # 新增页面-三证合一-是
    loc_liceNo_yes = (By.XPATH, '//input[@name="liceNoOrNewCard" and @value="Y"]')
    # 新增页面-三证合一-否
    loc_liceNo_no = (By.XPATH, '//input[@name="liceNoOrNewCard" and @value="N"]')
    # 新增页面-是否启用-是
    loc_isEnable_yes = (By.XPATH, '//input[@name="isEnable" and @value="Y"]')
    # 新增页面-是否启用-否
    loc_isEnable_no = (By.XPATH, '//input[@name="isEnable" and @value="N"]')
    # 新增页面-保存
    loc_save = (By.XPATH, '//button[text()="保存"]')
    # 请确认是否保存的提示信息定位符
    loc_save_text = (By.XPATH, '//span[text()="请确认是否保存!"]')
    # 请确认是否保存!--选择是
    loc_sure_yes = (By.XPATH, '//button[text()="是"]')
    # 保存成功！
    loc_success_info = (By.XPATH, '//span[text()="保存成功！"]')
    # 确定按钮
    loc_confirm = (By.XPATH, '//button[text()="确定"]')
    # 查询结果
    loc_number = (By.XPATH, '//div[@class="x-grid3-cell-inner x-grid3-col-3"]')










