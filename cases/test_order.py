import datetime
import time
from selenium.webdriver.common.keys import Keys
from commom.login import Login
from commom.zone_change import Zone_change
from selenium.webdriver.support.ui import WebDriverWait

class Test_order:
    def test_order(self, quiry, condition):
        f = open('test_order_result.txt', 'a')
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


if __name__ == '__main__':
    test = Test_order()
    # test.test_order('boss结束', '结束状态')
    # test.test_order('邓安红', '用户姓名')
    # test.test_order('15681789188', '手机号码')
    # test.test_order('2020-07-13 00:00:00，2020-07-14 00:00:00', '开始时间')
    # test.test_order('511502000454', '车辆编码')
    # test.test_order('3463496', '终端编号')
    # test.test_order('已结束', '订单状态')
    # test.test_order('无异常', '异常状态')
    # test.test_order('非员工', '用户类型')
    test.test_order('通电时间未返回', '结束状态')