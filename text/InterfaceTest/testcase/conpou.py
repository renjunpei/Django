#coding:utf-8
import requests
import unittest
import json
from InterfaceTest.common.config import Conf
from InterfaceTest.common.mylogin import mylogin

class conpou(unittest.TestCase):

    def setUp(self):
        self.cookie = mylogin()

    def test_conpou(self):
        data ={
           'page':1,
           'status':0,
           'imei':'3B8D4B09-D864-402F-91D8-33C20B26681A',
           'weexVersion':127,
           'mobileModel':'iPhone5s (GSM+CDMA)'



        }
        a=requests.get(url=Conf.API_ADDRESS+'/sdapp/coupon/getMyConpou',data=data,cookies=self.cookie)
        response = json.loads(a.content)
        print(a)
        # print(type(a))

        def tearDown(self):
            pass

if __name__ == '__main__':
    unittest.main()


