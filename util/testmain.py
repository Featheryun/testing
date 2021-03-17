import unittest
import os
import sys
from BeautifulReport import BeautifulReport
import time

datedemo = time.strftime('%Y-%m-%d-%H')
# print(os.path.abspath(__file__))
# print(os.path.dirname(__file__))
current_directory = os.path.dirname(os.path.abspath(__file__))
# print(current_directory)
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
# print(root_path)
sys.path.append(root_path)
from commom.send_email import send_email
from commom.logoutput import LogOutput
# pathro2 = os.path.abspath(os.path.dirname(__file__))+datedemo+'.html'
discover = unittest.defaultTestLoader.discover('D:\\testing\\cases\\', pattern="test_*.py")
logoutput = LogOutput()
logoutput.logOutput('D:/testing/testfile/', 'testmain.py')
if __name__ == "__main__":
    report = BeautifulReport(discover)
    a = '用户信息(' + datedemo + ').html'
    report.report(filename=a, description='测试报告', report_dir='D:\\testing\\util', theme='theme_default')
    send_email('D:\\testing\\util\\'+a)
    # with open(pathro2, "wb")as file:
    #     runner = HTMLTestRunner(stream=file, title="测试报告", description="杨芸")
    #     runner.run(discover)