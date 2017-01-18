# -*- coding: utf-8 -*-
__author__ = 'leo'
import MySQLdb
import ToolsDB

'''该脚本用于修改良粉账号，通过修改数据库把良粉账号修改成非良粉账号 ==！
   良粉会员身份清除
    1、删掉入会订单
    2、删掉会员表
'''







def OrderDB():
  try:
        #print (unicode("请输入测试环境数据库（120,121,122,100）：",'utf-8').encode('gbk'))
        #Worders=raw_input()
        Worders=raw_input("请输入测试环境数据库（122,168,100）：")
        Worder=Worders.strip()#自动去空
        if Worder=='120':

            conn = ToolsDB.OrderDBconn(host="192.168.88.120",port=3306,user="testxiaoshuxiong", passwd="9bo0388lAxA4XsCY" ,db="mama_mall")
            return conn

        if Worder=='121':
            conn = ToolsDB.OrderDBconn(host="192.168.88.121",port=3306,user="testxiaoshuxiong", passwd="9bo0388lAxA4XsCY" ,db="mama_mall")
            return conn

        if Worder=='122':
            conn = ToolsDB.OrderDBconn(host="192.168.88.122",port=3306,user="testxiaoshuxiong", passwd="9bo0388lAxA4XsCY" ,db="mama_mall")
            return conn

        if Worder=='100':
            conn = ToolsDB.OrderDBconn('10.0.0.100','3306','testxiaoshuxiong', '9bo0388lAxA4XsCY','mama_mall')
            return conn

  except:
    print "输入数据库错误。"
  #  print (unicode("输入数据库错误。",'utf-8').encode('gbk'))
    OrderDB()
























def UpdataLF(conn,order_sn):
    conn=MySQLdb.connect(conn)
    print conn
    cur=conn.cursor()  #创建游标
    a=cur.execure("SELECT * FROM  mall_order_rebates WHERE order_sn='%order_sn'"%order_sn) #执行sql，查询入会订单是否存在
    b=cur.execure("SELECT buyser_user_id FROM  mall_order_rebates WHERE order_sn='%order_sn'"%order_sn)
    c=cur.execure("SELECT * FROM mall_user_distribution WHERE user_id='976'"%order_sn)#查询该用户的user_id
  #  cur.execure("DELETE  FROM mall_user_distribution WHERE user_id='976'"%order_sn)#删掉入会订单
  #  cur.execure("DELETE * FROM  mall_order_rebates WHERE order_sn='%order_sn'"%order_sn)#删掉会员表
    print a,b,c
    cur.close()
    conn.commit()
    conn.close()





def Oder_info(DB):

       # print ("请输入订单号，输入666可切换数据库：")
        print (unicode("请输入订单号，输入666可切换数据库：",'utf-8').encode('gbk'))
        Worder=raw_input()
        b=Worder.strip()
        if Worder=='666':
          #  print "正在重新选择测试环境，=。=！"
            print (unicode("正在重新选择测试环境，=。=！",'utf-8').encode('gbk'))
            OrderDB()
        elif Worder=='':
         #   print "输入内容为空，请重新输入，=。=！"
            print (unicode("输入内容为空，请重新输入，=。=！",'utf-8').encode('gbk'))
            OrderDB()
        else:
              a="SELECT * FROM  mall_order_rebates WHERE order_sn='%order_sn'"%b     #执行sql，查询入会订单是否存在
              # b=cur.execure("SELECT buyser_user_id FROM  mall_order_rebates WHERE order_sn='%order_sn'"%order_sn)
              # c=cur.execure("SELECT * FROM mall_user_distribution WHERE user_id='976'"%order_sn)#查询该用户的user_id




            order_sn= "SELECT order_sn FROM mall_order_info WHERE order_sn='%s'"%b
            order_amount = "SELECT order_amount FROM mall_order_info WHERE order_sn='%s'"%b  #获取商品价格
            datas=DB.ch_data(order_sn)
            Api_key = "SELECT api_key FROM mall_app WHERE app_id='1'"
            Api_secret = "SELECT api_secret FROM mall_app WHERE  app_id='1'"
         #   print datas

            if (datas!=None):#判断该订单是否存在，存在为1 不存在为0
             #   print('订单存在,正在修改订单状态')
                print(unicode("订单存在,正在修改订单状态。",'utf-8').encode('gbk'))
                payload=test_data.updatePayStatus
                print datas
                payload.setdefault('order_sn',str(datas))
            #    print payload
                order_amounts=DB.ch_data(order_amount)# 使用execute方法执行SQL语句
              #  print order_amounts
                payload.setdefault('order_amount',str(order_amounts))
              #  print payload
                Api_keys=DB.ch_data(Api_key)
                if  Api_keys == None:
                   # print(u"api_key 不存在，请检查接口数据！")
                    print(unicode("api_key 不存在。",'utf-8').encode('gbk'))
                else:
                    payload.setdefault('api_key',str(Api_keys))
                    Api_secrets=DB.ch_data(Api_secret)
                #    print  Api_secrets
                    if  Api_secrets !=None:
                 #       print payload
                        api_sign=api_signs.api_signs(payload,Api_secrets)
                        payload.setdefault('api_sign',api_sign)
                      #  print payload
                        r=requests.post(test_url.updatePayStatus_url, params=payload)
                      #  print payload
                        result=r.text
                        result_jsons.result_json(result)
                        del payload['order_sn']
                        del payload['order_amount']
                        del payload['api_sign']
                      #  print payload
                        Oder_info(DB)
                    else:
                       # print (u"该 api_secret 不存在")
                        print(unicode("api_secret 不存在。",'utf-8').encode('gbk'))
            else:
               # print u"该订单不存在，请重新输入，或检查连接库是否正确。"
                print(unicode("该订单不存在，请重新输入，或检查连接库是否正确。",'utf-8').encode('gbk'))
                Oder_info(DB)




