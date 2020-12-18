#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : rateadj_page_loc.py
@Author: rebecca
@Date  : 2020/4/13 11:08
@Desc  : 
"""
from selenium.webdriver.common.by import By


class RateAdjPageLoc:
    # 元素定位-信贷业务
    business_loc = (By.XPATH, '//span[text()="信贷业务"]')
    # 元素定位-执行利率调整
    loc_formal = (By.XPATH, '//a[text()="执行利率调整"]')
    # 查询按钮
    loc_query = (By.XPATH, "//button[text()='查询']")
    # 选择第一条
    loc_first_choose = (By.XPATH, '//div[@id="grid.RateAdjustTzsqQuery"]//div[@class="x-grid3-body"]/div[1]')
    # 点击新增申请
    loc_add = (By.XPATH, '//button[text()="新增申请"]')
    # 月利率
    loc_month = (By.XPATH, '//input[@id="afterIntRateM.RateAdjustPanel.DTL"]')
    # 执行利率调整
    loc_rate_adj = (By.XPATH, '//input[@id="afterIntRate.RateAdjustPanel"]')
    # 当期生效按钮
    loc_cur_effect = (By.XPATH, '//label[text()="当期生效"]')
    #  下期生效按钮
    loc_next_effect = (By.XPATH, '//label[text()="下期生效"]')
    # 利率生效日期
    loc_eff_date = (By.XPATH, '//input[@id="effDt.RateAdjustPanel"]')
    # 生成还款计划表
    loc_btnGenSchd = (By.XPATH, '//font[text()="生成还款计划"]')
    # 保存按钮
    loc_save = (By.XPATH, '//button[text()="保存"]')
    # 系统提示信息
    loc_success_info = (By.XPATH, '//span[text()="保存成功！"]')
    # 确定按钮
    loc_sure = (By.XPATH, '//button[text()="确定"]')
    # 确认是否提交
    loc_submit = (By.XPATH, '//span[text()="请确认是否提交？"]')
    # 确认提交：是
    loc_yes = (By.XPATH, '//button[text()="是"]')
    # 选择岗位审批
    loc_posts = (By.XPATH, '//label[text()="岗位审批"]')
    # 选择审批者
    loc_approver = (By.ID, 'formworkflowSubmit_editor_examinerrole')
    # 选择决策岗
    loc_decision = (By.XPATH, '//div[@title="决策岗"]')
    # 提交给决策岗
    loc_buttonSubmit = (By.ID, 'buttonSubmit')