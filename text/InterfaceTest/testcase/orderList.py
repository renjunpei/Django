import unittest
import requests
import json
from InterfaceTest.common.mylogin import mylogin
from InterfaceTest.common.config import Conf

class OrderList(unittest.TestCase):
    def setUp(self):
        self.cookie = mylogin()
        return self.cookie

    def test_tradelist(self):
        #status = 1待付款 status = 5 待发货 status = 6 待收货 status = 7 已完成
        data = {
            'systemVersion': '7.0',
            'clientType': 3,
            'imei': 860076030766777,
            'mobileModel': 'HUAWEI NXT - AL10',
            'versionAndr': 107,
            'version': 107,
            'weexVersion': 201,
            'page': 1,
            'status':0,
            'type':2
        }
        response = requests.post(url=Conf.API_ADDRESS+'/sdapp/trade/queryTradeListByPage',data=data,cookies = self.cookie)
        result = json.loads(response.content)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
