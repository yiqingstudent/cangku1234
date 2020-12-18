#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : qywh_datas.py
@Author: rebecca
@Date  : 2020/4/28 14:42
@Desc  : 
"""
from Common.create_number import CreateNumber

# 以下为新增功能
# 企业名称+组织机构代码证+备注
cm = CreateNumber()
success_org_data = {
    "qy_name": cm.create_enterprise_name(),
    "org_code": cm.create_organization(),
    "check—info": "保存成功"}

# 企业名称+社会信用代码证+备注
success_social_data = {
    "qy_name": cm.create_enterprise_name(),
    "social_code": cm.create_social_credit(),
    "check—info": "保存成功"}
