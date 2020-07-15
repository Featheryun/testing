from selenium import webdriver
import time
from commom.login import Login


class Test_Terminal:
    def test_terminal_terid_inqury(self, caseid, datas, results):
        f = open('result.txt', 'a')
        login = Login()
        wd = login.login('15095859543', '123456')
        wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/aside/div/ul/li[2]/div').click()
        time.sleep(0.1)
        wd.find_element_by_link_text('终端').click()
        wd.find_element_by_id("ecuId").send_keys(datas)
        wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[1]/form/div/div[4]/span/button[1]').click()
        time.sleep(1)
        msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div/table/tbody/tr/td[1]').text
        print(msg)
        if results in msg:
            print(caseid+'Test Sucessfully', file=f)
            print('成功')
        else:
            print(caseid+'Test Failed', file=f)

        f.close()
        wd.quit()

if __name__ == '__main__':
    test = Test_Terminal()
    test.test_terminal_terid_inqury('test_terminal001', '3451383', '3451383')