# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import time
import datetime
times= int(time.time())
dtime=datetime.datetime.now()
def addTime():
    dtime=datetime.datetime.now()
    dtime2= dtime + datetime.timedelta(hours=1)
    timestamp=int(time.mktime(dtime2.timetuple()))
    return timestamp
dtimes=addTime()

add_time= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))# 获取当前时间。
promotionNames=str(add_time) + 'Test_AddPms'

Title=str(add_time)+'Test_AddPms'


#点评相关接口


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
        'version':'2.0',
        'api_key':'8d46b75a4a0456a35302d2893ed072a3',
        'products':'[{"product_id":"10852",'
                   '"goods_id":"846",'
                   '"product_sn":"product2016101010852",'
                   '"goods_name":"扣点商品001（xsx勿动）",'
                   '"shop_price":"10.00",'
                   '"goods_thumb":"//cdn-dianping.mama.cn/upload/201610/20161010/b02077e9907e75c58d15b8c6245bb175.jpg",'
                   '"supplier_id":"121",'
                   '"without_return":"0",'
                   '"goods_number":"1",'
                   '"use_coupon":"3",'
                   '"end_return_time":"0",'
                   '"return_anytime":"1",'
                   '"goods_attr_id":"3030",'
                   '"goods_attr":"默认属性:均码"}]'
}


#点评验卷接口
data_DPverif={
    'api_key':'b47d4503ce201db6df525911812dd089',
    'timestamp':times,
    'data':'{"supplierId":1,"couponIds":[2447]}'
}



data_UserOrderListDP={
     'api_key':'8d46b75a4a0456a35302d2893ed072a3',
     'uid':'43507844',
     'order_cate_id':'[2001,2006]'



}



#旅游相关接口


'''test:获取用户所有的订单列表'''
test_UserOrderListTour={
        'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
        'uid':'43507844',
        'page_num':'1',
        'page_size':'20',
        'status':'100',
        'order_cate_id':'[2001,2002,2003,2004]'

    }

'''test:根据订单分类获取分类订单总数'''

test_UserOrderNums={
        'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
        'uid':43507844,
        'order_cate_id':'[2001,2002,2003,2004,2006]'

    }


'''旅游通过出行日期查询已支付的订单'''

test_OrderByGoTime={
     'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
     'time':time,
     'go_time':'2016-10-26',
     'extra_fields':'["refund","delivery"]'


}

'''旅游通过出行日期查询已支付的订单'''

test_OrderBySnTour={
    'api_key':'9R3coFDrgBiEZUQG2PZmqTXMjiT2wU6o',
    'timestamp':time,
    'order_sn':'LY67414946235558'

}

#PMS相关接口



'''增加优惠劵 '''

test_Addpms={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,
    'data':'{'
           '"promotionName":"' + str(promotionNames) + '",'
           '"sendNumLimit":2,'
           '"sendNum":0,"startDateLimit":2,'
           '"dateExpireNum":1,'
           '"getNumLimit":0,'
           '"adminId":1,"suppliersId":0,'
           '"promotionTitle":"' + str(Title) + '",'
           '"promotionDetail":"",'
           '"receiveLimit":1,'
           '"type":0,'
           '"rangeType":0,'
           '"chargePer":0.9,'
           '"supplierChargePer":0.1,'
           '"promotionRange":[],'
           '"supportMsGoods":1,'
           '"linkUrl":"",'
           '"selfType":"1",'
           '"supportDistributeGoods":1,'
           '"promotionType":1,'
           '"discountMoney":10,'
           '"useMinMoney":20,'
           '"goodsNumber":0'
           '}'

}


'''操作优惠活动（开启、关闭）接口 '''

test_Pmsoperate={
    'api_key':'647b00ec1fe6990b1b97263b05341b6b',
    'timestamp':times,

    'data':'{'
           '"promotionId": 454,'
           '"adminId": 1,'
           '"status": 2'
           ' }'
}


'''更新订单支付状态'''

data_updatePayStatus={
    'api_key':'b47d4503ce201db6df525911812dd089',
    'timestamp':times,
    'order_sn':'DP08414562386338',
    'order_amount':'10',
    'trade_no':'2015122921001003610003783823',
    'pay_serial_no':'2015122964844',
    'pay_id':'1',
    'order_status':'1',

}

'''创建订单'''
data_create={
     'api_key':'b47d4503ce201db6df525911812dd089',
     'timestamp':times,
     'uid':'43507844',
     'consignee':'leo_peng',
     'mobile':13728142737,
     'products':'[{"product_id":10750 ,'
                '"goods_id":777,'
                '"goods_name":"test001",'
                '"shop_price":0.1,'
                '"goods_number":1,'
                '"supplier_id":128,'
                '"goods_own_type":1,'
                '"delivery_method":1'
                '}]'

}


'''通过商品id获取订单列表'''

data_OrderByProductId={
    'api_key':'d81b8598bc36a686cc8cbbd26599bd92',
    'uid':'43507844',
    'product_id':'10750',
    'goods_id':'777',



}




































      # 'promotionName':promotionNames
       #  'discountMoney''20',
        # 'useMinMoney':199,
        # 'sendNumLimit':1,
        # 'sendNum':1,
        # 'haveSentNum':1,
        # 'startTime':times,
        # 'endTime':dtimes,
        # 'getNumLimit':1,
        # 'adminId':0,
        # 'promotionTitle':Title,
        # 'receiveLimit':1,
        # 'type':0,
        # 'chargePer':0.65,
        # 'supplierChargePer':0.35,
        # 'promotionType':1,
        # 'supportMsGoods':1,
        # 'selfType':1,
        # 'supportDistributeGoods':1







































