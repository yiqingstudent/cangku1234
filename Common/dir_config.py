#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: rebecca
# Time: 2019/11/28 17:04
import os

# 框架项目顶层目录
print("系统ospath：", os.path)

# os.path.abspath(path) ：返回绝对路径：G:\2020_AUTO\2020xindai_pytest_web\Common\dir_config.py
# os.path.abspath(__file__) 作用： 获取当前脚本的完整路径
ab_path = os.path.abspath(__file__)
print("绝对路径为：", os.path.abspath(__file__))

# 返回文件路径:G:\2020_AUTO\2020xindai_pytest_web\Common
common_path = os.path.dirname(ab_path)
print("本层文件路径为：", os.path.dirname(ab_path))

# 返回上一层级
print("上级文件目录为：", os.path.dirname(common_path))

# os.path.split()：按照路径将文件名和路径分割开,返回值为元组，('G:\\2020_AUTO\\2020xindai_pytest_web\\Common', 'dir_config.py')
sp_path = os.path.split(ab_path)
print(sp_path)
# 返回上一层目录，到文件夹这个层级：G:\2020_AUTO\2020xindai_pytest_web\Common
print(sp_path[0])

# 再次返回上一层的根目录
root_path = os.path.split(sp_path[0])[0]
print("根目录为：", root_path)

# 根目录与其他文件夹，分层的进行拼接
test_case_path = os.path.join(root_path, "TestCases")
print("测试案例的路径为：", test_case_path)

base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# print(base_dir)

testdatas_dir = os.path.join(base_dir, "TestDatas")

testcases_dir = os.path.join(base_dir, "TestCases")

htmlreport_dir = os.path.join(base_dir, "Outputs/reports")
# print(htmlreport_dir)

logs_dir = os.path.join(base_dir, "Outputs/logs")

# config_dir =  os.path.join(base_dir,"Config")

screenshot_dir = os.path.join(base_dir, "Outputs/screenshots")
# print(screenshot_dir)
DC_PATH = os.path.join(base_dir, "SourceDatas/districtcode.txt")
# print(DC_PATH)

