#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : public_func.py
@Author: rebecca
@Date  : 2020/4/8 9:43
@Desc  : 
"""
import requests
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PublicFunc:
    def __init__(self, driver):
        self.driver = driver

    def retry_click(self, by):
        result = False
        attempts = 0
        while attempts < 2:
            try:
                WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by))
                self.driver.find_element(*by).click()
                result = True
                break
            except StaleElementReferenceException:
                pass
            attempts += 1
        return result


    def get_Ajax(self, base_url):
        """
        Get the data transmitted asynchronously by the backend,
        the return value is a list containing all the data information
        base_url:the request url,change it you could get any other ajax part you need
        """
        try:
            cookielist = self.driver.get_cookies()
            for cookiedict in cookielist:
                if cookiedict['name'] == 'CiSession':
                    cookievalue = cookiedict['value']
                else:
                    pass
            cookie = "testcookie=yes;CiSession=" + cookievalue
            header = {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
                'Cookie': cookie,
            }

            response = requests.get(base_url, headers=header)
            Ajax_list = response.json()
            return Ajax_list

        except requests.ConnectionError as e:
            print("--ERROR--:", e.args)
