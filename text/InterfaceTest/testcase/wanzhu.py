#-*- coding:utf-8 -*-
import unittest
import requests
import json
from InterfaceTest.common.config import Conf
from InterfaceTest.common.mylogin import mylogin

class Wanzhu(unittest.TestCase):

    def setUp(self):
        self.cookie = mylogin()
    # 玩主主页
    def test_a_zhuye(self):

        data = {
            'mobileModel': 'HUAWEI NXT - AL10',
            'versionAndr': 104,
            'version': 104,
            'clientType': 2,
        }
        response = requests.get(url=Conf.API_ADDRESS+"/sdapp/user/detail/findUserLeaderDetailById",data=data,cookies=self.cookie)
        result = json.loads(response.content)
        print(result)

    # 玩主资产
    def test_b_zichan(self):
        data = {
            'mobileModel': 'HUAWEI NXT - AL10',
            'versionAndr': 104,
            'version': 104,
            'clientType': 2,
        }
        response = requests.get(url=Conf.API_ADDRESS+"/sdapp/user/detail/findUserLeaderDetailMoney",data=data,cookies=self.cookie)
        result = json.loads(response.content)
        print(result)

    # 我的地盘
    def test_c_dipan(self):
        data = {
            'mobileModel': 'HUAWEI NXT - AL10',
            'versionAndr': 104,
            'version': 104,
            'clientType': 2,
            'ifBillVip':2,
            'page':5,

        }
        response = requests.post(url=Conf.API_ADDRESS+"/sdapp/user/relation/getUserEaringPreList",data=data,cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
















if __name__ == '__main__':
    unittest.main()







