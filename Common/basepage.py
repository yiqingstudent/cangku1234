#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : basepage.py
@Author: rebecca
@Date  : 2020/4/14 11:00
@Desc  :
1、包含了pageobjects中用到的selenium底层方法
2、还可以包含通用的一些元素，比如alert， iframe和windows
3、还可以额外封装一些web相关的断言
4、实现日志记录、实现失败的截图

"""
import datetime
import logging
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Common.dir_config import screenshot_dir


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def save_screen_shot(self, filename):
        """
        文件命令规则，最好不要有冒号在里面，容易保存失败的
        :param filename:
        :return:
        """
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        screenshot_path = screenshot_dir + "/{}_{}.png".format(filename, now)
        try:
            self.driver.save_screenshot(screenshot_path)
        except:
            logging.exception("当前截图失败！")
            raise
        else:
            logging.info("当前图片保存在路径为{}".format(screenshot_path))

    # 基础操作1-1：等待元素可见
    # 如果需要滚动到页面最底部，元素才可见的话，可以添加一个参数，来决定是否需要拖动到最底部
    def wait_ele_visible(self, locator, filename, timeout=10, poll_frequency=0.5):
        logging.info("{}模块:等待{}元素可见.".format(filename, locator))
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
        except:
            # 1、显示将异常信息写入 2、开始截图 3、抛出异常
            logging.exception("此元素{}可能不可见，请确认下元素定位是否正确".format(locator))  # error的级别的，Traceback的信息完整的写入日志
            self.save_screen_shot(filename)
            raise
        else:
            end = datetime.datetime.now()
            duration = (end - start)
            logging.info("{}模块：等待元素可见成功！开始时间为{}，结束时间为{},耗时{}".format(filename, start, end, duration))

    # 基础操作1-2：等待元素存在页面，与之前的区别不大，主要是为了截图和失败的时候捕获异常
    def wait_ele_exist(self, locator, filename, timeout=10, poll_frequency=0.5):
        """
        :param locator:
        :param filename:
        :param timeout:
        :param poll_frequency:
        :return:True False
        """
        logging.info("{}模块:等待{}元素存在.".format(filename, locator))
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(locator))
        except:
            # 1、显示将异常信息写入 2、开始截图 3、抛出异常
            logging.exception("此元素可能不存在，请查证后再次输入！报错了，亲们！")  # error的级别的，Traceback的信息完整的写入日志
            self.save_screen_shot(filename)
            raise
        else:
            end = datetime.datetime.now()
            duration = (end - start)
            logging.info("{}模块：等待存在成功！开始时间为{}，结束时间为{},耗时{}".format(filename, start, end, duration))

    # 基础操作2：查找元素成功
    def get_element_success(self, locator, filename, timeout=10, poll_frequency=0.5):
        """
        调用selenium的原有函数find_element的方法。
        :param locator:
        :param filename:
        :param timeout:
        :param poll_frequency:
        :return:element本身。返回的是元素
        """
        logging.info("{}模块:开始查找元素{}".format(filename, locator))
        try:
            start = datetime.datetime.now()
            element = self.driver.find_element(*locator)
        except:
            # 1、显示将异常信息写入 2、开始截图 3、抛出异常
            logging.exception("查找元素失败！")
            self.save_screen_shot(filename)
            raise
        else:
            end = datetime.datetime.now()
            duration = (end - start)
            logging.info("{}模块：查找元素成功，开始时间为{}，结束时间为{},耗时{}".format(filename, start, end, duration))
            return element

    def get_elements_success(self, locator, filename, timeout=10, poll_frequency=0.5):
        """
        调用selenium的原有函数find_element的方法。
        :param locator:
        :param filename:
        :param timeout:
        :param poll_frequency:
        :return:element本身。返回的是元素
        """
        logging.info("{}模块:开始查找元素{}".format(filename, locator))
        try:
            start = datetime.datetime.now()
            elements = self.driver.find_elements(*locator)
        except:
            # 1、显示将异常信息写入 2、开始截图 3、抛出异常
            logging.exception("查找元素失败！")
            self.save_screen_shot(filename)
            raise
        else:
            end = datetime.datetime.now()
            duration = (end - start)
            logging.info("{}模块：查找元素成功，开始时间为{}，结束时间为{},耗时{}".format(filename, start, end, duration))
            return elements

    # 页面元素滚动的js执行方式
    def execute_scroll_view(self, locator, filename, timeout=10, poll_frequency=0.5):
        self.wait_ele_visible(locator, filename)
        element = self.get_element_success(locator, filename)
        logging.info("{}模块：滚动到元素可见位置begin......".format(filename, locator))
        try:
            start = datetime.datetime.now()
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            #element.click()
        except:
            logging.exception("滚动到元素可见位置失败！")
            self.save_screen_shot(filename)
            raise
        else:
            end = datetime.datetime.now()
            duration = (end - start)
            logging.info("{}模块：滚动到最底部成功，开始时间为{}，结束时间为{},耗时{}".format(filename, start, end, duration))

    # 日期输入的js执行方式
    def execute_js_date(self, locator, int_date, filename, timeout=10, poll_frequency=0.5):
        self.wait_ele_visible(locator, filename)
        element = self.get_element_success(locator, filename)
        logging.info("{}模块：滚动到元素可见位置begin......".format(filename, locator))
        try:
            start = datetime.datetime.now()
            js_effDt = """
                                var b = arguments[0]
                                b.readOnly = false;
                                b.value = arguments[1];
                                """
            self.driver.execute_script(js_effDt, element, int_date)
        except:
            logging.exception("JS方式输入日期失败！")
            self.save_screen_shot(filename)
            raise
        else:
            end = datetime.datetime.now()
            duration = (end - start)
            logging.info("#{}#模块：JS方式输入日期成功，开始时间为{}，结束时间为{},耗时{}".format(filename, start, end, duration))

    # 基础操作：实现 鼠标双击
    def double_click_success(self, locator, filename, timeout=10, poll_frequency=0.5):
        self.wait_ele_visible(locator, filename)
        element = self.get_element_success(locator, filename)
        logging.info("{}模块：对元素{}进行双击操作......".format(filename, locator))
        try:
            start = datetime.datetime.now()
            ActionChains(self.driver).double_click(element).perform()
        except:
            logging.exception("鼠标双击点击失败！")
            self.save_screen_shot(filename)
            raise
        else:
            end = datetime.datetime.now()
            duration = (end - start)
            logging.info("{}模块：鼠标双击元素成功，开始时间为{}，结束时间为{},耗时{}".format(filename, start, end, duration))

    # 基础操作：实现 鼠标悬浮点击的功能
    def move_to_click(self, locator, filename, timeout=10, poll_frequency=0.5):
        self.wait_ele_visible(locator, filename)
        element = self.get_element_success(locator, filename)
        logging.info("{}模块：对元素{}进行点击操作begin......".format(filename, locator))
        try:
            start = datetime.datetime.now()
            ActionChains(self.driver).move_to_element(element).click(element).perform()
        except:
            logging.exception("鼠标悬浮移动并点击失败！")
            self.save_screen_shot(filename)
            raise
        else:
            end = datetime.datetime.now()
            duration = (end - start)
            logging.info("{}模块：鼠标移动到元素并点击成功，开始时间为{}，结束时间为{},耗时{}".format(filename, start, end, duration))

    # 基础操作1-1 +基础操作2：click操作，点击行为，封装操作
    def click_ele_success(self, locator, filename, timeout=10, poll_frequency=0.5):
        """
        点击操作
        :param locator:
        :param filename:
        :param timeout:
        :param poll_frequency:
        :return: None
        """
        self.wait_ele_visible(locator, filename)
        element = self.get_element_success(locator, filename)
        logging.info("{}模块:对元素{}进行点击操作begin......".format(filename, locator))
        try:
            start = datetime.datetime.now()
            element.click()
        except:
            logging.exception("对元素点击操作失败！")
            self.save_screen_shot(filename)
            raise
        else:
            end = datetime.datetime.now()
            duration = (end - start)
            logging.info("{}模块-元素{}点击:开始时间为{}，结束时间为{},耗时{}".format(filename, locator, start, end, duration))

    # 基础操作1-1 +基础操作2 :input输入元素的值value
    def input_element_value(self, locator, value, filename, timeout=10, poll_frequency=0.5):
        """
        在输入框输入元素的值
        步骤为：1、等待元素可见 2、找到元素 3、输入元素的值
        :param locator:
        :param value:
        :param filename:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        self.wait_ele_visible(locator, filename)
        element = self.get_element_success(locator, filename)
        logging.info("{}#模块:{}元素的输入框值为{}".format(filename, locator, value))
        try:
            start = datetime.datetime.now()
            element.send_keys(value, Keys.ENTER)
        except:
            # 写入异常信息到日志
            logging.exception("{}元素输入值的操作报错咯~".format(locator))
            # 截图-命令规范
            self.save_screen_shot(filename)
            raise
        else:
            end = datetime.datetime.now()
            duration = (end - start)
            logging.info("{}模块：输入成功！开始时间为{}，结束时间为{},耗时{}".format(filename, start, end, duration))

    #  获取元素的文本信息
    def get_element_text(self, locator, filename, timeout=10, poll_frequency=0.5):
        """
        1、等待元素存在
        2、查找元素
        3、获取元素的文本信息
        :param locator:
        :param filename:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        self.wait_ele_exist(locator, filename, timeout, poll_frequency)
        element = self.get_element_success(locator, filename)
        logging.info("{}模块:获取{}元素的文本内容开始了......".format(filename, locator))
        try:
            start = datetime.datetime.now()
            text = element.text
        except:
            # 写入异常信息到日志
            logging.exception()
            # 截图-命令规范
            self.save_screen_shot(filename)
            raise
        else:
            end = datetime.datetime.now()
            duration = (end - start)
            logging.info("获取成功，开始时间为{}，结束时间为{},耗时{}".format(start, end, duration))
            return text

    # 获取元素的属性值
    def get_element_value(self, locator, filename, attr_name, timeout=10, poll_frequency=0.5):
        """
        1、等待元素存在
        2、查找元素
        3、获取元素的属性值
        :param locator:
        :param filename:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        self.wait_ele_exist(locator, filename)
        element = self.get_element_success(locator, filename)
        logging.info("{}模块：获取{}元素的属性{}的值开始了。。。".format(filename, locator, attr_name))
        try:
            start = datetime.datetime.now()
            value = element.get_attribute(attr_name)
        except:
            logging.exception()
            self.save_screen_shot(filename)
            raise
        else:
            end = datetime.datetime.now()
            duration = (end - start)
            logging.info("{}模块：开始时间为{}，结束时间为{},耗时{}".format(filename, start, end, duration))
            return value

    # 获取当前的url,可以直接self.driver.current_url()
    def get_current_url(self):
        # self.driver.current_url()
        pass

    # alert的处理
    def handle_alert(self, action="accept"):
        # 等待alert出现
        time.sleep(2)
        pass
        #

    # 切换window的新窗口，动作：导致新的窗口出现
    def switch_to_new_window(self, filename, timeout=10, poll_frequency=0.5):
        # 等待新窗口的出现
        time.sleep(2)
        # 获取窗口的句柄
        windows = self.driver.window_handles
        logging.info("当前窗口句柄为{}".format(windows))
        # 切换到新窗口去
        try:
            self.driver.switch_to.window(windows[-1])
        except:
            logging.exception("{}秒切换到新窗口失败！。".format(timeout))
            self.save_screen_shot(filename)
            raise
        else:
            logging.info("{}内元素可见。".format(timeout))

    # 检查页面元素是否存在
    def check_elements_exist(self, locator, filename, timeout=10, poll_frequency=0.5):
        logging.info("{}：检测元素存在且可见于页面。".format(locator, filename))
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
        except:
            logging.exception("{}秒内元素在当前页面不可见。".format(timeout))
            self.save_screen_shot(filename)
            return False
        else:
            logging.info("{}内元素可见。".format(timeout))
            return True

#  获取多个元素的信息
    def get_elements_texts(self, locator, filename, timeout=10, poll_frequency=0.5):
        """
        1、等待元素存在
        2、查找元素
        3、获取元素的文本信息
        :param locator:
        :param filename:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        self.wait_ele_exist(locator, filename, timeout, poll_frequency)
        elements = self.get_elements_success(locator, filename)
        logging.info("{}模块:获取{}元素的all_texts开始了......".format(filename, locator))
        try:
            lists = []
            for element in elements:
                lists.append(element.text)
        except:
            logging.exception("{}获取所有元素的文本值报错！。".format(timeout))
            self.save_screen_shot(filename)
            raise
        else:
            logging.info("{}模块：完成获取元素所有的文本值".format(filename))
            return lists

    def clear_ele_success(self, locator, filename, timeout=10, poll_frequency=0.5):
        """
        清空操作
        :param locator:
        :param filename:
        :param timeout:
        :param poll_frequency:
        :return: None
        """
        self.wait_ele_visible(locator, filename)
        element = self.get_element_success(locator, filename)
        logging.info("{}模块:对元素{}进行点击操作开始......".format(filename, locator))
        try:
            start = datetime.datetime.now()
            element.clear()
        except:
            logging.exception("对元素清空操作失败！")
            self.save_screen_shot(filename)
            raise
        else:
            end = datetime.datetime.now()
            duration = (end - start)
            logging.info("{}模块#元素{}清空操作:开始时间为{}，结束时间为{},耗时{}".format(filename, locator, start, end, duration))





