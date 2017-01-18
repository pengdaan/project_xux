# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import sys
import time
times= int(time.time())
sys.path.append('../db_fixture')
from setting.mysql_setting import MySQLOperating

def inster_data(table,datas):
    db=MySQLOperating()
    db.clear(table)#删除上一次执行的test数据，保留本次的test数据
    for data in datas:
        db.insert(table,data)
    db.close()


table_poll_OrderDP="orderdp"




#成功创建订单
data_OrderDPSuces={
        'uid':'43507844',
        'timestamp':times,
        'consignee':'么么22',
        'shop_id':'38021',
        'pay_expire':'7200',
        'mobile':'13728142737',
        'source':'wap',
        'shop_city':'289',
        'products':[{"product_id":"10853",
                     "goods_id":"847",
                     "product_sn":"product2016101010853",
                     "goods_name":"成本商品001（xsx勿动）",
                     "shop_price":"20.00",
                     "goods_thumb":"http://cdn-dianping.mama.cn/upload/201610/20161010/6452620821fdfe3efdbd15a0ade355e8.jpg",
                     "supplier_id":"120",
                     "without_return":"1",
                     "goods_number":"1",
                     "use_coupon":"1",
                     "end_return_time":"0",
                     "return_anytime": "0",
                     "goods_attr_id":"3031",
                     "goods_attr": "默认属性:均码"
                    }],
         'version':'2.0',
         'api_key':'8d46b75a4a0456a35302d2893ed072a3'
}

data_OrderDPSucess=[data_OrderDPSuces]

#api_key为空
data_orderDP_api_keyNull={
        'api_key':'8d46b75a4a0456a35302d2893ed072a3',
        'uid':'43507844',
        'consignee':'么么22',
        'mobile':'13728142737',
        'shop_id':'123456',
        'products':'[{"product_id":10749,"number":1}]',
        'timestamp':times,
    }
data_orderDP_api_keyNulls=[data_orderDP_api_keyNull]

#Uid为空
data_orderDP_uidNull={
        'api_key':'8d46b75a4a0456a35302d2893ed072a3',
        'uid':'',
        'consignee':'么么22',
        'mobile':'13728142737',
        'shop_id':'123456',
        'products':'[{"product_id":10749,"number":1}]',
        'timestamp':times,
    }
data_orderDP_uidNulls=[data_orderDP_uidNull]

#用户名为空
data_orderDP_ConNull={
        'api_key':'8d46b75a4a0456a35302d2893ed072a3',
        'uid':'43507844',
        'consignee':'',
        'mobile':'13728142737',
        'shop_id':'123456',
        'products':'[{"product_id":10749,"number":1}]',
        'timestamp':times,
    }
data_orderDP_ConNulls=[data_orderDP_ConNull]

#shop_id为空
data_orderDP_Shop_idNull={
        'api_key':'8d46b75a4a0456a35302d2893ed072a3',
        'uid':'43507844',
        'consignee':'么么22',
        'mobile':'13728142737',
        'shop_id':'123456',
        'products':'[{"product_id":10749,"number":1}]',
        'timestamp':times,
    }
data_orderDP_Shop_idNulls=[data_orderDP_Shop_idNull]

#商品信息为空
data_orderDP_ProdNull={
        'api_key':'8d46b75a4a0456a35302d2893ed072a3',
        'uid':'43507844',
        'consignee':'么么22',
        'mobile':'13728142737',
        'shop_id':'123456',
        'products':'',
        'timestamp':times,
    }
data_orderDP_ProdNulls=[data_orderDP_ProdNull]


#请求时间戳为空
data_orderDP_TimesNull={
        'api_key':'8d46b75a4a0456a35302d2893ed072a3',
        'uid':'43507844',
        'consignee':'么么22',
        'mobile':'13728142737',
        'shop_id':'123456',
        'products':'[{"product_id":10749,"number":1}]',
        'timestamp':'',
    }
data_orderDP_TimesNulls=[data_orderDP_TimesNull]


def init_data():
    inster_data(table_poll_OrderDP,data_OrderDPSucess)
    inster_data(table_poll_OrderDP,data_orderDP_api_keyNulls)
    inster_data(table_poll_OrderDP,data_orderDP_ConNulls)
    inster_data(table_poll_OrderDP,data_orderDP_Shop_idNulls)
    inster_data(table_poll_OrderDP,data_orderDP_ProdNulls)
    inster_data(table_poll_OrderDP,data_orderDP_TimesNulls)



if __name__=='__main__':
    init_data()

