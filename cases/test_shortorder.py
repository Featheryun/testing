from commom.login import Login
from commom.zone_change import Zone_change
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import datetime


class Test_shortorder:
    def test_shortorder(self, quriy, condition):
        f = open('test_shortorder_result.txt', 'a')
        login = Login()
        wd = login.login('15095859543', '123456')
        zone = Zone_change()
        wd = zone.zone_change('翠屏区', wd)
        time.sleep(1)
        starttime = ''
        endtime = ''
        msg = ''
        if wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[1]/div/div/div[1]').text not in '首页/订单管理/短时订单':
            wd.implicitly_wait(5)
            wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/aside/div/ul/li[6]/div').click()
            time.sleep(0.5)
            wd.find_element_by_xpath('//*[@id="/order$Menu"]/li[3]').click()
        wd.implicitly_wait(5)
        element = WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_link_text('展开'))
        element.click()
        wd.implicitly_wait(5)
        if condition == '用户姓名':
            wd.find_element_by_id('userName').send_keys(quriy)
        elif condition == '手机号码':
            wd.find_element_by_id('phone').send_keys(quriy)
        elif condition == '车辆编码':
            wd.find_element_by_id('vehicleSn').send_keys(quriy)
        elif condition == '终端编码':
            wd.find_element_by_id('terminalId').send_keys(quriy)
        elif condition == '故障类型':
            wd.find_element_by_id('faultFlag').click()
            if quriy == '刹车':
                wd.switch_to.active_element.send_key(Keys.DOWN)
            elif quriy == '车灯':
                wd.switch_to.active_element.send_key(2*Keys.DOWN)
            elif quriy == '车线':
                wd.switch_to.active_element.send_key(3*Keys.DOWN)
            elif quriy == '车座':
                wd.switch_to.active_element.send_key(4*Keys.DOWN)
            elif quriy == '脚蹬':
                wd.switch_to.active_element.send_key(5*Keys.DOWN)
            elif quriy == '车撑':
                wd.switch_to.active_element.send_key(6*Keys.DOWN)
            elif quriy == '挡泥板':
                wd.switch_to.active_element.send_key(7*Keys.DOWN)
            elif quriy == '其他':
                wd.switch_to.active_element.send_key(8*Keys.DOWN)
            wd.switch_to.active_element.send_key(Keys.ENTER)
        elif condition == '造成原因':
            wd.find_element_by_id('reasonFlag').click()
            if quriy == '被上私锁':
                wd.switch_to.active_element.send_key(Keys.DOWN)
            elif quriy == '尝试一下':
                wd.switch_to.active_element.send_key(2*Keys.DOWN)
            elif quriy == '车辆故障':
                wd.switch_to.active_element.send_key(3*Keys.DOWN)
            elif quriy == '其他':
                wd.switch_to.active_element.send_key(4*Keys.DOWN)
            wd.switch_to.active_element.send_key(Keys.ENTER)
        elif condition == '上报时间':
            wd.find_element_by_id('createAt').click()
            starttime = quriy.split('，')[0]
            endtime = quriy.split('，')[1]
            wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]/div').click()
            wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[5]/td[5]').click()
            wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(19*Keys.BACK_SPACE)
            wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(starttime)
            wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').click()
            wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(19*Keys.BACK_SPACE)
            wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(endtime)
            ActionChains(wd).move_by_offset(300, 200).click().perform()
        wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[1]/form/div[3]/div/button[1]').click()
        # wd.switch_to.active_element.send_keys(Keys.ENTER)
        time.sleep(2)

        try:
            msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]').text
            Flag = True
        except:
            Flag = False
        if Flag:
            if condition == '用户姓名':
                msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[3]').text
            elif condition == '手机号码':
                msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[4]').text
            elif condition == '车辆编码':
                msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]').text
            elif condition == '终端编码':
                msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]').text
            elif condition == '故障类型':
                msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[5]').text
            elif condition == '造成原因':
                msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[6]').text
            elif condition == '上报时间':
                msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[7]').text
                msg = datetime.date(*map(int, msg.split(' ')[0].split('-')))
                starttime = datetime.date(*map(int, starttime.split(' ')[0].split('-')))
                endtime = datetime.date(*map(int, endtime.split(' ')[0].split('-')))
                if msg >= starttime and msg <=  endtime:
                    msg = quriy
                else:
                    msg = ''
        else:
            msg = ''
        print(msg+'===============2')
        if quriy in msg:
            print('test_shortorder:'+condition+'=>'+quriy+'=========>sucess', file=f)
        else:
            print('test_shortorder:' + condition + '=>' + quriy + '=========>fail', file=f)


if __name__ == '__main__':
    test = Test_shortorder()
    # test.test_shortorder('2020-07-13 00:00:00，2020-07-14 00:00:00', '上报时间')
    # test.test_shortorder('张雪林', '用户姓名')
    # test.test_shortorder('15283638111', '手机号码')
    test.test_shortorder('511502000458', '车辆编码')
