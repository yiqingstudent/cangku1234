#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : login_page.py
@Author: rebecca
@Date  : 2020/4/2 15:37
@Desc  : 
"""
import logging
import time
from selenium import webdriver
from PageLocators.login_page_loc import LoginPageLoc as loc
from Common.basepage import BasePage


class LoginPage(BasePage):
    # 继承了basepage的类，就可以直接使用里面的函数了~
    # 申明是webdriver的类型，就可以直接使用self.
    # def __init__(self, driver:WebDriver):
    #     self.driver = driver
    #     self.BasePage = BasePage(self.driver)

    # 登录行为
    def login(self, username, password):
        # self.BasePage.wait_ele_visible(loc.loc_username, 'testing.png')
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.loc_username))
        # 输入用户名 J3208888880001
        self.input_element_value(loc.loc_username, username, "登录页面-用户名输入")
        self.input_element_value(loc.loc_password, password, "登录页面-密码输入")
        # 直接输入了Enter.Keys
        # self.click_success(loc.loc_login, "登录页面-点击按钮")
        # self.driver.find_element(*loc.loc_username).send_keys(username, Keys.ENTER)
        # # 输入密码，回车登录 123123
        # self.driver.find_element(*loc.loc_password).send_keys(password)
        # # 点击登录按钮
        # self.driver.find_element(*loc.loc_login).click()
        # 打印成功
        # logging.info("登录成功")
        # print("{} 登录成功！".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

    # 获取提示信息
    def get_error_message(self):
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.loc_error))
        # return self.driver.find_element(*loc.loc_error).text
        return self.get_element_text(loc.loc_error, "登录页面-错误提示信息")


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://172.31.19.96:80/pubsys/login.jsp")
    LoginPage = LoginPage(driver)
    LoginPage.login('05009', '123123')
