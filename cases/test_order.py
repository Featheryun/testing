import datetime
import time
from selenium.webdriver.common.keys import Keys
from commom.login import Login
from commom.zone_change import Zone_change
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from util.str_to_dict import str_to_dict

class Test_order:
    def test_order_singlequery(self, quiry, condition):
        f = open('D:/testing/testfile/test_order_result.txt', 'a')
        login = Login()
        wd = login.login('15095859543', '123456')
        zone = Zone_change()
        wd = zone.zone_change('翠屏区', wd)
        starttime = ''
        endtime = ''
        if wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[1]/div/div/div[1]').text not in '首页/订单管理/订单明细':
            time.sleep(1)
            wd.find_element_by_css_selector('#root > div > div > div > section > aside > div > ul > li:nth-child(6) > div.ant-menu-submenu-title').click()
            time.sleep(0.5)
            element = WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_xpath('//*[@id="/order$Menu"]/li[1]'))
            element.click()
            wd.implicitly_wait(5)
        element = wd.find_element_by_id('createAt')
        element1 = wd.find_element_by_xpath('//*[@id="createAt"]/span/i[1]')
        ActionChains(wd).move_to_element(element).click(element1).perform()
        # element = WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_xpath('//*[@id="createAt"]/span/i[1]'))
        # element.click()
        if condition == '订单编号':
            wd.find_element_by_id('id').send_keys(quiry)
        elif condition == '用户姓名':
            wd.find_element_by_id('realName').send_keys(quiry)
        elif condition == '手机号码':
            wd.find_element_by_id('phone').send_keys(quiry)
        elif condition == '车辆编码':
            wd.find_element_by_id('vehicleSn').send_keys(quiry)
        elif condition == '终端编号':
            wd.find_element_by_id('terminalId').send_keys(quiry)
        elif condition == '是否应付':
            wd.find_element_by_id('isHaveCharge').click()
            if quiry == '未应付':
                wd.switch_to.active_element.send_keys(Keys.DOWN)
            wd.switch_to.active_element.send_keys(Keys.ENTER)
        elif condition == '订单状态':
            wd.find_element_by_id('status').click()
            if quiry == '临时停车':
                wd.switch_to.active_element.send_keys(Keys.DOWN)
            elif quiry == '已结束':
                wd.switch_to.active_element.send_keys(2*Keys.DOWN)
            wd.switch_to.active_element.send_keys(Keys.ENTER)
        elif condition == '异常状态':
            wd.find_element_by_id('isAbnormal').click()
            if quiry == '有异常':
                wd.switch_to.active_element.send_keys(Keys.DOWN)
            wd.switch_to.active_element.send_keys(Keys.ENTER)
        elif condition == '是否违约':
            wd.find_element_by_id('isHaveViolation').click()
            if quiry == '无违约':
                wd.switch_to.active_element.send_keys(Keys.DOWN)
            wd.switch_to.active_element.send_keys(Keys.ENTER)
        elif condition == '用户类型':
            wd.find_element_by_id('isStaff').click()
            if quiry == '非员工':
                wd.switch_to.active_element.send_keys(Keys.DOWN)
            wd.switch_to.active_element.send_keys(Keys.ENTER)
        elif condition == '结束状态':
            wd.find_element_by_id('stopFlag').click()
            if quiry == '超时结束':
                wd.switch_to.active_element.send_keys(Keys.DOWN)
            elif quiry == 'boss结束':
                wd.switch_to.active_element.send_keys(2*Keys.DOWN)
            elif quiry == '运维结束':
                wd.switch_to.active_element.send_keys(3*Keys.DOWN)
            elif quiry == '余额不足':
                wd.switch_to.active_element.send_keys(4*Keys.DOWN)
            elif quiry == '通电时间未返回':
                wd.switch_to.active_element.send_keys(5*Keys.DOWN)
            elif quiry == '开锁后未返回服务区':
                wd.switch_to.active_element.send_keys(6*Keys.DOWN)
            wd.switch_to.active_element.send_keys(Keys.ENTER)
        elif condition == '取车位置':
            wd.find_element_by_id('stationId').click()
            if quiry == '站内':
                wd.switch_to.active_element.send_keys(Keys.DOWN)
            wd.switch_to.active_element.send_keys(Keys.ENTER)
        elif condition == '开始时间':
            wd.find_element_by_id('createAt').click()
            starttime = quiry.split('，')[0]
            endtime = quiry.split('，')[1]
            wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]').click()
            wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[5]/td[5]').click()
            wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(19*Keys.BACK_SPACE)
            wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(starttime)
            wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').click()
            wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(19*Keys.BACK_SPACE)
            wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(endtime)
            wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/div/a[2]').click()
        wd.implicitly_wait(5)
        wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[1]/form/div[5]/div/button[1]').click()
        time.sleep(2)
        msg = ''
        try:
            wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]')
            Flag = True
            print(1)
        except:
            Flag = False
            print(2)
        if Flag:
            if condition == '订单编号':
                msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]').text
            elif condition == '用户姓名':
                msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[3]').text
            elif condition == '手机号码':
                msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[4]').text
            elif condition == '车辆编码':
                msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[5]').text
            elif condition == '终端编号':
                msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[6]').text
            elif condition == '是否应付':
                msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[3]/div/div/table/tbody/tr[1]/td[3]').text
                if float(msg) <= 0:
                    msg = quiry
                else:
                    msg = ''
            elif condition == '订单状态':
                msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[8]').text
            elif condition == '异常状态':
                msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[3]/div/div/table/tbody/tr[1]/td[6]').text
            elif condition == '用户类型':
                msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[13]').text
            elif condition == '结束状态':
                msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[3]/div/div/table/tbody/tr[1]/td[5]').text
            elif condition == '取车位置':
                msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[9]').text
                if msg != '':
                    msg = quiry
                else:
                    msg = ''
            elif condition == '开始时间':
                msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[10]').text
                msg = datetime.date(*map(int, msg.split(' ')[0].split('-')))
                starttime = datetime.date(*map(int, starttime.split(' ')[0].split('-')))
                endtime = datetime.date(*map(int, endtime.split(' ')[0].split('-')))
                if msg >= starttime and msg <= endtime:
                    msg = quiry
                else:
                    msg = ''
        else:
            msg = ''
        print(msg)
        if quiry in msg:
            print('test_order:'+condition+'=>'+quiry+'=======================>sucess', file=f)
        else:
            print('test_order:'+condition+'=>'+quiry+'=======================>fail', file=f)

    def test_order_multiplequery(self, caseid, data, results):
        data = str_to_dict(data)
        f = open('D:/testing/testfile/test_order_result.txt', 'a')
        try:
            login = Login()
            wd = login.login('15095859543', '123456')
            zone = Zone_change()
            wd = zone.zone_change('翠屏区', wd)
            starttime = ''
            endtime = ''
            if wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[1]/div/div/div[1]').text not in '首页/订单管理/订单明细':
                time.sleep(1)
                wd.find_element_by_css_selector('#root > div > div > div > section > aside > div > ul > li:nth-child(6) > div.ant-menu-submenu-title').click()
                time.sleep(0.5)
                element = WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_xpath('//*[@id="/order$Menu"]/li[1]'))
                element.click()
                wd.implicitly_wait(10)
            element = wd.find_element_by_id('createAt')
            element1 = wd.find_element_by_xpath('//*[@id="createAt"]/span/i[1]')
            ActionChains(wd).move_to_element(element).click(element1).perform()
            # element = WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_xpath('//*[@id="createAt"]/span/i[1]'))
            # element.click()
            msg = ''
            condition1 = ''
            quiry1 = ''
            for key in data.keys():
                condition = key
                quiry = data[key]
                if condition == '订单编号':
                    wd.find_element_by_id('id').send_keys(quiry)
                elif condition == '用户姓名':
                    wd.find_element_by_id('realName').send_keys(quiry)
                elif condition == '手机号码':
                    wd.find_element_by_id('phone').send_keys(quiry)
                elif condition == '车辆编码':
                    wd.find_element_by_id('vehicleSn').send_keys(quiry)
                elif condition == '终端编号':
                    wd.find_element_by_id('terminalId').send_keys(quiry)
                elif condition == '是否应付':
                    wd.find_element_by_id('isHaveCharge').click()
                    if quiry == '未应付':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '订单状态':
                    wd.find_element_by_id('status').click()
                    if quiry == '临时停车':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    elif quiry == '已结束':
                        wd.switch_to.active_element.send_keys(2*Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '异常状态':
                    wd.find_element_by_id('isAbnormal').click()
                    if quiry == '有异常':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '是否违约':
                    wd.find_element_by_id('isHaveViolation').click()
                    if quiry == '无违约':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '用户类型':
                    wd.find_element_by_id('isStaff').click()
                    if quiry == '非员工':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '结束状态':
                    wd.find_element_by_id('stopFlag').click()
                    if quiry == '超时结束':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    elif quiry == 'boss结束':
                        wd.switch_to.active_element.send_keys(2*Keys.DOWN)
                    elif quiry == '运维结束':
                        wd.switch_to.active_element.send_keys(3*Keys.DOWN)
                    elif quiry == '余额不足':
                        wd.switch_to.active_element.send_keys(4*Keys.DOWN)
                    elif quiry == '通电时间未返回':
                        wd.switch_to.active_element.send_keys(5*Keys.DOWN)
                    elif quiry == '开锁后未返回服务区':
                        wd.switch_to.active_element.send_keys(6*Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '取车位置':
                    wd.find_element_by_id('stationId').click()
                    if quiry == '站内':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '开始时间':
                    wd.find_element_by_id('createAt').click()
                    time.sleep(0.5)
                    starttime = quiry.split(',')[0]
                    endtime = quiry.split(',')[1]
                    wd.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]').click()
                    wd.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[5]/td[5]').click()
                    wd.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(19*Keys.BACK_SPACE)
                    wd.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(starttime)
                    wd.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[2]/div[1]/div/input').click()
                    wd.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(19*Keys.BACK_SPACE)
                    wd.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(endtime)
                    wd.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[2]/div/a[2]').click()
                wd.implicitly_wait(5)
                # wd.find_element_by_xpath(
                #     '//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[1]/form/div[5]/div/button[2]').click()
                # time.sleep(8)
                quiry1 = quiry1 + ';' + quiry
                condition1 = condition1 + ';' + condition
            wd.find_element_by_xpath(
                '//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[1]/form/div[5]/div/button[1]').click()
            time.sleep(2)
            try:
                wd.find_element_by_xpath(
                    '//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]')
                Flag = True
                print(1)
            except:
                Flag = False
                print(2)
            if Flag:
                for key in data.keys():
                    condition = key
                    quiry = data[key]
                    if '订单编号' == condition:
                        msg = msg + ';' + wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]').text
                    elif '用户姓名' == condition:
                        msg = msg + ';' + wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[3]').text
                    elif '手机号码' == condition:
                        msg = msg + ';' + wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[4]').text
                    elif '车辆编码' == condition:
                        msg = msg + ';' + wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[5]').text
                    elif '终端编号' == condition:
                        msg = msg + ';' + wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[6]').text
                    elif '是否应付' == condition:
                        msg1 = wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[3]/div/div/table/tbody/tr[1]/td[3]').text
                        if float(msg1) <= 0:
                            msg = msg + ';' + quiry
                        else:
                            msg = msg + ';' + ''
                    elif '订单状态' == condition:
                        msg = msg + ';' + wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[8]').text
                    elif '异常状态' == condition:
                        msg = msg + ';' + wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[3]/div/div/table/tbody/tr[1]/td[6]').text
                    elif '用户类型' == condition:
                        msg = msg + ';' + wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[13]').text
                    elif '结束状态' == condition:
                        msg = msg + ';' + wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[3]/div/div/table/tbody/tr[1]/td[5]').text
                    elif '取车位置' == condition:
                        msg1 = wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[9]').text
                        if msg1 != '':
                            msg = msg + quiry
                        else:
                            msg = msg + ''
                    elif '开始时间' == condition:
                        msg1 = wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[10]').text
                        msg1 = datetime.date(*map(int, msg1.split(' ')[0].split('-')))
                        starttime = datetime.date(*map(int, starttime.split(' ')[0].split('-')))
                        endtime = datetime.date(*map(int, endtime.split(' ')[0].split('-')))
                        if msg1 >= starttime and msg1 <= endtime:
                            msg = msg + ';' + quiry
                        else:
                            msg = msg + ';' + ''
            else:
                msg = msg + ';' + ''
            print(msg)
            print(condition1)
            print(quiry1)
            if quiry1 in msg:
                print(caseid + ':' + condition1[1:] + '=>' + quiry1[1:] + '=======================>sucess', file=f)
            else:
                print(caseid + ':' + condition1[1:] + '=>' + quiry1[1:] + '=======================>fail', file=f)
        except:
            print(caseid + ':execute================>error', file=f)

    def test1(self, a):
        for key in a.keys():
            print(key+a[key])
        print(a)

    def str_to_dict(self, s):
        b = s.split('，')
        c = list()
        d = list()
        for i in b:
            c.append(i.split('：')[0])
            d.append(i.split('：')[1])
        print(c)
        print(d)
        e = dict(zip(c, d))
        print(e)
        return e
import unittest
from  ddt import ddt, data
from util.excel_read import excel_read
from util.str_to_dict import str_to_dict

@ddt()
class Order_TestCase(unittest.TestCase):
    datas = excel_read('D:\\testing\\util\\test_data.xlsx')
    orderdatas = []
    for i in datas:
        if 'order' in i[0]:
            orderdatas.append(i)
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

    @data(*orderdatas)
    def test_order(self, case):
        data = str_to_dict(case[4])
        caseid = case[0]
        result = case[5]
        f = open('D:/testing/testfile/test_order_result.txt', 'a')
        wd = self.wd
        try:
            starttime = ''
            endtime = ''
            if wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/div/main/div/div/div[1]/div/div/div[1]').text not in '首页/订单管理/订单明细':
                wd.find_element_by_css_selector(
                    '#root > div > div > div > section > aside > div > ul > li:nth-child(6) > div.ant-menu-submenu-title').click()
                time.sleep(0.5)
                element = WebDriverWait(wd, 10).until(
                    lambda driver: wd.find_element_by_xpath('//*[@id="/order$Menu"]/li[1]'))
                element.click()
                wd.implicitly_wait(10)
            element = wd.find_element_by_id('createAt')
            element1 = wd.find_element_by_xpath('//*[@id="createAt"]/span/i[1]')
            ActionChains(wd).move_to_element(element).click(element1).perform()
            # element = WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_xpath('//*[@id="createAt"]/span/i[1]'))
            # element.click()
            msg = ''
            condition1 = ''
            quiry1 = ''
            for key in data.keys():
                condition = key
                quiry = data[key]
                if condition == '订单编号':
                    wd.find_element_by_id('id').send_keys(quiry)
                elif condition == '用户姓名':
                    wd.find_element_by_id('realName').send_keys(quiry)
                elif condition == '手机号码':
                    wd.find_element_by_id('phone').send_keys(quiry)
                elif condition == '车辆编码':
                    wd.find_element_by_id('vehicleSn').send_keys(quiry)
                elif condition == '终端编号':
                    wd.find_element_by_id('terminalId').send_keys(quiry)
                elif condition == '是否应付':
                    wd.find_element_by_id('isHaveCharge').click()
                    if quiry == '未应付':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '订单状态':
                    wd.find_element_by_id('status').click()
                    if quiry == '临时停车':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    elif quiry == '已结束':
                        wd.switch_to.active_element.send_keys(2 * Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '异常状态':
                    wd.find_element_by_id('isAbnormal').click()
                    if quiry == '有异常':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '是否违约':
                    wd.find_element_by_id('isHaveViolation').click()
                    if quiry == '无违约':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '用户类型':
                    wd.find_element_by_id('isStaff').click()
                    if quiry == '非员工':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '结束状态':
                    wd.find_element_by_id('stopFlag').click()
                    if quiry == '超时结束':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    elif quiry == 'boss结束':
                        wd.switch_to.active_element.send_keys(2 * Keys.DOWN)
                    elif quiry == '运维结束':
                        wd.switch_to.active_element.send_keys(3 * Keys.DOWN)
                    elif quiry == '余额不足':
                        wd.switch_to.active_element.send_keys(4 * Keys.DOWN)
                    elif quiry == '通电时间未返回':
                        wd.switch_to.active_element.send_keys(5 * Keys.DOWN)
                    elif quiry == '开锁后未返回服务区':
                        wd.switch_to.active_element.send_keys(6 * Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '取车位置':
                    wd.find_element_by_id('stationId').click()
                    if quiry == '站内':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '开始时间':
                    wd.find_element_by_id('createAt').click()
                    time.sleep(0.5)
                    starttime = quiry.split(',')[0]
                    endtime = quiry.split(',')[1]
                    wd.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]').click()
                    wd.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[5]/td[5]').click()
                    wd.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(
                        19 * Keys.BACK_SPACE)
                    wd.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(starttime)
                    wd.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div[2]/div[1]/div/input').click()
                    wd.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(
                        19 * Keys.BACK_SPACE)
                    wd.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(endtime)
                    wd.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[2]/div/a[2]').click()
                wd.implicitly_wait(5)
                # wd.find_element_by_xpath(
                #     '//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[1]/form/div[5]/div/button[2]').click()
                # time.sleep(8)
                quiry1 = quiry1 + ';' + quiry
                condition1 = condition1 + ';' + condition
            time.sleep(0.5)
            wd.find_element_by_xpath(
                '//*[@id="root"]/div/div/div/section/section/div/main/div/div/div[2]/div/div/div/div/div/div/div[1]/form/div[5]/div/button[1]').click()
            time.sleep(0.5)
            try:
                wd.find_element_by_xpath(
                    '//*[@id="root"]/div/div/div/section/section/div/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]')
                Flag = True
            except:
                Flag = False
                print(1)
            if Flag:
                for key in data.keys():
                    condition = key
                    quiry = data[key]
                    if '订单编号' == condition:
                        msg = msg + ';' + wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/div/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]').text
                    elif '用户姓名' == condition:
                        msg = msg + ';' + wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/div/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[3]').text
                    elif '手机号码' == condition:
                        msg = msg + ';' + wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/div/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[4]').text
                    elif '车辆编码' == condition:
                        msg = msg + ';' + wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/div/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[5]').text
                    elif '终端编号' == condition:
                        msg = msg + ';' + wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/div/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[6]').text
                    elif '是否应付' == condition:
                        msg1 = wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/div/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[3]/div/div/table/tbody/tr[1]/td[3]').text
                        if float(msg1) <= 0:
                            msg = msg + ';' + quiry
                        else:
                            msg = msg + ';' + ''
                    elif '订单状态' == condition:
                        msg = msg + ';' + wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/div/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[8]').text
                    elif '异常状态' == condition:
                        msg = msg + ';' + wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/div/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[3]/div/div/table/tbody/tr[1]/td[6]').text
                    elif '用户类型' == condition:
                        msg = msg + ';' + wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/div/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[13]').text
                    elif '结束状态' == condition:
                        msg = msg + ';' + wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/div/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[3]/div/div/table/tbody/tr[1]/td[5]').text
                    elif '开始时间' == condition:
                        msg1 = wd.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div/section/section/div/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[10]').text
                        msg1 = datetime.date(*map(int, msg1.split(' ')[0].split('-')))
                        starttime = datetime.date(*map(int, starttime.split(' ')[0].split('-')))
                        endtime = datetime.date(*map(int, endtime.split(' ')[0].split('-')))
                        if msg1 >= starttime and msg1 <= endtime:
                            msg = msg + ';' + quiry
                        else:
                            msg = msg + ';' + ''
            else:
                msg = msg + ';' + ''
            print(msg)
            print(quiry1)
            if quiry1 in msg:
                print(caseid + ':' + condition1[1:] + '=>' + quiry1[1:] + '=======================>sucess', file=f)
                self.assertEqual(1, 1)
            else:
                print(caseid + ':' + condition1[1:] + '=>' + quiry1[1:] + '=======================>fail', file=f)
                self.assertEqual(1, 2)
        except:
            print(caseid + ':execute================>error', file=f)
            self.assertEqual(1, 2)
        try:
            wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/div/main/div/div/div[2]/div/div/div/div/div/div/div[1]/form/div[5]/div/button[2]').click()
        except:
            self.assertEqual(1, 2)
        self.wd = wd
        return self.wd

    @classmethod
    def tearDownClass(cls):
        cls.wd.quit()


if __name__ == '__main__':
    test = Test_order()
    # test.test_order_singlequery('boss结束', '结束状态')
    # test.test_order_singlequery('邓安红', '用户姓名')
    # test.test_order_singlequery('15681789188', '手机号码')
    # test.test_order_singlequery('2020-07-13 00:00:00，2020-07-14 00:00:00', '开始时间')
    # test.test_order_singlequery('511502000454', '车辆编码')
    # test.test_order_singlequery('3463496', '终端编号')
    # test.test_order_singlequery('已结束', '订单状态')
    # test.test_order_singlequery('无异常', '异常状态')
    # test.test_order_singlequery('非员工', '用户类型')
    # test.test_order_singlequery('余额不足', '结束状态')
    # test.test_order_multiplequery(结束状态='boss结束', 开始时间='2020-07-13 00:00:00，2020-07-14 00:00:00', 用户类型='非员工')
    # test.test_order_multiplequery(结束状态='超时结束')
    # test.test_order_multiplequery(订单状态='骑行中', 异常状态='无异常')
    s = '结束状态：boss结束，开始时间：2020-07-13 00:00:00,2020-07-14 00:00:00，用户类型：非员工'
    # s = test.str_to_dict(s)
    test.test_order_multiplequery('test_order001', s, '')