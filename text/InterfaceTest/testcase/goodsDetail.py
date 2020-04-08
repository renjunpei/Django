import unittest
import requests
import json
from InterfaceTest.common.config import Conf
from InterfaceTest.common.mylogin import mylogin
import time

class GoodsDetail(unittest.TestCase):
    def setUp(self):
        self.cookie = mylogin()

    # 商品详情页
    def test_a_goodsDetail(self):
        data={
            'clientType':2,
            'goodsId':256595020035811,
            'imei':'0B3B30A7-41B8-43D6-8979-A49F56020843',
            'mobileModel':'iPhone_X',
            'systemVersion':'12.1',
            'version':105,
            'versionIos':105
        }
        response = requests.post(url=Conf.API_ADDRESS+'/sdapp/goods/queryDetail',data=data,cookies=self.cookie)
        # response = json.loads(response.content)
        # print(response)
        # self.assertEqual(True, False)
        code = response.status_code
        if code == 200:
            result = json.loads(response.content)
            # return result["result"]["goodsSkus"][0]["skuId"]
            # return result["result"]["goodsDetail"]["goodsId"]
            goodsId = result["result"]["goodsDetail"]["goodsId"]
            skuId = result["result"]["goodsSkus"][0]["skuId"]
            # list = []
            #
            # list.append(skuId)
            # list.append(goodsId)
            # # return skuIds[0]
            # return list
            dict = {"skuId":skuId,"goodsId":goodsId}
            # print(str(dict))
            return dict


    #  商品说明
    def test_b_goodsexplain(self):
        a = self.test_a_goodsDetail()
        # print(a)
        # user_dict = eval(a)

        # print(type(user_dict))
        id = a['goodsId']
        # print(id)
        data = {
            'clientType': 2,
            'imei':'D439B4B3-DB5D-4505-B38E-4AB6351B158E',
            'mobileModel': 'iPhone_X',
            'goodsId':id,
            'version': 105,
            'versionIos': 105,
            'systemVersion': '12.1',
            'weexVersion':127
        }
        # print(data)
        response = requests.post(url=Conf.API_ADDRESS+'/sdapp/goods/getGoodsInstructions',data=data,cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)

    # 商品优惠券（需要查看该商品有没有优惠券）
    def test_c_goodscoupon(self):
        a = self.test_a_goodsDetail()
        id = a['goodsId']
        data = {
            'clientType': 2,
            'imei': 'D439B4B3-DB5D-4505-B38E-4AB6351B158E',
            'mobileModel': 'iPhone_X',
            'goodsId': id,
            'version': 105,
            'versionIos': 105,
            'systemVersion': '12.1',
            'weexVersion': 127
        }
        response = requests.post(url=Conf.API_ADDRESS+'/sdapp/coupon/findByGoodsId',data=data,cookies=self.cookie)
        # result = json.loads(response.content)
        # print(result)
        # time.sleep(1)
        code = response.status_code
        if code == 200:
            result = json.loads(response.content)
            # id = result["result"][0]["id"]
            # print(id)
            return result["result"][0]["id"]

    # 领取优惠券
    def test_d_receivecoupon(self):
        id1 = self.test_c_goodscoupon()
        # print(id)
        data = {
            'clientType': 2,
            'imei': 'D439B4B3-DB5D-4505-B38E-4AB6351B158E',
            'mobileModel': 'iPhone_X',
            'couponId': id1,
            'version': 105,
            'versionIos': 105,
            'systemVersion': '12.1',
            'weexVersion': 127
        }
        response = requests.post(url=Conf.API_ADDRESS+"/sdapp/coupon/addUserCoupon",data=data,cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)


    # 商品收藏
    def test_e_shoucang(self):
        a = self.test_a_goodsDetail()
        id = a['goodsId']
        # print(id)
        data = {
            'clientType': 2,

            'imei': '0B3B30A7-41B8-43D6-8979-A49F56020843',
            'mobileModel': 'iPhone_X',
            'systemVersion': '12.1',
            'version': 105,
            'versionIos': 105,
            'goodsId': id
        }
        response = requests.post(url=Conf.API_ADDRESS + '/sdapp/goods/collect/insertCollect', data=data,
                                 cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)
    # 商品精选
    def test_f_jingxuan(self):
        a = self.test_a_goodsDetail()
        id = a['goodsId']
        # print(id)
        data = {
            'clientType': 2,
            'imei': '0B3B30A7-41B8-43D6-8979-A49F56020843',
            'mobileModel': 'iPhone_X',
            'systemVersion': '12.1',
            'version': 105,
            'versionIos': 105,
            'goodsId': id
        }
        response = requests.post(url=Conf.API_ADDRESS + '/sdapp/goods/user/shop/insertGoodsUserShop', data=data,
                                 cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)
    # 商品分享
    def test_g_fexniang(self):
        a = self.test_a_goodsDetail()
        id = a['goodsId']
        # print(id)
        data = {
            'clientType': 2,
            'type': 4,
            'imei': '0B3B30A7-41B8-43D6-8979-A49F56020843',
            'mobileModel': 'iPhone_X',
            'systemVersion': '12.1',
            'version': 105,
            'versionIos': 105,
            'dataId': id
        }
        response = requests.post(url=Conf.API_ADDRESS + '/sdapp/core/share/detail', data=data, cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)

    # 分享增加活跃值
    def test_h_addActive(self):
        a = self.test_a_goodsDetail()
        id = a['goodsId']
        # print(id)
        data = {
            'clientType': 2,
            'dataId': id,
            'imei': '0B3B30A7-41B8-43D6-8979-A49F56020843',
            'mobileModel': 'iPhone_X',
            'systemVersion': '12.1',
            'version': 105,
            'versionIos': 105,
            'type': 4
        }
        response = requests.post(url=Conf.API_ADDRESS+"/sdapp/core/share/addActive",data=data,cookies=self.cookie)
        result = json.loads(response.content)
        print(result)
        time.sleep(1)

    # 加入购物车列表
    def test_i_addshopcar(self):
        a = self.test_a_goodsDetail()
        skuId = a['skuId']
        tradeSkuVO = [{"num":1,"skuId":"{}".format(skuId)}]
        data = {
            'clientType': 2,
            'mobileModel': 'iPhone_X',
            'systemVersion': '12.1',
            'version': 105,
            'versionIos': 105,
            'tradeSkuVO':'{}'.format(tradeSkuVO)
            # 'skuId':'{}'.format(skuId),
            # 'num':1
        }
        print(data)
        result = requests.post(url=Conf.API_ADDRESS + "/sdapp/shop/car/addShopCar",data=data,cookies=self.cookie)
        response = json.loads(result.content)
        print(response)
        time.sleep(1)


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
