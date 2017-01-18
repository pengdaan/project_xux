# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):

        #点评相关接口
        self.orderDP_url="http://www.xiaoshuxiong.com/api/order/createOrderDp"
        self.DPverify ='http://www.xiaoshuxiong.com/api/ocoupon/verify'#点评验卷接口
        self.UserOrderListDP_url='http://www.xiaoshuxiong.com/api/order/getUserOrderListDianping' #获取用户订单列表-点评项目

        #旅游相关接口
        self.OrderBySnTour_url ="http://www.xiaoshuxiong.com/api/order/getOrderBySnTour"
        self.OrderByGoTime_url='http://www.xiaoshuxiong.com/api/order/getOrderByGoTime'
        self.UserOrderListTour_url='http://www.xiaoshuxiong.com/api/order/getUserOrderListTour'
        self.UserOrderNums_url='http://www.xiaoshuxiong.com/api/order/getUserOrderNums'

        #pms接口
        self.PMSadd_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/add'
        self.PMSoperate_url='http://pms.api.xiaoshuxiong.com/pmsapi/action/promotion/operate'

        #order接口
        self.updatePayStatus_url='http://www.xiaoshuxiong.com/api/order/updatePayStatus'
        self.create_url='http://order.api.xiaoshuxiong.com/order/create'
        self.OrderByProductId_url='http://www.xiaoshuxiong.com/api/order/getOrderByProductId'









    def tearDown(self):
       # pass

        print(self.code,self.msgs)
