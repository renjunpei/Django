#coding:utf-8
import unittest
import requests
import json
from InterfaceTest.common.config import Conf
from InterfaceTest.common.mylogin import mylogin

class getConpouByCode(unittest.TestCase):

    def setUp(self):
        self.cookie = mylogin()

    def test_getConpouByCode(self):
        data ={

            "tattedCode":111111,

        }

        a = requests.post(url=Conf.API_ADDRESS + '/sdapp/coupon/getConpouByCode',data=data)

        response = json.loads(a.content)
        print(a)

        # print(type(a))

        def tearDown(self):
            pass

    if __name__ == '__main__':
        unittest.main()
