#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : baseapprove.py
@Author: rebecca
@Date  : 2020/4/9 15:24
@Desc  : 
"""

from Common.public_func import PublicFunc


class ApproveManager:
    def __init__(self, driver):
        self.driver = driver
        self.test = PublicFunc(driver)

    def actionContinue(self, submitAuditInfo, continueType, name=None, phone=None):
        '''
                Desc:个人审批继续提交审批
                Args:
                    continueType:继续提交的类型，0为个人审批，1为岗位审批，2为短信审批
                    name:为要提交的人或岗位
                    phone:为短信审批发送的手机号码
        '''
        pass

    def actionSingleAudit(self, auditType, action, remark=None,
                          continueType=None, name=None, phone=None):
        """
        进行个人审批
        :param auditType: 审批的类型,对哪种交易进行审批
        :param action: 审批的动作:退回申请人,同意审批,拒绝审批,继续提交
        :param remark: 审批意见
        :param continueType: 继续提交的类型，0为个人审批，1为岗位审批，2为短信审批
        :param name: 为要提交的人或岗位
        :param phone: 为短信审批发送的手机号码
        :return:
        """
        pass

    def postActionAudit(self, auditType, action, remark=None, continueType=None, name=None, phone=None):
        """
        :param auditType:审批的类型,对哪种交易进行审批
        :param action:审批的动作:退回申请人,同意,拒绝,继续提交
        :param remark:审批意见
        :param continueType:继续提交的类型，0为个人审批，1为岗位审批，2为短信审批
        :param name:为要提交的人或岗位
        :param phone:为短信审批发送的手机号码
        :return:
        """
        pass

