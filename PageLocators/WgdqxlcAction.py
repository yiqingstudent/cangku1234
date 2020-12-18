#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : WgdqxlcAction.py
@Author: rebecca
@Date  : 2020/5/29 14:01
@Desc  : 无固定期限理财登记
"""
from selenium.webdriver.common.by import By


class WgdqxLc_loc:
    # 元素定位-资金业务
    zjyw_loc = (By.XPATH, '//span[text()="资金业务"]')
    # 元素定位-流动性管理
    loc_wgdlc = (By.XPATH, '//a[text()="无固定期限理财登记"]')
    # 查询-理财名称输入框
    loc_query_lcname = (By.ID, 'lcmc.WgdqxPanel')
    # 查询按钮
    loc_query = (By.XPATH, "//button[text()='查询']")
    # 新增按钮
    loc_add = (By.XPATH, '//button[text()="新增"]')
    # 输入框-理财名称
    loc_lcmc = (By.ID, 'lcmc.WgdqxWin')
    # 输入框-机构  //div[@class='x-combo-list-inner'][1]
    loc_jg = (By.ID, 'jg.WgdqxWin')
    loc_bank = (By.XPATH, "//div[@class='x-combo-list-inner'][1]/div[text()='银行']")
    loc_other_jg = (By.XPATH, "//div[@class='x-combo-list-inner'][1]/div[text()='其他机构']")
    # 输入框-理财类型
    loc_lclx = (By.ID, 'lclx.WgdqxWin')
    # 理财类型：T+0
    loc_T0 = (By.XPATH, '//div[@class="x-layer x-combo-list "][2]//div[text()="T+0"]')
    # 理财类型：T+1
    loc_T1 = (By.XPATH, '//div[@class="x-layer x-combo-list "][2]//div[text()="T+1"]')
    # 理财类型： 其他
    loc_other = (By.XPATH, '//div[@class="x-layer x-combo-list "][2]//div[text()="其他"]')
    # 登记类型：djlx.WgdqxWin
    loc_djlx = (By.ID, 'djlx.WgdqxWin')
    # 登记类型-申购
    loc_sg = (By.XPATH, '//div[@class="x-layer x-combo-list "][3]//div[text()="申购"]')
    loc_sh = (By.XPATH, '//div[@class="x-layer x-combo-list "][3]//div[text()="赎回"]')
    # 交易金额
    loc_jyje = (By.ID, 'jyje.WgdqxWin')
    # 备注
    loc_remark = (By.ID, 'remark.WgdqxWin')
    # 保存按钮
    loc_save = (By.XPATH, '//button[text()="保存"]')
    # 保存成功！
    loc_success_info = (By.XPATH, '//span[text()="操作成功！"]')
    # 确定按钮
    loc_confirm = (By.XPATH, '//button[text()="确定"]')
    # 查询结果
    loc_number = (By.XPATH, '//div[@class="x-grid3-cell-inner x-grid3-col-3"]')






