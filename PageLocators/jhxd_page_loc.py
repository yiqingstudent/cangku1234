#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : jhxd_page_loc.py
@Author: rebecca
@Date  : 2020/6/3 9:52
@Desc  : 
"""
from selenium.webdriver.common.by import By


class JianXdPageLoc:
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
    # 简化信贷，默认为普通贷款，也可以选择授信
    loc_jhxd_sx = (By.XPATH, "//label[text()='授信']")
    # 选择 外部输入产品，产品为6开头
    loc_outer_prod = (By.XPATH, "//div[text()='龙川转贷']")
    # 确定按钮
    loc_sure = (By.ID, "btOk.SetPayDate")
    # 申请金额
    loc_applamt = (By.ID, "applAmt.LoanApplyDetailPanel")
    # 贷款期限applPerd.LoanApplyDetailPanel
    loc_applPerd = (By.ID, "applPerd.LoanApplyDetailPanel")
    # 担保方式 mainGurTyp.LoanApplyDetailPanel
    loc_mainGurTyp = (By.ID, "mainGurTyp.LoanApplyDetailPanel")
    # 担保方式01 --信用
    loc_mainGurTyp_01 = (By.XPATH, "//div[text()='信用']")
    # 担保方式02 --质押
    loc_mainGurTyp_02 = (By.XPATH, "//div[text()='质押']")
    # 担保方式03 --保证
    loc_mainGurTyp_03 = (By.XPATH, "//div[text()='保证']")
    # 担保方式04 --抵押
    loc_mainGurTyp_04 = (By.XPATH, "//div[text()='抵押']")
    # 选择担保方式的下拉框的第一项（共4项）
    loc_mainGurTyp_first = (By.XPATH, "//div[@class='x-layer x-combo-list '][1]//div[2]")

    # 借款事由
    loc_loanUse = (By.ID, "loanUse.LoanApplyDetailPanel")
    # 借款事由01--经营、创业、买房-居住、买房-商用、买车、助学、装修、日常消费、其他
    loc_loanUse_01 = (By.XPATH, "//div[text()='经营']")
    loc_loanUse_02 = (By.XPATH, "//div[text()='创业']")
    loc_loanUse_03 = (By.XPATH, "//div[text()='买房-居住']")
    loc_loanUse_04 = (By.XPATH, "//div[text()='买房-商用']")
    loc_loanUse_05 = (By.XPATH, "//div[text()='买车']")
    loc_loanUse_06 = (By.XPATH, "//div[text()='助学']")
    loc_loanUse_07 = (By.XPATH, "//div[text()='装修']")
    loc_loanUse_08 = (By.XPATH, "//div[text()='日常消费']")
    loc_loanUse_09 = (By.XPATH, "//div[text()='其他']")
    # 选择借款事由的下拉框第一项（共9项）
    loc_loanUse_first = (By.XPATH, "//div[@class='x-layer x-combo-list '][2]//div[2]")

    # 贷款来源类型
    loc_typeSource = (By.ID, "typeSource.LoanApplyDetailPanel")
    # 贷款来源类型--第三合作机构、自营
    loc_typeSource_01 = (By.XPATH, "//div[text()='第三合作机构']")
    loc_typeSource_02 = (By.XPATH, "//div[text()='自营']")
    # 选择贷款来源的下拉框第一项（共2项）
    loc_typeSource_first = (By.XPATH, "//div[@class='x-layer x-combo-list '][3]//div[2]")

    #  贷款来源名称
    loc_cdeSource = (By.ID, "cdeSource.LoanApplyDetailPanel")
    # 贷款来源名称 选择贷款来源名城--下拉框第一个值（不确定是几项，看配置）
    loc_cdeSource_first = (By.XPATH, "//div[@class='x-layer x-combo-list '][4]//div[2]")

    # 备注 name="applRemark"
    loc_remark = (By.XPATH, "//textarea[@name='applRemark']")

    # 保存按钮
    loc_save = (By.ID, "btnSave")
    # 保存成功的提示框
    loc_success_info = (By.XPATH, '//span[text()="保存成功"]')
    # 确定按钮
    loc_sure_save = (By.XPATH, '//button[text()="确定"]')
    # 提交按钮  btnSubmit
    loc_submit = (By.XPATH, "//table[@id='btnSubmit']//button[text()='提交']")
    # 提交成功
    loc_submit_success = (By.XPATH, "//span[@class='ext-mb-text']")
    # 确定按钮
    loc_submit_sure = (By.XPATH, "//button[@class=' x-btn-text' and text()='确定']")

    # 录入调查页面--贷款基本信息
    # 贷款对象：
    # 起息日：
    loc_intStartDt = (By.ID, "intStartDt.LoanDataInputPanel")
    # 到期日：
    loc_lastDueDt = (By.ID, "lastDueDt.LoanDataInputPanel")
    # 贷款金额：
    loc_loan_amt = (By.ID, "exapAmt.LoanDataInputPanel")
    # 贷款对象以及贷款对象下拉框的第一个取值
    loc_loanObj = (By.XPATH, "//input[@id='loanObj.LoanDataInputPanel']")
    loc_loanObj_first = (By.XPATH, "//div[@class='x-layer x-combo-list '][1]//div[2]")
    # 资金投向
    loc_zjtx = (By.XPATH, "//button[text()='选择']")
    # 资金投向-查询
    loc_zjtx_query = (By.XPATH, "//button[text()='查询']")
    # 选择第一个
    loc_zjtx_first = (By.XPATH, "//div[@class='x-grid3-body']/div[1]")
    # 确认  //button[text()='保存']
    loc_zjtx_submit = (By.XPATH, "//table[@id='btnSubmit.EncodingListQuery']//button[text()='确认']")
    # 贷款品种
    loc_prdctCde = (By.ID, "prdctCde.LoanDataInputPanel")
    # 贷款品种--默认选择第一个 农户贷款短期-信用
    loc_dq_first = (By.XPATH, "//div[text()='农户贷款短期-信用']")
    loc_dq_second = (By.XPATH, "//div[text()='个人受托贷款短期-信用']")
    loc_zcq_first = (By.XPATH, "//div[text()='农户贷款中长期-信用']")
    loc_zcq_second = (By.XPATH, "//div[text()='个人受托贷款中长期-信用']")
    # 选择第二项
    loc_prdctCde_second = (By.XPATH, "//div[@class='x-layer x-combo-list '][2]//div[@class='x-combo-list-item']")

    # 贷款合同号
    loc_crdtNo = (By.ID, "crdtNo.LoanDataInputPanel")
    # 贷款合同号——
    loc_crdtNo_first = (By.XPATH, "//div[@class='x-layer x-combo-list '][3]//div[@class='x-grid3-body']/div[1]")
    # 本金宽限期
    loc_gracePerdP = (By.ID, "gracePerdP.LoanDataInputPanel")
    # 利息宽限期
    loc_graceInt = (By.ID, "gracePerdI.LoanDataInputPanel")

    #录入调查页面--还款属性
    loc_repayTyp = (By.ID, "repayTyp.LoanDataInputPanel")
    # 等额本息
    loc_debx = (By.XPATH, "//div[text()='等额本息']")
    # 等额本金
    loc_debj = (By.XPATH, "//div[text()='等额本金']")
    # 按期还息到期还本
    loc_aqhxdqhb = (By.XPATH, "//div[text()='按期还息到期还本']")
    # 利随本清
    loc_lsbq = (By.XPATH, "//div[text()='利随本清']")

    # 约定还款日
    loc_dueday = (By.ID, "dueDay.LoanDataInputPanel")

    # 基础利率模式
    loc_rateMode = (By.ID, "rateMode.LoanDataInputPanel")
    # 基础利率模式——
    loc_ktz = (By.XPATH, "//div[text()='可调整利率']")
    # 基础利率模式——
    loc_gdlv = (By.XPATH, "//div[text()='固定利率']")
    # 执行年利率
    loc_intRate = (By.ID, "intRate.LoanDataInputPanel")
    # 罚息利率
    loc_odIntRateTyp = (By.ID, "odIntRateTyp.LoanDataInputPanel")
    # 罚息利率-按固定值
    loc_agdz = (By.XPATH, "//div[text()='按固定值']")
    # 罚息利率-按浮动比
    loc_afdb = (By.XPATH, "//div[text()='按浮动比']")
    # 年华--收益率
    loc_odIntRatePrcp = (By.ID, "odIntRatePrcp.LoanDataInputPanel")

    # 录入调查页面 -业务性质
    # 业务性质--
    loc_businessNature = (By.ID, "businessNature.LoanDataInputPanel")
    loc_business_zy = (By.XPATH, "//div[text()='自营']")
    loc_business_gs = (By.XPATH, "//div[text()='公司']")
    # 客户性质
    loc_custNature = (By.ID, "custNature.LoanDataInputPanel")
    loc_cust_xz = (By.XPATH, "//div[text()='新增']")
    loc_cust_cl = (By.XPATH, "//div[text()='存量']")
    # 是否托收 collection.LoanDataInputPanel
    loc_collection = (By.ID, "collection.LoanDataInputPanel")
    # 托收账号
    loc_collectionNo = (By.ID, "collectionNo.LoanDataInputPanel")
    # 担保合同号
    loc_guarNo = (By.ID, "gurContNo.LoanDataInputPanel")
    # 业务类型 ywlx.LoanDataInputPanel
    loc_ywlx = (By.ID, "ywlx.LoanDataInputPanel")
    # 业务类型-01
    loc_ywlx_xz = (By.XPATH, "//div[text()='新增']")
    loc_ywlx_xd = (By.XPATH, "//div[text()='续贷']")
    loc_ywlx_bx = (By.XPATH, "//div[text()='并行']")
    # 支付宝账号
    loc_zfb = (By.ID, "zfbNo.LoanDataInputPanel")

    # 录入调查页面 -生成还款计划表
    # 生成还款计划
    #loc_GenPay = (By.ID, "LoanDataInputBtnGenPay")
    loc_btnGenSchd = (By.XPATH, '//font[text()="生成还款计划"]')
    # 拖到最底部，保存按钮  //table[@id="btnLoanDataSave"]//button[text()='保存']

    loc_pay_save = (By.XPATH, "//button[text()='保存']")
    # 系统提示：//div[text()='请确认以上贷款信息，是否保存？']
    loc_sys_tips = (By.XPATH, "//div[text()='请确认以上贷款信息，是否保存？']")
    # 系统提示：是
    loc_sys_tips_yes = (By.XPATH, "//table[@id='yesBtn.XttsOtWin']//button[text()='是']")
    # 保存成功
    loc_save_ok = (By.XPATH, '//span[text()="保存成功！"]')
    # 保存成功提示信息的---确定按钮
    loc_save_sure = (By.XPATH, '//button[text()="确定"]')
    # 提交还款计划表
    loc_submitBt = (By.XPATH, "//table[@id='submitBt']//button[text()='提交']")
    # 系统提示--贷款审批成功！
    loc_loan_sp_ok = (By.XPATH, "//span[text()='贷款审批成功！']")
    # 点击确定按钮
    loc_sys_tips_sure = (By.XPATH, '//button[text()="确定"]')
    # 贷款审批成功之后--签约信息
    loc_contract_sign = (By.XPATH, "//span[text()='合同签约']")
    # 合同签约---点击进入按钮
    loc_contract_sign_in = (By.XPATH, "//h1[text()='合同签约']/following-sibling::button[1]")
    # 合同签约--保存
    loc_contract_sign_save = (By.XPATH, "//table[@id='btSave']//button[text()='保存']")
    # 合同签约--确认是否保存
    loc_contract_sign_check = (By.XPATH, "//button[text()='是']")
    # 合同签约--是--保存成功！--确定
    loc_contract_sign_sure = (By.XPATH, "//button[text()='确定']")
    # 合同签约-提交
    loc_contract_sign_submit = (By.XPATH, "//button[text()='提交']")
    # 系统提示--合同生成成功，请会计放款
    loc_contract_sign_tips = (By.XPATH, "//button[text()='合同生成成功，请会计放款']")
    # 系统提示--合同生成成功，请会计放款--确定
    loc_contract_kj_sure = (By.XPATH, "//button[text()='确定']")






























