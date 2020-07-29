from selenium import webdriver
from commom.login import Login

#  登录用例
class Test_Login:
    # 登录成功
    def test_login_sucess(self, caseid, datas, results):
        f = open("D:/testing/testfile/test_login_sucess_result.txt", "a")
        username = datas.split('\n')[0].split('=')[1]
        pwd = datas.split('\n')[1].split('=')[1]
        login  = Login()
        wd = login.login(username, pwd)
        msg = wd.find_element_by_css_selector("#root > div > div > div > section > section > header > div > div > span:nth-child(3)").text
        if results in msg:
            print(caseid+'Test Sucessfully', file=f)
        else:
            print(caseid+'Test Failed', file=f)

        f.close()
        wd.quit()
    # 登录失败
    def test_login_fail(self, caseid, datas, results):
        f = open('D:/testing/testfile/test_login_fail_result.txt', 'a')
        username = datas.split('\n')[0].split('=')[1]
        pwd = datas.split('\n')[0].split('=')[1]
        login = Login()
        wd = login.login(username, pwd)
        msg = wd.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/form/div[1]/div[3]/div/div[2]').text
        if results in msg:
            print(caseid+'Test Sucessfully', file=f)
        else:
            print(caseid+'Test Failed', file=f)

        f.close()
        wd.quit()

