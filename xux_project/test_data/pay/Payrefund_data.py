# -*- coding: utf-8 -*-
__author__ = 'leo'
import sys
import time

times= int(time.time())
#成功退款
data_PayRefundSuces={
        'api_key':'b47d4503ce201db6df525911812dd089',
        'order_sn':'XS87414143650678',
        'own_mch_id':'10001',
        'refund_sn':'20161103112901840',
        'refund_money':'0.3',
        'refund_reason':'用户取消',
        'refund_notify_url':'http://localhost/refund_notify',
        'timestamp':times,
    }
