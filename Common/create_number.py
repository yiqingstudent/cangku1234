#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : create_number.py
@Author: rebecca
@Date  : 2020/4/28 10:19
@Desc  : 
"""
import random,time
import datetime as dt

from Common.dir_config import DC_PATH


class CreateNumber:
    # 统一社会信用代码最后一位：代码字符集
    check_dict = {
        "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
        "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "J": 18, "K": 19, "L": 20, "M": 21,
        "N": 22, "P": 23, "Q": 24, "R": 25, "T": 26, "U": 27, "W": 28, "X": 29, "Y": 30
    }
    dict_check = {value: key for key, value in check_dict.items()}

    # 组织机构代码 9位
    def create_organization(self):
        ww = [3, 7, 9, 10, 5, 8, 4, 2]  # suan fa yin zi
        cc = []
        dd = 0

        for i in range(8):  # gei CC fu zhi
            cc.append(random.randint(1, 9))
            dd = dd + cc[i] * ww[i]
        for i in range(len(cc)):
            cc[i] = str(cc[i])
        C9 = 11 - dd % 11
        if C9 == 10:
            C9 = 'X'
        else:
            if C9 == 11:
                C9 = '0'
            else:
                C9 = str(C9)
        cc.append('-' + C9)
        return "".join(cc)

    def create_organization_bak(self):
        weight_code = [3, 7, 9, 10, 5, 8, 4, 2]  # Wi 代表第i位上的加权因子=pow(3,i-1)%31
        org_code = []
        sum = 0
        for i in range(8):
            org_code.append(self.dict_check[random.randint(0, 30)])  # 前八位本体代码：0~9 + A~Z 31个
            sum = sum + self.check_dict[org_code[i]] * weight_code[i]
        C9 = 11 - sum % 11
        if C9 == 10:
            last_code = 'X'
        elif C9 == 11:
            last_code = '0'
        else:
            last_code = str(C9)
        code = ''.join(org_code) + '-' + last_code  # 组织机构代码
        return code

    def create_social_credit(self):
        """
        # 生成 统一社会信用代码 18位
        :return:social_code
        """
        manage_code = [9]  # 登记管理部门代码：9-工商
        type_code = [1, 2, 3, 9]  # 9-1-企业，9-2-个体工商户，9-3-农民专业合作社，9-9-其他
        area_code = '100000'  # 登记管理机关行政区划码：100000-国家用
        org_code = self.create_organization().replace('-', '')  # 组织机构代码
        sum = 0
        # # Wi 代表第i位上的加权因子=pow(3,i-1)%31
        weight_code = [1, 3, 9, 27, 19, 26, 16, 17, 20, 29, 25, 13, 8, 24, 10, 30, 28]
        code = str(random.choice(manage_code)) + str(random.choice(type_code)) + area_code + org_code
        for i in range(17):
            sum = sum + self.check_dict[code[i:i + 1]] * weight_code[i]
        C18 = self.dict_check[31 - sum % 31]
        social_code = code + C18
        return social_code

    def create_enterprise_name(self):
        name = "企业名称为"+dt.datetime.now().strftime('%F %T')
        return name

    def create_customer_name(self):
        name = "A个人客户名称"+dt.datetime.now().strftime('%F %T')
        return name

    # 随机生成手机号码
    def create_phone(self):
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                   "147",
                   "150", "151", "152","153","155", "156", "157", "158", "159",
                   "186",
                   "187",
                   "188",
                   "189"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

    # 随机生成身份证号
    def get_district_code(self):
        district_codes = []
        with open(DC_PATH, mode='r', encoding='utf-8') as f:
            for l in f.readlines():
                district_codes.append(l.strip()[:6])
        return district_codes

    def generate_id(self, gender=None):
        """
            :param gender: 控制性别，None为随机, 1:男，0：女
            :return: 身份证号码
        """
        # 6位地址码
        codelist = self.get_district_code()
        id_location = codelist[random.randint(0, len(codelist) - 1)]  # randint为闭区间，注意-1
        # 8位生日编码
        date_start = time.mktime((1971, 1, 1, 0, 0, 0, 0, 0, 0))
        date_end = time.mktime((2019, 8, 1, 0, 0, 0, 0, 0, 0))
        date_int = random.randint(date_start, date_end)
        id_date = time.strftime("%Y%m%d", time.localtime(date_int))
        # 3位顺序码，末尾奇数-男，偶数-女
        id_order = 0
        if not gender:
            id_order = random.randint(0, 999)
        elif gender == 1:
            id_order = random.randint(0, 499) * 2 + 1
        elif gender == 0:
            id_order = random.randint(0, 499) * 2

        if id_order >= 100:
            id_order = str(id_order)
        elif id_order >= 10:
            id_order = "0" + str(id_order)
        else:
            id_order = "00" + str(id_order)
        # 前17位相加
        ID_former = id_location + id_date + id_order
        # 验证码
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
        check_code = {
            '0': '1',
            '1': '0',
            '2': 'X',
            '3': '9',
            '4': '8',
            '5': '7',
            '6': '6',
            '7': '5',
            '8': '5',
            '9': '3',
            '10': '2'}  # 校验码映射
        sum = 0
        for i, num in enumerate(ID_former):
            sum += int(num) * weight[i]
        ID_check = check_code[str(sum % 11)]
        ID = ID_former + ID_check
        return ID


if __name__ == '__main__':
    cm = CreateNumber()
    number = cm.create_social_credit()
    print(number)
    print(cm.create_organization())
    print(cm.create_enterprise_name())
    print(cm.generate_id(gender=1))
    print(cm.create_phone())

