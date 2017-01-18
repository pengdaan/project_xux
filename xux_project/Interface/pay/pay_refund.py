# -*- coding: utf-8 -*-
__author__ = 'leo'
import unittest


#退款接口：http://wiki.corp.mama.cn/pages/viewpage.action?pageId=65077644
class MyTest(unittest.TestCase):
    def setUp(self):
        self.Payrefund_url="http://pay.xiaoshuxiong.com/refund/send"


    def tearDown(self):

        print(self.code,self.msgs)
