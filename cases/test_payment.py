from commom.zone_change import Zone_change
from commom.login import Login
import time
import datetime
from selenium.webdriver.common.keys import Keys
from util.str_to_dict import str_to_dict


class Test_payment:
    def test_payment(self, caseid, data, results):
        data = str_to_dict(data)
        f = open('D:/testing/testfile/test_payment_result.txt', 'a')
        try:
            login = Login()
            wd = login.login('15095859543', '123456')
            zone = Zone_change()
            wd = zone.zone_change('翠屏区', wd)
            time.sleep(1.5)
            msg = ''
            condition1 = ''
            query1 = ''
            if wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[1]/div/div/div[1]').text not in '首页/财务管理/支付明细':
                wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/aside/div/ul/li[13]/div').click()
                time.sleep(1)
                wd.find_element_by_xpath('//*[@id="/payment$Menu"]/li').click()
                time.sleep(1)
            for key in data.keys():
                condition = key
                query = data[key]
                if condition == '用户姓名':
                    wd.find_element_by_id('trueName').send_keys(query)
                elif condition == '手机号码':
                    wd.find_element_by_id('phone').send_keys(query)
                elif condition == '支付情况':
                    wd.find_element_by_id('status').click()
                    if query == '取消支付':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '收费类型':
                    wd.find_element_by_id('chargeType').click()
                    if query == '罚金缴纳':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '发起时间':
                    wd.find_element_by_id('createAt').click()
                    starttime = query.split(',')[0]
                    endtime = query.split(',')[1]
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]').click()
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[5]/td[5]').click()
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(19*Keys.BACK_SPACE)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(starttime)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').click()
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(19*Keys.BACK_SPACE)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(endtime)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/div/a[2]').click()
                elif condition == '成功时间':
                    wd.find_element_by_id('fillAt').click()
                    starttime = query.split(',')[0]
                    endtime = query.split(',')[1]
                    wd.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]').click()
                    wd.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[5]/td[5]').click()
                    wd.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(19*Keys.BACK_SPACE)
                    wd.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(starttime)
                    wd.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[2]/div[1]/div/input').click()
                    wd.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(19*Keys.BACK_SPACE)
                    wd.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(endtime)
                    wd.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[2]/div/a[2]').click()
            wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[1]/form/div[3]/div/button[1]').click()
            time.sleep(1)
            try:
                wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[1]')
                Flag = True
            except:
                Flag = False
            if Flag:
                for key in data.keys():
                    condition = key
                    query = data[key]
                    if condition == '用户姓名':
                        msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[1]').text
                    elif condition == '手机号码':
                        msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]').text
                    elif condition == '支付情况':
                        msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[5]/span').text
                    elif condition == '收费类型':
                        msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[6]/span/span[2]').text
                    elif condition == '发起时间':
                        time1 = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[3]/div/div/table/tbody/tr[1]/td[1]').text
                        time1 = datetime.date(*map(int, time1.split(' ')[0].split('-')))
                        starttime = datetime.date(*map(int, query.split(',')[0].split(' ')[0].split('-')))
                        endtime = datetime.date(*map(int, query.split(',')[1].split(' ')[0].split('-')))
                        if time1 >= starttime and time1 <= endtime:
                            msg = msg + ';' + query
                        else:
                            msg = msg + ';' + ' '
                    elif condition == '成功时间':
                        time1 = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[3]/div/div/table/tbody/tr[1]/td[2]').text
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
                msg = ''
            if query1 in msg:
                print(caseid + ':' + condition1[1:] + ' ==> ' + query1[1:] + '===============>sucess', file=f)
            elif msg == results:
                print(caseid + ':' + condition1[1:] + ' ==> ' + msg + '===============>sucess', file=f)
            else:
                print(caseid + ':' + condition1[1:] + ' ==> ' + query1[1:] + '===============>fail', file=f)
        except:
            print(caseid + ':execute========>error', file=f)

if __name__ == '__main__':
    test = Test_payment()
    test.test_payment('test_payment001', '用户姓名：赵强，发起时间：2020-07-10 00:00:00,2020-07-17 00:00:00', '')
    # test.test_payment('test_payment002', '')
