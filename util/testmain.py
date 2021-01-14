import unittest
from HTMLTestRunner import HTMLTestRunner
import os
from BeautifulReport import BeautifulReport
import time
datedemo = time.strftime('%Y-%m-%d-%H')
# pathro2 = os.path.abspath(os.path.dirname(__file__))+datedemo+'.html'
discover = unittest.defaultTestLoader.discover('D:\\testing\\cases\\', pattern="test_*.py")
if __name__ == "__main__":
    report = BeautifulReport(discover)
    a = '用户信息(' + datedemo + ')'
    report.report(filename=a, description='测试报告', report_dir='D:\\testing\\util', theme='theme_default')
    # with open(pathro2, "wb")as file:
    #     runner = HTMLTestRunner(stream=file, title="测试报告", description="杨芸")
    #     runner.run(discover) 