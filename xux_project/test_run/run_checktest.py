__author__ = 'leo'
import time,sys
sys.path.append('./xux_project')
#sys.path.append('./setting')
import unittest
from setting.HTMLTestRunner import HTMLTestRunner
test_dir='/xux_project/test_case'

discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_checks.py')

if __name__ =="__main__":
    now=time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    filename ='/xux_project/report/'+now+'_result.html'
    fp=open(filename,'wb')
    runner =HTMLTestRunner(stream=fp,
                           title='check_allInterface Test Report',
                           description='Implementation Example whith:'
                           )
    runner.run(discover)
    fp.close()


