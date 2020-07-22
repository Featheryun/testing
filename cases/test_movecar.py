import datetime

from commom.login import Login
from commom.zone_change import Zone_change
from util.str_to_dict import str_to_dict
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class Test_movecar:
    def test_movecar(self, caseid, data, results):
        data = str_to_dict(data)
        f = open('test_movecar_result.txt', 'a')
        msg = ''
        condition1 = ''
        query1 = ''
        try:
            login = Login()
            wd = login.login('15095859543', '123456')
            zone = Zone_change()
            wd = zone.zone_change('巴中市', wd)
            if wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[1]/div/div/div[1]').text not in '首页/挪车管理/正在挪车':
                time.sleep(1.5)
                wd.find_element_by_css_selector('#root > div > div > div > section > aside > div > ul > li:nth-child(10) > div').click()
                element = WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_xpath('//*[@id="/bike/moving$Menu"]/li[2]'))
                element.click()
            wd.implicitly_wait(5)
            for key in data.keys():
                condition = key
                query = data[key]
                if condition == '车辆编码':
                    wd.find_element_by_id('vehicleSn').send_keys(query)
                elif condition == '员工姓名':
                    wd.find_element_by_id('creatorName').send_keys(query)
                elif condition == '开始时间':
                    starttime = query.split(',')[0]
                    endtime = query.split(',')[1]
                    wd.find_element_by_id('createAt').click()
                    element = WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]'))
                    element.click()
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[5]/td[5]').click()
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(19*Keys.BACK_SPACE)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(starttime)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').click()
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(19*Keys.BACK_SPACE)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(endtime)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/div/a[2]').click()
            wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[1]/form/div/div[4]/span/button[1]').click()
            time.sleep(1)
            try:
                wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]')
                Flag = True
            except:
                Flag = False
            if Flag:
                for key in data.keys():
                    condition = key
                    query = data[key]
                    if condition == '车辆编码':
                        msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]').text
                    elif condition == '员工姓名':
                        msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[7]').text
                    elif condition == '开始时间':
                        time1 = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[6]').text
                        time1 = datetime.date(*map(int, time1.split(' ')[0].split('-')))
                        starttime = datetime.date(*map(int, query.split(',')[0].split(' ')[0].split('-')))
                        endtime = datetime.date(*map(int, query.split(',')[1].split(' ')[0].split('-')))
                        if time1 >= starttime and time1 <= endtime:
                            msg = msg + ';' + query
                        else:
                            msg = msg + ';' + ' '
                    condition1 = condition1 + ';' + condition
                    query1 = query1 + ';' + query
            else:
                query1 = ' 查询为空'
            if query1 in msg:
                print(caseid + ':' + condition1[1:] + '==>' + query1[1:] + '====================>sucess', file=f)
            else:
                print(caseid + ':' + condition1[1:] + '==>' + query1[1:] + '====================>fail', file=f)
            wd.quit()
        except:
            print(caseid + ':execute==============>error', file=f)
        f.close()


if __name__ == '__main__':
    test = Test_movecar()
    # test.test_movecar('test_movecar001', '员工姓名：赵楠', '')
    test.test_movecar('test_movecar002', '开始时间：2020-07-20 00:00:00,2020-07-21 00:00:00', '')
