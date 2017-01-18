# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import unittest
import sys,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import requests,json,time
from Interface.dp import OrderDp
from test_data.dp_data import OrderDP_data
import setting.api_signs
import setting.result_jsons
import setting.DBConns
from setting.test_result import test_result


times= int(time.time())


class Test(OrderDp.MyTest):
    @classmethod

    def setUpClass(cls):
#        DP_data.init_data()#暂时想不出入库有什么意义，代码先保留吧

        pass

    def test_post_orderDP_sucess(self):
        '''成功创建点评订单'''
        api_key=setting.DBConns.Api_secret(**OrderDP_data.data_OrderDPSuces)#返回api_key
        if api_key == None:
            print(u"api_key 不存在，请检查接口数据！")
        else:
            api_secrets=setting.DBConns.secret(api_key)#返回api_secret
            if api_secrets !=0:
                payload=OrderDP_data.data_OrderDPSuces
                api_sign=setting.api_signs.api_signs(payload,api_secrets)
                payload.setdefault('api_sign',api_sign)
                r=requests.post(self.base_url, params=payload)
             #   print(json.dumps(payload,ensure_ascii=False,sort_keys=True,indent=10))
                self.code=r.status_code
                try:
                    js = json.loads(r.text)
                    print(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10)) #转换为中文
                except:
                     print (r.text)
            else:
                print (u"该 api_secret 不存在，请检查数据库是否连接正确！")


    def test_post_orderDP_api_keyNull(self):
        '''api_key为空'''
        r=requests.post(self.base_url, params=OrderDP_data.data_orderDP_api_keyNull)
        self.code=r.status_code
        s = r.json()
        json_string=json.dumps(s,sort_keys=True, indent=2)#后面的参数控制输出的json格式
        data=json.loads(json_string)#joson转换为dic
        test_result.test_result(data)
        self.text=test_result.test_result(data)
        js = json.loads(r.text)
        print(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10))
        #print(json_string)
 #       self.assertEquals(self.code,200)
#        self.assertEquals(self.text,99000003)

    def test_post_orderDP_api_uidNull(self):
        '''Uid为空'''
        r=requests.post(self.base_url, params=OrderDP_data.data_orderDP_uidNull)
        self.code=r.status_code
        s = r.json()
        print r.text
        json_string=json.dumps(s,sort_keys=True, indent=2)#后面的参数控制输出的json格式
        data=json.loads(json_string)#joson转换为dic
        test_result.test_result(data)
        self.text=test_result.test_result(data)
        print type(json_string)
        print(json_string.encode(encoding='gbk'))
        print(unicode(json_string,'gbk'))
        self.assertEquals(self.code,200)
        self.assertEquals(self.text,10010001)


    def test_post_orderDP_api_ConNull(self):
        '''用户名为空'''
        r=requests.post(self.base_url, params=OrderDP_data.data_orderDP_ConNull)
        self.code=r.status_code
        s = r.json()
        json_string=json.dumps(s,sort_keys=True, indent=2)#后面的参数控制输出的json格式
        data=json.loads(json_string)#joson转换为dic
        test_result.test_result(data)
        self.text=test_result.test_result(data)
        print(json_string)
        self.assertEquals(self.code,200)
        self.assertEquals(self.text,10010001)

    def test_post_orderDP_api_ProdNull(self):
        '''商品信息为空'''
        r=requests.post(self.base_url, params=OrderDP_data.data_orderDP_ProdNull)
        self.code=r.status_code
        s = r.json()
        json_string=json.dumps(s,sort_keys=True, indent=2)#后面的参数控制输出的json格式
        data=json.loads(json_string)#joson转换为dic
        test_result.test_result(data)
        self.text=test_result.test_result(data)
        print(json_string)
        self.assertEquals(self.code,200)
        self.assertEquals(self.text,10040004)

    def test_post_orderDP_Shop_idNull(self):
        '''商品id为空'''
        r=requests.post(self.base_url, params=OrderDP_data.data_orderDP_Shop_idNull)
        self.code=r.status_code
        s = r.json()
        json_string=json.dumps(s,sort_keys=True, indent=2)#后面的参数控制输出的json格式
        data=json.loads(json_string)#joson转换为dic
        test_result.test_result(data)
        self.text=test_result.test_result(data)
        print(json_string)
        self.assertEquals(self.code,200)
#        self.assertEquals(self.text,0)

    def test_post_orderDP_TimesNull(self):
        '''请求时间戳为空'''
        r=requests.post(self.base_url, params=OrderDP_data.data_orderDP_TimesNull)
        self.code=r.status_code
        s = r.json()
        json_string=json.dumps(s,sort_keys=True, indent=2)#后面的参数控制输出的json格式
        data=json.loads(json_string)#joson转换为dic
        test_result.test_result(data)
        self.text=test_result.test_result(data)
        print(json_string)
        self.assertEquals(self.code,200)
        self.assertEquals(self.text,0)


if __name__=='__main__':
    unittest.main()



