#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : shouxin_page_loc.py
@Author: rebecca
@Date  : 2020/6/22 16:14
@Desc  : 
"""
from selenium.webdriver.common.by import By


class ShouXinPageLoc:
    # 元素定位-简化信贷业务申请页面
    business_loc = (By.XPATH, '//span[text()="信贷业务"]')
    # 元素定位-业务申请办理
    loc_yw_apply = (By.XPATH, '//a[text()="业务申请办理"]')
    # 查询按钮
    loc_query = (By.XPATH, "//button[text()='查询']")
    # 客户名称-查询
    loc_cust_name = (By.ID, "custName.LoanQueryMgrPnl")
    # 新增业务按钮
    loc_bus_add = (By.XPATH, "//button[text()='新增业务']")

    # 新增二级页面的 BuildCustMgrPnl -->客户名称查询
    loc_custName_BC = (By.ID, "custName.BuildCustMgrPnl")
    loc_custName_query = (By.ID, "query.BuildCustMgrPnl")
    # 新客户按钮
    loc_add_cust = (By.ID, "add.BuildCustMgrPnl")

    # 新客户-默认个人客户的radio按钮
    # 客户资料-》个人客户->客户名称
    loc_custName = (By.ID, "custName.RegisterCustInfoWin")
    # 客户资料-》个人客户->身份证号
    loc_paperNo = (By.ID, "paperNo.RegisterCustInfoWin")
    # 客户资料-》个人客户->手机号码
    loc_phoneNo = (By.ID, "phoneNo.RegisterCustInfoWin")
    # 客户资料-》个人客户-》客户来源 typeSource.RegisterCustInfoWin
    loc_cust_typeSource = (By.ID, "typeSource.RegisterCustInfoWin")
    # 客户资料-》个人客户-》客户来源:自营
    loc_cust_typeSource_first = (By.XPATH, "//div[@class='x-combo-list-inner']/div[2]")
    # 客户资料-》个人客户-》客户来源:第三方
    loc_cust_typeSource_second = (By.XPATH, "//div[@class='x-combo-list-inner']/div[3]")
    # 客户资料-》个人客户-》客户来源名称
    loc_cust_cdeSource = (By.ID, "cdeSource.RegisterCustInfoWin")
    loc_cust_cdeSource_first = (By.XPATH, "//div[@class='x-layer x-combo-list '][2]//div[2]")

    # 新客户-选择企业客户的radio按钮
    loc_corpCust = (By.ID, 'corpCust.RegisterCustInfoWin')
    # 新客户-企业客户-企业名称
    loc_corpName = (By.ID, "custName.RegisterCustInfoWin")
    # 新客户-企业客户-组织机构代码证
    loc_cLiceNo = (By.ID, "cLiceNo.RegisterCustInfoWin")
    # 新客户-企业客户-联系方式手机号
    loc_corp_phoneNo = (By.ID, "phoneNo.RegisterCustInfoWin")
    # 新客户-企业客户-客户来源（自营、第三方）
    # 新客户-企业客户-客户来源名称

    # 保存按钮（个人+企业）
    loc_register = (By.ID, "btnRegister.RegisterCustInfoWin")
    #  提示信息
    loc_tips = (By.XPATH, "//span[@class='ext-mb-text']")
    # 选择是
    loc_yes = (By.XPATH, "//button[text()='是']")
    # 保存成功！
    loc_save_cust = (By.XPATH, "//button[text()='保存成功！']")
    #  确定按钮
    loc_sure_cust = (By.XPATH, "//button[text()='确定']")
    # 新增客户成功的校验--提示
    loc_save_cust_success = (By.XPATH, "//font[text()='客户信息保存成功，请选择下一步操作']")
    # 新增贷款信息
    loc_addLoan = (By.ID, "addLoan.OperateWin")
    # 继续填写其他信息按钮
    loc_addMoreMsg = (By.ID, "addMoreMsg.OperateWin")
    # 新增下一客户按钮
    loc_addNext = (By.ID, "addNext.OperateWin")
    # 新增客户页面的右上角关闭按钮
    loc_close = (By.XPATH, "//div[@class='x-tool x-tool-close']")
    # 客户查询结果：//div[@class='x-grid3-body']
    loc_customer_count = (By.XPATH, "//div[@class='x-grid3-body']/div")

    # 选择第一条客户
    loc_choose_cust = (By.XPATH, "//div[@class='x-grid3-body']/div[1]")
    # 提交按钮
    loc_tijiao = (By.XPATH, "//button[text()='提交']")

    # 选择产品
    loc_choose_prod = (By.ID, "prodNo.ChooseProductWin")
    # 选择简化信贷
    loc_jhxd = (By.XPATH, "//div[text()='简化信贷1218-yi']")
    # 简化信贷，默认为普通贷款，本模块为授信产品，所以选择授信
    loc_jhxd_sx = (By.XPATH, "//label[text()='授信']")
    # 选择 外部输入产品，产品为6开头
    loc_outer_prod = (By.XPATH, "//div[text()='龙川转贷']")
    # 确定按钮
    loc_sure = (By.ID, "btOk.SetPayDate")
