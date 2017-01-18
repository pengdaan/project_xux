__author__ = 'Administrator'
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        self.base_url="http://www.xiaoshuxiong.com/api/order/createOrderDp"


    def tearDown(self):

        print(self.code,self.text)
