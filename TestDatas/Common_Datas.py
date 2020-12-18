#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : Common_Datas.py
@Author: rebecca
@Date  : 2020/4/2 11:13
@Desc  : 创建文件，全局的数据-公共信息
"""


class CommonDatas:
    # 服务器方位的base_url
    base_url = "http://172.31.19.96/pubsys"
    base_url_zjtj = "http://172.31.19.71/pubsys"
    # 登录地址
    login_url = base_url + "/login.jsp"
    login_url_zjtj = base_url_zjtj + "/login.jsp"
    # 登录成功首页地址
    home_url = base_url + "/com/main.jsp"

    # 以下为 客户经理-账号
    user_name = "J3205823010050"
    password = "123123"

    # 以下为 小贷公司管理员账号
    administrator_name = "qianhuili"
    administrator_password = "123123"

    # 以下为 资金调剂账号
    zjtj_name = "yushikui"
    zjtj_password = "123123"


