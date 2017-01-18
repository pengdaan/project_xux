# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import unittest
import sys,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import requests,json,time
import setting.PayDBConns
from test_data.pay import  Payrefund_data
import setting.api_signs
import setting.result_jsons
import setting.DBConns
from Interface.pay import pay_refund
times= int(time.time())
class Test(pay_refund.MyTest):


    def test_post_Payrefund_sucess(self):
        '''退款接口：成功退款'''
        own_mch_id=setting.PayDBConns.Payapi_secret(**Payrefund_data.data_PayRefundSuces)#返回api_key
        if own_mch_id == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.PayDBConns.paysecret(own_mch_id)#返回api_secret
            if api_secrets !=0:
                payload=Payrefund_data.data_PayRefundSuces
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
               # print payload
                r=requests.post(self.Payrefund_url, params=payload)
                self.code=r.status_code
                self.result=r.text
                js=setting.result_jsons.result_json(self.result)
                if js.has_key('msg')==True:
                        self.msgs=js.get('msg')
                        self.assertEquals(self.code,200)
                        self.assertEqual(self.msgs, '退款单退款成功')

                else:
                        print 'NO msg'
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")
