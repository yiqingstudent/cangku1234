#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : jhxd_page.py
@Author: rebecca
@Date  : 2020/6/3 9:52
@Desc  : 
"""
from selenium import webdriver
from PageLocators.jhxd_page_loc import JianXdPageLoc as loc
from Common.basepage import BasePage
from time import sleep


class JianHuaXdMain(BasePage):
    # 继承了basepage的类，就可以直接使用里面的函数了~
    # 申明是webdriver的类型，就可以直接使用self.
    # def __init__(self, driver:WebDriver):
    #     self.driver = driver
    #     self.BasePage = BasePage(self.driver)

    # 进入菜单：菜单-监管评级-供应链核心企业维护
    def click_menu(self):
        self.move_to_click(loc.business_loc, "菜单-信贷业务")
        self.click_ele_success(loc.loc_yw_apply, "菜单-业务申请办理")

    # 查询操作，新增结束之后，进行查找
    def query_customer_loan(self, name):
        """
        :param name: 根据客户姓名进行查询操作
        :return:
        """
        self.driver.switch_to.frame("content_iframe")
        self.input_element_value(loc.loc_cust_name, name, "客户名称-输入框")
        self.click_ele_success(loc.loc_query, "查询客户页面")

    def get_customer_count(self):
        """
        根据查询条件，返回查询结果-个数
        :return:
        """
        return self.get_elements_texts(loc.loc_customer_count, "客户查询-返回个数")

    # 新增操作:进入新的frame，点击新增按钮，输入正确的数据
    def add_cust_data(self, name, paperNo, phoneNo, flag=1):
        """
        :param name:客户名称
        :param paperNo:身份号码
        :param phoneNo:手机号码
        :param flag: 1-表示自营 2-表示第三方
        :return:
        """
        self.driver.switch_to.frame("content_iframe")
        self.click_ele_success(loc.loc_bus_add, "业务申请办理-新增业务按钮")
        self.input_element_value(loc.loc_custName_BC, name, "BuildCustMgrPnl-输入客户名称")
        self.click_ele_success(loc.loc_custName_query, "BuildCustMgrPnl-查询按钮")
        sleep(1)
            # # 如果返回不为空，那么直接选择第一条开始：
            # self.click_ele_success(loc.loc_choose_cust, "选择客户页面-选择查询中的这个")
            # self.click_ele_success(loc.loc_tijiao, "选择客户页面-提交按钮")
            # 如果返回为空，那么新增客户进行后续流程：
        self.click_ele_success(loc.loc_add_cust, "BuildCustMgrPnl-新客户按钮")
        self.input_element_value(loc.loc_custName, name, "RegisterCustInfoWin-输入客户名称")
        self.input_element_value(loc.loc_paperNo, paperNo, "RegisterCustInfoWin-输入身份证号码")
        self.input_element_value(loc.loc_phoneNo, phoneNo, "RegisterCustInfoWin-输入手机证号码")
        self.click_ele_success(loc.loc_cust_typeSource, "RegisterCustInfoWin-选择客户来源")
        if flag == 1:
            self.click_ele_success(loc.loc_cust_typeSource_first, "RegisterCustInfoWin-选择自营")
        else:
            self.click_ele_success(loc.loc_cust_typeSource_second, "RegisterCustInfoWin-选择第三方")
        self.click_ele_success(loc.loc_cust_cdeSource, "RegisterCustInfoWin-选择客户来源名称")
        self.click_ele_success(loc.loc_cust_cdeSource_first, "RegisterCustInfoWin-选择客户来源名称第一个")
        self.click_ele_success(loc.loc_register, "RegisterCustInfoWin-用户注册")
        self.click_ele_success(loc.loc_yes, "RegisterCustInfoWin-选择是")
        self.click_ele_success(loc.loc_sure_cust, "RegisterCustInfoWin-选择确定")
        return name

    def enter_choose_product(self, is_outer=1):
        """
        :param is_outer: 1默认为简化信贷模板，非1为其他类型的模板，根据需要进行添加
        :return:
        """
        self.click_ele_success(loc.loc_addLoan, "点击新增贷款-进入选择产品和贷款页面")
        self.click_ele_success(loc.loc_choose_prod, "选择客户页面-产品类型")
        if is_outer == 1:
            self.click_ele_success(loc.loc_jhxd, "选择产品页面-简化信贷产品模板")
        else:
            self.click_ele_success(loc.loc_outer_prod, "选择产品页面-外部输入产品模板")
        self.click_ele_success(loc.loc_sure, "选择产品页面-点击确定按钮")

    # def enter_choose_product(self):
    #     self.click_ele_success(loc.loc_addLoan, "点击新增贷款-进入选择产品和贷款页面")
    #     self.click_ele_success(loc.loc_choose_prod, "选择客户页面-产品类型")
    #     self.click_ele_success(loc.loc_jhxd, "选择产品页面-简化信贷产品模板")
    #     self.click_ele_success(loc.loc_sure, "选择产品页面-点击确定按钮")

    def loan_apply_detail(self, applamt, applPerd, remark):
        """
        :param applamt: 贷款金额-输入项
        :param applPerd: 贷款期限-输入项
        :param remark: 备注
        :return:
        """
        self.input_element_value(loc.loc_applamt, applamt, "贷款申请的详情页面-输入贷款金额")
        self.input_element_value(loc.loc_applPerd, applPerd, "贷款申请的详情页面-输入贷款期限")
        self.click_ele_success(loc.loc_mainGurTyp, "贷款申请的详情页面-触发担保方式输入框")
        self.click_ele_success(loc.loc_mainGurTyp_first, "贷款申请的详情页面-选择担保方式第一条")
        self.click_ele_success(loc.loc_loanUse, "贷款申请的详情页面-触发借款事由的输入框")
        self.click_ele_success(loc.loc_loanUse_first, "贷款申请的详情页面-选择借款事由的第一条")
        self.click_ele_success(loc.loc_typeSource, "贷款申请的详情页面-触发贷款来源类型的输入框")
        self.click_ele_success(loc.loc_typeSource_first, "贷款申请的详情页面-选择贷款来源类型的第一条")
        self.click_ele_success(loc.loc_cdeSource, "贷款申请的详情页面-触发贷款来源名称型的输入框")
        self.click_ele_success(loc.loc_cdeSource_first, "贷款申请的详情页面-选择贷款来源名称的第一条")
        self.input_element_value(loc.loc_remark, remark, "贷款申请的详情页面-贷款描述")
        self.click_ele_success(loc.loc_save, "贷款申请的详情页面-点击保存按钮")

    def save_sure_submit(self):
        self.click_ele_success(loc.loc_sure_save, "贷款申请的详情页面-点击确定按钮")
        sleep(0.5)
        self.click_ele_success(loc.loc_submit, "贷款申请的详情页面-点击提交按钮")
        self.click_ele_success(loc.loc_submit_sure, "贷款申请的详情页面-点击确定按钮以便进入下一个调查录入页面")

    def loan_data_basic(self, intStartDt, lastDueDt, gracePerdP, graceInt, is_dq=1):
        """
        :param intStartDt: 起息日
        :param gracePerdP: 本金宽限期
        :param graceInt: 利息宽限期
        :param is_dq: 是否中长期,1表示短期，非1表示长期
        :return:
        """
        self.execute_js_date(loc.loc_intStartDt, intStartDt, "调查录入-贷款基本信息-起息日")
        self.execute_js_date(loc.loc_lastDueDt, lastDueDt, "调查录入-贷款基本信息-到期日")
        self.click_ele_success(loc.loc_loanObj, "调查录入-贷款基本信息-点击贷款对象按钮")
        self.click_ele_success(loc.loc_loanObj_first, "调查录入-贷款基本信息-选择农户")
        self.click_ele_success(loc.loc_zjtx, "调查录入-贷款基本信息-点击资金投向")
        # 资金投向具体内容，需要进入iframe：epFlowFrm.EncodingListQueryWin
        self.driver.switch_to.frame("epFlowFrm.EncodingListQueryWin")
        self.click_ele_success(loc.loc_zjtx_query, "调查录入-贷款基本信息-资金投向-查询按钮")
        self.click_ele_success(loc.loc_zjtx_first, "调查录入-贷款基本信息-资金投向-查询按钮-选择第一个")
        self.driver.switch_to.parent_frame()
        self.execute_scroll_view(loc.loc_zjtx_submit, "调查录入-贷款基本信息-资金投向-确认按钮滚到可视区域")
        self.click_ele_success(loc.loc_zjtx_submit, "调查录入-贷款基本信息-资金投向-查询按钮-选择第一个-确认")

        self.click_ele_success(loc.loc_prdctCde, "调查录入-贷款基本信息-点击贷款品种")
        if is_dq == 1:
            self.click_ele_success(loc.loc_dq_first, "调查录入-贷款基本信息-贷款品种-选择短期-信用")
        else:
            self.click_ele_success(loc.loc_zcq_first, "调查录入-贷款基本信息-贷款品种-选择中长期-信用")
        self.click_ele_success(loc.loc_crdtNo, "调查录入-贷款基本信息-点击贷款合同号")
        self.double_click_success(loc.loc_crdtNo_first, "调查录入-贷款基本信息-选择第一个贷款合同号")
        self.input_element_value(loc.loc_gracePerdP, gracePerdP, "调查录入-贷款基本信息-本金宽限期")
        self.input_element_value(loc.loc_graceInt, graceInt, "调查录入-贷款基本信息-利息宽限期")

    def loan_data_repayTyp(self, dueday, intRate, odIntRatePrcp, repayTyp=1, rateMode=1, odint=1):
        """
        :param intRate:执行年利率
        :param odIntRatePrcp: 罚息利率
        :param repayTyp:1-等额本息，2-等额本金，3-按期还息到期还本，4-利随本清
        :param rateMode:基础利率模式 1-可调整利率 2-固定利率
        :param odint:罚息利率 1-按固定值 2-按浮动比
        :return:
        """
        self.click_ele_success(loc.loc_repayTyp, "调查录入-还款属性-点击还款方式")
        if repayTyp == 1:
            self.click_ele_success(loc.loc_debx, "调查录入-还款属性-等额本息")
        elif repayTyp == 2:
            self.click_ele_success(loc.loc_debj, "调查录入-还款属性-等额本金")
        elif repayTyp == 3:
            self.click_ele_success(loc.loc_aqhxdqhb, "调查录入-还款属性-按期还息到期还本")
        else:
            self.click_ele_success(loc.loc_lsbq, "调查录入-还款属性-利随本清")
        self.click_ele_success(loc.loc_dueday, "调查录入-点击约定还款日")
        self.click_ele_success(loc.loc_rateMode, "调查录入-还款属性-点击基础利率模式")
        self.clear_ele_success(loc.loc_dueday, "调查录入-还款属性-清空约定还款日")
        self.input_element_value(loc.loc_dueday, dueday, "调查录入-还款属性-输入约定还款日")
        if rateMode == 1:
            self.click_ele_success(loc.loc_ktz, "调查录入-还款属性-基础利率模式：可调整利率")
        else:
            self.click_ele_success(loc.loc_gdlv, "调查录入-还款属性-基础利率模式：固定利率")
        self.input_element_value(loc.loc_intRate, intRate, "调查录入-还款属性-输入执行年利率")
        self.click_ele_success(loc.loc_odIntRateTyp, "调查录入-还款属性-点击罚息利率下拉框")
        if odint == 1:
            self.click_ele_success(loc.loc_agdz, "调查录入-还款属性-罚息利率:按固定值")
        else:
            self.click_ele_success(loc.loc_afdb, "调查录入-还款属性-罚息利率:按浮动比")
        self.input_element_value(loc.loc_odIntRatePrcp, odIntRatePrcp, "调查录入-还款属性-输入年化收益率")

    def loan_data_businessnature(self, collection, collectionNo, guarNo, zfb, bus_nature=1, cust_nature=1, ywlx=1):
        """
        :param collection:是否托收
        :param collectionNo:托收账号
        :param guarNo:担保合同号
        :param zfb:支付宝账号
        :param bus_nature:业务性质-下拉框，1-自营 2-公司
        :param cust_nature:客户性质-下拉框，1-新增 2-存量
        :param ywlx:业务类型-下拉框，1-新增 2-存量 3-并行
        :return:
        """
        self.click_ele_success(loc.loc_businessNature, "调查录入-业务性质-点击业务性质下拉框")
        if bus_nature == 1:
            self.click_ele_success(loc.loc_business_zy, "调查录入-业务性质-业务性质:自营")
        else:
            self.click_ele_success(loc.loc_business_gs, "调查录入-业务性质-业务性质:公司")
        self.click_ele_success(loc.loc_custNature, "调查录入-业务性质-点击客户性质下拉框")
        if cust_nature == 1:
            self.click_ele_success(loc.loc_cust_xz, "调查录入-业务性质-客户性质:新增")
        else:
            self.click_ele_success(loc.loc_cust_cl, "调查录入-业务性质-客户性质:存量")
        self.input_element_value(loc.loc_collection, collection, "调查录入-业务性质-输入是否托收")
        self.input_element_value(loc.loc_collectionNo, collectionNo, "调查录入-业务性质-托收账号")
        self.input_element_value(loc.loc_guarNo, guarNo, "调查录入-业务性质-担保合同号")
        self.click_ele_success(loc.loc_ywlx, "调查录入-业务性质-点击业务类型下拉框")
        if ywlx == 1:
            self.click_ele_success(loc.loc_ywlx_xz, "调查录入-业务性质-业务类型:新增")
        elif ywlx == 2:
            self.click_ele_success(loc.loc_ywlx_xd, "调查录入-业务性质-业务类型:续贷")
        else:
            self.click_ele_success(loc.loc_ywlx_bx, "调查录入-业务性质-业务类型:并行")
        self.input_element_value(loc.loc_zfb, zfb, "调查录入-业务性质-支付宝账号")

    def gen_reapy_sch(self):
        self.click_ele_success(loc.loc_btnGenSchd, "调查录入-点击生成还款计划表")
        sleep(0.5)
        self.execute_scroll_view(loc.loc_pay_save, "调查录入-拖到最底部找到保存按钮")
        self.click_ele_success(loc.loc_pay_save, "调查录入-点击保存按钮")

    def save_success_click(self):
        self.click_ele_success(loc.loc_sys_tips_yes, "调查录入-是否保存？是")
        self.click_ele_success(loc.loc_save_ok, "保存成功！")
        self.click_ele_success(loc.loc_save_sure, "保存成功弹出框的的确定按钮")
        sleep(1)
        self.click_ele_success(loc.loc_submitBt, "调查录入-点击提交按钮")
        self.click_ele_success(loc.loc_sys_tips_sure, "调查录入-点击提确定按钮")

    def get_message_from_save_success(self):
        return self.get_element_text(loc.loc_success_info, "贷款申请的详情页面-保存成功的提示框内容")

    def get_message_from_submit_success(self):
        return self.get_element_text(loc.loc_submit_success, "贷款申请的详情页面-提交成功的提示框内容")

    def get_message_from_loan_Save_success(self):
        return self.get_element_text(loc.loc_sys_tips, "简化信贷-贷款申请成功的系统提示")

    def get_mssage_from_loan_shenpi_success(self):
        return self.get_element_text(loc.loc_loan_sp_ok, "简化信贷-贷款审批成功的系统提示")

    def check_qianyue_exist(self):
        return self.check_elements_exist(loc.loc_contract_sign, "简化信贷-贷款审批成功的页面校验")

    def contract_sign(self):
        """
        有页面刷新，需要等待一下
        :return:
        """
        self.click_ele_success(loc.loc_contract_sign_in, "简化信贷--合同签约-点击进入")
        sleep(1)
        self.execute_scroll_view(loc.loc_contract_sign_save, "简化信贷--合同签约--滚动页面将保存按钮给展示出来")
        self.click_ele_success(loc.loc_contract_sign_save, "简化信贷--合同签约-点击进入-点击保存按钮")
        self.click_ele_success(loc.loc_contract_sign_check, "简化信贷--合同签约-点击进入-点击确认是否保存按钮")
        self.click_ele_success(loc.loc_contract_sign_sure, "简化信贷--合同签约-点击进入-点击是")
        sleep(0.5)
        self.click_ele_success(loc.loc_contract_sign_submit, "简化信贷--合同签约-点击进入-点击提交按钮")
        self.click_ele_success(loc.loc_contract_kj_sure, "简化信贷--合同签约-点击进入-点击提确认按钮")


