#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : conftest.py
@Author: rebecca
@Date  : 2020/6/2 15:08
@Desc  :
专们用来前置后置共享，当前文件所在目录以及子目录下的用例，均可以调用当中的fixtures
而且是就近原则，自己本目录下有，然后再往外找
名字固定为：conftest.py
"""
import pytest
from selenium import webdriver

from PageObjects.login_page import LoginPage
from TestDatas.Common_Datas import CommonDatas


@pytest.fixture(scope="function")  # 默认是用例级别的，就是目前的。可以为空
def init_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CommonDatas.login_url)
    #lp = LoginPage(driver)
    print("############测试案例级别的：测试开始##############")
    # 前置
    yield driver
    # 后置
    driver.quit()
    print("#############测试案例级别：用例结束##############")

# 客户经理账号登录成功!作为前置后置,可以继承上面的打开浏览器init_driver
@pytest.fixture()
def login_khjl_success(init_driver): # 调用了上面的init_driver且用了init_driver的返回值
    LoginPage(init_driver).login(CommonDatas.user_name, CommonDatas.password)
    yield init_driver

# 如果在用例中调用login_success登录成功
"""
init_driver--前置
login_success--前置
login_success--后置
init_driver--后置
"""
# 小贷公司管理员账号登录成功!作为前置后置,可以继承上面的打开浏览器init_driver
@pytest.fixture()
def login_administrator_success(init_driver): # 调用了上面的init_driver且用了init_driver的返回值
    LoginPage(init_driver).login(CommonDatas.administrator_name, CommonDatas.administrator_password)
    yield init_driver


# 资金调剂账号登录成功!作为前置后置,可以继承上面的打开浏览器init_driver
@pytest.fixture()
def login_zjtj_success(init_driver): # 调用了上面的init_driver且用了init_driver的返回值
    LoginPage(init_driver).login(CommonDatas.zjtj_name, CommonDatas.zjtj_password)
    yield init_driver

# # 还有session和module级别的
# @pytest.fixture(scope="session", autouse=True)
# def session_gl():
#     print("############测试session开始################")
#     yield True
#     print("############测试session结束################")

# 还有模块化的module
@pytest.fixture(scope="module")
def module_gl():
    print("############测试module开始################")
    yield True
    print("############测试module结束################")

# 入参 身份证号码
@pytest.fixture()
def gen_identity_number():
    pass

