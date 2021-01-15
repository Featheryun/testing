from commom.login import Login
from commom.zone_change import Zone_change
import time
import io
import sys
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from util.str_to_dict import str_to_dict
import unittest
from ddt import ddt, data
from util.excel_read import excel_read
from HTMLTestRunner import HTMLTestRunner
import os
from commom.logoutput import LogOutput

class Test_Userinfo:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    def test_userinfo(self, caseid, data, reluts):
        data = str_to_dict(data)
        f = open('D:/testing/testfile/result1.txt', 'a')
        try:
            login = Login()
            wd = login.login('15095859543', '123456')
            wd.implicitly_wait(5)
            zone_chang = Zone_change()
            wd = zone_chang.zone_change('翠屏区', wd)
            time.sleep(0.5)
            if wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[1]/div/div/div[1]').text not in '首页/用户管理/用户信息':
                wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/aside/div/ul/li[4]/div[1]').click()
                time.sleep(0.5)
                wd.find_element_by_xpath('//*[@id="/cif$Menu"]/li[1]').click()
            # time.sleep(1)
            wd.implicitly_wait(5)
            element = WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_link_text('展开'))
            wd.execute_script('arguments[0].click();', element)     # 元素被覆盖
            # wd.find_element_by_link_text('展开').click()
            msg = ''
            condition1 = ''
            username1 = ''
            for key in data.keys():
                condition = key
                username = data[key]
                if condition == '信息查询':
                    wd.find_element_by_id('info').send_keys(username)
                elif condition == '用户ID':
                    wd.find_element_by_id('id').send_keys(username)
                elif condition == '注册时间':
                    startAt = username.split(',')[0]
                    endAt = username.split(',')[1]
                    wd.find_element_by_xpath('//*[@id="createAt"]/span/input[1]').click()
                    wd.implicitly_wait(5)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]/div').click()
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[5]/td[5]/div').click()
                    WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div/input')).send_keys(19*Keys.BACK_SPACE)
                    # wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(19*Keys.BACK_SPACE)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(startAt)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').click()
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(19*Keys.BACK_SPACE)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(endAt)
                    ActionChains(wd).move_by_offset(300, 100).click().perform()
                    time.sleep(1)

                elif condition == '账号状态':
                    wd.find_element_by_xpath('//*[@id="status"]/div/div').click()
                    wd.implicitly_wait(2)
                    if username == '注销':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '欠费状态':
                    elemet = WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_xpath('//*[@id="arrearsStatus"]/div/div'))
                    elemet.click()
                    if username == '无欠费':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)

                elif condition == '骑行状态':
                    wd.find_element_by_xpath('//*[@id="orderStatus"]/div/div').click()
                    wd.implicitly_wait(2)
                    if username == '骑行中':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    elif username == '临时锁车':
                        wd.switch_to.active_element.send_keys(2*Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '实名认证':
                    mouse = wd.find_element_by_xpath('//*[@id="realNameStatus"]/div/div')
                    mouse.click()
                    wd.implicitly_wait(2)
                    if username == '已实名':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    elif username == '实名失败':
                        wd.switch_to.active_element.send_keys(2*Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                    # wd.find_element_by_xpath('//*[@id="realNameStatus"]/div/div/div').send_keys(Keys.ENTER)
                elif condition == '违约状态':
                    element = WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_xpath('//*[@id="breachFlag"]/div/div'))
                    element.click()
                    if username == '有待处理违约':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '用车日期':
                    starttime = username.split(',')[0]
                    endtime = username.split(',')[1]
                    wd.find_element_by_xpath('//*[@id="orderAt"]/span/input[1]').click()
                    wd.implicitly_wait(5)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]/div').click()
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[5]/td[5]/div').click()
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(19*Keys.BACK_SPACE)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(starttime)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').click()
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(19*Keys.BACK_SPACE)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(endtime)
                    wd.implicitly_wait(5)
            time.sleep(0.5)
            wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[1]/form/div[4]/div/button[1]').click()
            time.sleep(0.5)
            try:
                wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[5]')
                flag = True
            except:
                flag = False
            for key in data.keys():
                condition = key
                username = data[key]
                if flag:
                    if condition == '信息查询':
                        msg1 = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[5]').text
                        msg = msg + ';' + msg1 + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[3]').text
                    elif condition == '用户ID':
                        msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]').text
                    elif condition == '账号状态':
                        msg = msg + ';' + wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[11]').text
                    elif condition == '欠费状态':
                        msg1 = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[17]').text
                        msg1 = msg1.split('元')[0]
                        if float(msg1) < 0:
                            msg = msg + ';' + '有欠费'
                        else:
                            msg = msg + ';' + '无欠费'
                    elif condition == '骑行状态':
                        msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[9]').text
                    elif condition == '实名认证':
                        msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[10]').text
                    elif condition == '违约状态':
                        msg1 = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[8]').text
                        if int(msg1) > 0:
                            msg = msg + ';' + '有待处理违约'
                        else:
                            msg = msg + ';' + '无待处理违约'
                    elif condition == '注册时间':
                        msg1 = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[16]').text
                        time1 = msg1.split(' ')[0].split('-')
                        date1 = datetime.date(*map(int, time1))
                        staAt = username.split(',')[0]
                        endAt = username.split(',')[1]
                        staAt = datetime.date(*map(int, staAt.split(' ')[0].split('-')))
                        endAt = datetime.date(*map(int, endAt.split(' ')[0].split('-')))
                        if staAt <= date1 and endAt >= date1:
                            msg = msg + ';' + username
                        else:
                            msg = msg + ';' + ''
                    elif condition == '用车日期':
                        msg1 = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[7]').text
                        time1 = msg1.split(' ')[0].split('-')
                        date1 = datetime.date(*map(int, time1))
                        staAt = username.split(',')[0]
                        endAt = username.split(',')[1]
                        staAt = datetime.date(*map(int, staAt.split(' ')[0].split('-')))
                        endAt = datetime.date(*map(int, endAt.split(' ')[0].split('-')))
                        if staAt <= date1 and endAt >= date1:
                            msg = msg + ';' + username
                        else:
                            msg = msg + ';' + ''
                    condition1 = condition1 + ';' + condition
                    username1 = username1 + ';' + username

                else:
                    msg = ''
            if username1 in msg:
                print(caseid + ':' + condition1[1:] + '=>' + username1[1:] + '====success', file=f)
            else:
                print(caseid + ':' + condition1[1:] + '=>' + username1[1:] + '====fail', file=f)
        except:
            print(caseid + ':execute================>error', file=f)
        f.close()
        wd.quit()


@ddt()
class Userinfo_TestCase(unittest.TestCase):
    datas1 = excel_read("D:\\testing\\util\\test_data.xlsx")
    userinfodatas = []
    for i in datas1:
        if 'userinfo' in i[0]:
            userinfodatas.append(i)
    @classmethod
    def setUpClass(cls):
        try:
            login = Login()
            wd = login.login('15095859543', '123456')
            wd.implicitly_wait(5)
            zone_chang = Zone_change()
            cls.wd = zone_chang.zone_change('珙县', wd)
        except:
            print('error')
        return cls.wd

    @data(*userinfodatas)
    def test_info(self, case):
        data = str_to_dict(case[4])
        caseid = case[0]
        result = case[5]
        wd = self.wd
        f = open('D:/testing/testfile/result1.txt', 'a')

        try:
            if wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/div/main/div/div/div[1]/div/div/div[1]').text not in '首页/用户管理/用户信息':
                wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/aside/div/ul/li[4]/div[1]').click()
                time.sleep(0.5)
                wd.find_element_by_xpath('//*[@id="/cif$Menu"]/li[1]').click()
                wd.implicitly_wait(5)
                element = WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_link_text('展开'))
                wd.execute_script('arguments[0].click();', element)     # 元素被覆盖
            msg = ''
            condition1 = ''
            username1 = ''
            for key in data.keys():
                condition = key
                username = data[key]
                if condition == '信息查询':
                    wd.find_element_by_id('info').send_keys(username)
                elif condition == '用户ID':
                    wd.find_element_by_id('id').send_keys(username)
                elif condition == '注册时间':
                    startAt = username.split(',')[0]
                    endAt = username.split(',')[1]
                    wd.find_element_by_xpath('//*[@id="createAt"]/span/input[1]').click()
                    wd.implicitly_wait(5)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]/div').click()
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[5]/td[5]/div').click()
                    WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div/input')).send_keys(19*Keys.BACK_SPACE)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(startAt)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').click()
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(19*Keys.BACK_SPACE)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(endAt)
                    ActionChains(wd).move_by_offset(300, 100).click().perform()

                elif condition == '账号状态':
                    wd.find_element_by_xpath('//*[@id="status"]/div/div').click()
                    wd.implicitly_wait(2)
                    if username == '注销':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '欠费状态':
                    elemet = WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_xpath('//*[@id="arrearsStatus"]/div/div'))
                    elemet.click()
                    if username == '无欠费':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)

                elif condition == '骑行状态':
                    wd.find_element_by_xpath('//*[@id="orderStatus"]/div/div').click()
                    wd.implicitly_wait(2)
                    if username == '骑行中':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    elif username == '临时锁车':
                        wd.switch_to.active_element.send_keys(2*Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '实名认证':
                    mouse = wd.find_element_by_xpath('//*[@id="realNameStatus"]/div/div')
                    mouse.click()
                    wd.implicitly_wait(2)
                    if username == '已实名':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    elif username == '实名失败':
                        wd.switch_to.active_element.send_keys(2*Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '违约状态':
                    element = WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_xpath('//*[@id="breachFlag"]/div/div'))
                    element.click()
                    if username == '有待处理违约':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '用车日期':
                    starttime = username.split(',')[0]
                    endtime = username.split(',')[1]
                    wd.find_element_by_xpath('//*[@id="orderAt"]/span/input[1]').click()
                    wd.implicitly_wait(5)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]/div').click()
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[5]/td[5]/div').click()
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(19*Keys.BACK_SPACE)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(starttime)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').click()
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(19*Keys.BACK_SPACE)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(endtime)
                    wd.implicitly_wait(5)
            time.sleep(0.5)
            wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/div/main/div/div/div[2]/div/div/div/div/div/div/div[1]/form/div[4]/div/button[1]').click()
            try:
                wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[5]')
                flag = True
            except:
                flag = False
            for key in data.keys():
                condition = key
                username = data[key]
                if flag:
                    if condition == '信息查询':
                        msg1 = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[5]').text
                        msg = msg + ';' + msg1 + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[3]').text
                    elif condition == '用户ID':
                        msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]').text
                    elif condition == '账号状态':
                        msg = msg + ';' + wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[11]').text
                    elif condition == '欠费状态':
                        msg1 = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[17]').text
                        msg1 = msg1.split('元')[0]
                        if float(msg1) < 0:
                            msg = msg + ';' + '有欠费'
                        else:
                            msg = msg + ';' + '无欠费'
                    elif condition == '骑行状态':
                        msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[9]').text
                    elif condition == '实名认证':
                        msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[10]').text
                    elif condition == '违约状态':
                        msg1 = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[8]').text
                        if int(msg1) > 0:
                            msg = msg + ';' + '有待处理违约'
                        else:
                            msg = msg + ';' + '无待处理违约'
                    elif condition == '注册时间':
                        msg1 = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[16]').text
                        date1 = datetime.datetime.strptime(msg1, '%Y-%m-%d %H:%M:S')
                        staAt = username.split(',')[0]
                        endAt = username.split(',')[1]
                        staAt = datetime.datetime.strptime(staAt, '%Y-%m-%d %H:%M:S')
                        endAt = datetime.datetime.strptime(endAt, '%Y-%m-%d %H:%M:S')
                        if staAt <= date1 and endAt >= date1:
                            msg = msg + ';' + username
                        else:
                            msg = msg + ';' + ''
                    elif condition == '用车日期':
                        msg1 = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[7]').text
                        date1 = datetime.datetime.strptime(msg1, '%Y-%m-%d %H:%M:S')
                        staAt = username.split(',')[0]
                        endAt = username.split(',')[1]
                        staAt = datetime.datetime.strptime(staAt, '%Y-%m-%d %H:%M:S')
                        endAt = datetime.datetime.strptime(endAt, '%Y-%m-%d %H:%M:S')
                        if staAt <= date1 and endAt >= date1:
                            msg = msg + ';' + username
                        else:
                            msg = msg + ';' + ''
                    condition1 = condition1 + ';' + condition
                    username1 = username1 + ';' + username

                else:
                    msg = ''
            if username1 in msg:
                print(caseid + ':' + condition1[1:] + '=>' + username1[1:] + '====success', file=f)
                self.assertEqual(1, 1)
            else:
                print(caseid + ':' + condition1[1:] + '=>' + username1[1:] + '====fail', file=f)
                self.assertEqual(1, 2)
        except:
            print(caseid + ':execute================>error', file=f)
            self.assertEqual(1, 2)
        wd.find_element_by_xpath(
            '//*[@id="root"]/div/div/div/section/section/div/main/div/div/div[2]/div/div/div/div/div/div/div[1]/form/div[4]/div/button[2]').click()
        self.wd = wd
        f.close()
        logoutput = LogOutput()
        logoutput.logOutput('D:/testing/testfile/test_userinfo_log.txt', 'test_userinfo')
        return self.wd

    @classmethod
    def tearDownClass(cls):
        cls.wd.quit()

from BeautifulReport import BeautifulReport
if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(Userinfo_TestCase('test_info'))
    result = BeautifulReport(suite)
    result.report(filename='用户信息', description='测试报告', report_dir='D:\\testing\\util', theme='theme_default')
    # pathro = os.path.abspath(os.path.dirname(__file__)) + '.html'

    # with open('D:\\testing\\util\\HTMLReport.html', 'wb') as report:
    #     runner = HTMLTestRunner(stream=report,
    #                             title='用户信息测试报表',
    #                             description='杨芸',
    #                             verbosity=2)
    #     runner.run(suite)
    # report.close()
    # test_userinfo = Test_Userinfo()
    # test_userinfo.test_userinfo('2020-07-10 00:00:00，2020-07-11 00:00:00', '注册时间')
    # test_userinfo.test_userinfo('有待处理违约', '违约状态')
    # test_userinfo.test_userinfo('test_userinfo', '骑行状态：空闲，违约状态：无待处理违约，注册时间：2020-07-10 00:00:00,2020-07-11 00:00:00', '')
