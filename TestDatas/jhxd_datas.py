#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : jhxd_datas.py
@Author: rebecca
@Date  : 2020/6/3 15:11
@Desc  : 
"""
from Common.create_number import CreateNumber

# 以下为新增功能
# 个人客户+证件号码+手机号码
cm = CreateNumber()
success_customer_data = [
    {"cname": cm.create_customer_name(), "paperNo": cm.generate_id(),"phoneNo": cm.create_phone(),"check—info": "保存成功"},
    {"cname": cm.create_customer_name(), "paperNo": cm.generate_id(),"phoneNo": cm.create_phone(),"check—info": "保存成功"},
    {"cname": cm.create_customer_name(), "paperNo": cm.generate_id(),"phoneNo": cm.create_phone(),"check—info": "保存成功"},
    {"cname": cm.create_customer_name(), "paperNo": cm.generate_id(),"phoneNo": cm.create_phone(),"check—info": "保存成功"},
    {"cname": cm.create_customer_name(), "paperNo": cm.generate_id(),"phoneNo": cm.create_phone(),"check—info": "保存成功"},
    {"cname": cm.create_customer_name(), "paperNo": cm.generate_id(),"phoneNo": cm.create_phone(),"check—info": "保存成功"},
    {"cname": cm.create_customer_name(), "paperNo": cm.generate_id(),"phoneNo": cm.create_phone(),"check—info": "保存成功"},
    {"cname": cm.create_customer_name(), "paperNo": cm.generate_id(),"phoneNo": cm.create_phone(),"check—info": "保存成功"},
    {"cname": cm.create_customer_name(), "paperNo": cm.generate_id(),"phoneNo": cm.create_phone(),"check—info": "保存成功"},
    {"cname": cm.create_customer_name(), "paperNo": cm.generate_id(),"phoneNo": cm.create_phone(),"check—info": "保存成功"},
    {"cname": cm.create_customer_name(), "paperNo": cm.generate_id(),"phoneNo": cm.create_phone(),"check—info": "保存成功"},
    {"cname": cm.create_customer_name(), "paperNo": cm.generate_id(),"phoneNo": cm.create_phone(),"check—info": "保存成功"},
    {"cname": cm.create_customer_name(), "paperNo": cm.generate_id(),"phoneNo": cm.create_phone(),"check—info": "保存成功"},
    {"cname": cm.create_customer_name(), "paperNo": cm.generate_id(),"phoneNo": cm.create_phone(),"check—info": "保存成功"},
    {"cname": cm.create_customer_name(), "paperNo": cm.generate_id(),"phoneNo": cm.create_phone(),"check—info": "保存成功"},
    {"cname": cm.create_customer_name(), "paperNo": cm.generate_id(),"phoneNo": cm.create_phone(),"check—info": "保存成功"}
]
# print(success_customer_data)
# 企业客户名称+组织机构代码证+备注
success_enterprise_data = {
    "qy_name": cm.create_enterprise_name(),
    "org_code": cm.create_organization(),
    "check—info": "保存成功"}