#-*- coding:utf-8 -*-
import json
import unittest

import requests

from InterfaceTest.common.config import Conf
from InterfaceTest.common.xlrd_train import readexcel_data
from InterfaceTest.common.mylogin import mylogin


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.cookies = mylogin()
        # return self.cookies
        # print(self.cookies)



    def test_login(self):
        # data = {
        #     'mobile': '15825519561',
        #     'password': '7FEB6545144CD4734BB9C3B0E2C4F53C00FDFCF342FD8E8B3DEAEC2523890FCE6395E879AC0F94EBFA134B7DB65FC2DCBBE0F589A00151533FE884A50B96031B5D16A9174F82D41AB500D913783B936CDA6D1D87B22450473F4BB04759BC20BE4E911C84EE60B77AA6784626C265B49E524AC8957CA58A14654C09FD8C06646C'
        # }
        # print(type(data['mobile']))
        data = readexcel_data()
        for data1 in data:
            result = requests.post(url=Conf.API_ADDRESS + "/user/login.shtml", data=data1)
            response = json.loads(result.content)
        # print(response)
            # self.assertEqual(response['success'],True)
            if response['success'] == True:
                print("----------通过----------")
            else:
                print("----------失败----------")


    def test_myTradeCount(self):
        # cookies = mylogin()
        response=requests.post(url=Conf.API_ADDRESS+"/ord/myTradeCount.shtml",cookies=self.cookies)
        result = json.loads(response.content)
        print(result)
        # return result

    # 登录




    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()
