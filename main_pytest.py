#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : main_pytest.py
@Author: rebecca
@Date  : 2020/6/7 22:40
@Desc  : 
"""
import pytest
# 入口函数
# 不加参数，是表示搜索当前目录下所有的测试用例
# 重运行2次，
pytest.main(["-m", "zhanqi",
             "-s", "-v",
             "--reruns", "2", "--reruns-delay", "5",
             "--html=Outputs/reports/pytest.html",
             "--alluredir=Outputs/allure"])


