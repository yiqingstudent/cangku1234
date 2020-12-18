#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : test_login.py
@Author: rebecca
@Date  : 2020/4/2 15:35
@Desc  : 
"""
import logging
from Common import logger
from selenium import webdriver
from PageObjects.home_page import HomePage
from PageObjects.login_page import LoginPage
from TestDatas.Common_Datas import CommonDatas
from TestDatas.login_datas import LoginDatas as LD
import pytest


@pytest.fixture(scope="function")  # 默认是用例级别的，就是目前的。可以为空
def init_login(init_driver):
    lp = LoginPage(init_driver)
    yield {"driver": init_driver, "lp": lp}


# 可以定义多个前置后置
@pytest.fixture(scope="class")
def demo_class():
    print("##################测试类级别的：用例开始#######################")
    yield
    print("##################测试类级别的：用例结束########################")


@pytest.mark.usefixtures("demo_class")  # 这个类下面的所有测试案例都是绑定这个前置后置条件
@pytest.mark.xwd_jianhuaxindai  # 这是在类前面打的标记，证明下面的测试用例全部含有xwd-简化信贷的标记哦！理论上只打在用例上
class TestLogin:
    @pytest.mark.usefixtures("init_login")  # 这个类下面的所有测试案例都是绑定这个前置后置条件
    @pytest.mark.smoke  # 打标记，mark+标记名，这一层是在测试用例前面打
    def test_login_success(self, init_login):  # fixture 函数名作为用例的参数==返回值
        logging.info("***************d登录功能开始******************")
        # 操作步骤，调用登录页面的登录方法，包含输入用户名和密码
        init_login["lp"].login(CommonDatas.user_name, CommonDatas.password)
        # 开始断言
        assert HomePage(init_login["driver"]).check_user_exist()
        # 断言2：
        assert init_login["driver"].current_url, CommonDatas.home_url

    @pytest.mark.parametrize("test_info", LD.wrong_datas)
    @pytest.mark.usefixtures("init_login")  # 这个类下面的所有测试案例都是绑定这个前置后置条件
    def test_login_failed(self, test_info, init_login):
        # 异常用例
        # 操作步骤，调用登录页面的登录方法，包含输入用户名和密码
        init_login["lp"].login(test_info["user_name"], test_info["password"])
        # 断言-登录页面有提示信息
        assert init_login["lp"].get_error_message(), test_info['check—info']

    @pytest.mark.smoke
    @pytest.mark.usefixtures("module_gl")
    def test_01(self):
        print("hello,python")



