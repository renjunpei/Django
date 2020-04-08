import unittest
import requests
import json
from InterfaceTest.common.mylogin import mylogin
from InterfaceTest.common.config import Conf

def readexcel_data():

    list = []
    a = 0
    # f = open('a.txt', 'r')
    for line in open('a.txt'):
        # line = f.readline()
        userInfo = mylogin(line.strip())
        # print(userInfo)
        i = 0
        while True:
            id = 259740230000016
            data1 = {'id':id}
            response1 = requests.post(url="http://123.157.216.154:8000/sdapp/goods/hot/saveLoveNum",data=data1,cookies=userInfo)
            code = response1.status_code
            if code == 200:
                i += 1
                result1 = json.loads(response1.content)
                # print(result1)
                if result1["result"]["hasPrize"] == True:
                    print(i)
                    # list.append(i)
                    break
    for a1 in list:
        a += a1
    print(str((a / len(list))*100) + '%')


        # i = 0
        # while True:
        #     data1 = {
        #     'connectType':'wx',
        #     'headUrl':'https://wx.qlogo.cn/mmopen/vi_32/PHj4OGk8ZfFVgJHrzdl00g2s0vMlPBZXeTHkm70AKagezQy1GGRTGw4WhVnMIAL7wXicicIw7OpcqX8HU2oOAoOw/132',
        #     'loginType':'sms',
        #     'nickName':'Better',
        #     'randomCode'
        #     'unionId':'oQ-Li5KyAFLsIQT33f5C-NPVcDqk'
        # }
        # result = requests. post(url="http://supply.mihui365.com/o2oShop/wxLogin/login",data=data1)
        # cookies = result.cookies
        # print(cookies)
        #
        # response = requests.get(url="http://supply.mihui365.com/o2oShop/wxTrade/create?addrId=11951&idCradId=2424&tradeCreateVo=%5B%7B%22skuId%22%3A16559%2C%22count%22%3A1%7D%5D&remark= HTTP/1.1",cookies=cookies)

if __name__ == '__main__':
        readexcel_data()