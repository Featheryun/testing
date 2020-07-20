from commom.login import Login
from commom.zone_change import Zone_change
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import datetime
from util.str_to_dict import str_to_dict


class Test_vehiclefailure:
    def test_vehiclefailure(self, caseid, data, results):
        data = str_to_dict(data)
        msg = ''
        condition1 = ''
        quiry1 = ''
        f = open('test_vehiclefailure_result.txt', 'a')
        try:
            login  = Login()
            wd = login.login('15095859543', '123456')
            zone_change = Zone_change()
            wd = zone_change.zone_change('翠屏区', wd)
            time.sleep(1)
            if wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[1]/div/div/div[1]').text not in '首页/用户管理/车辆报障':
                wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/aside/div/ul/li[4]/div[1]').click()
                time.sleep(1)
                wd.find_element_by_xpath('//*[@id="/cif$Menu"]/li[2]/a').click()
            element = WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_link_text('展开'))
            wd.execute_script('arguments[0].click();', element)
            for key in data.keys():
                condition = key
                quiry = data[key]
                if condition == '用户姓名':
                    wd.find_element_by_id('reporterName').send_keys(quiry)
                elif condition == '车辆编码':
                    wd.find_element_by_id('deviceSn').send_keys(quiry)
                elif condition == '报障类型（用户）':
                    wd.find_element_by_xpath('//*[@id="userFlag"]/div').click()
                    wd.implicitly_wait(5)
                    if quiry == '刹车':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    elif quiry == '车灯':
                        wd.switch_to.active_element.send_keys(2*Keys.DOWN)
                    elif quiry == '车险':
                        wd.switch_to.active_element.send_keys(3*Keys.DOWN)
                    elif quiry == '车座':
                        wd.switch_to.active_element.send_keys(4*Keys.DOWN)
                    elif quiry == '脚蹬':
                        wd.switch_to.active_element.send_keys(5*Keys.DOWN)
                    elif quiry == '车撑':
                        wd.switch_to.active_element.send_keys(6*Keys.DOWN)
                    else:
                        wd.switch_to.active_element.send_keys(7*Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '报障类型（员工）':
                    element = WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_id('staffFlag'))
                    element.click()
                    # wd.find_element_by_id('staffFlag').click()
                    wd.implicitly_wait(5)
                    if quiry == '脚踏':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    elif quiry == '曲柄':
                        wd.switch_to.active_element.send_keys(2*Keys.DOWN)
                    elif quiry == '坐垫':
                        wd.switch_to.active_element.send_keys(3*Keys.DOWN)
                    elif quiry == '前后挡泥板':
                        wd.switch_to.active_element.send_keys(4*Keys.DOWN)
                    elif quiry == '侧撑':
                        wd.switch_to.active_element.send_keys(5*Keys.DOWN)
                    elif quiry == '车篮':
                        wd.switch_to.active_element.send_keys(6*Keys.DOWN)
                    elif quiry == '座桶前围':
                        wd.switch_to.active_element.send_keys(7*Keys.DOWN)
                    elif quiry == '掉漆':
                        wd.switch_to.active_element.send_keys(8*Keys.DOWN)
                    elif quiry == '二维码':
                        wd.switch_to.active_element.send_keys(9*Keys.DOWN)
                    elif quiry == '广告牌':
                        wd.switch_to.active_element.send_keys(10*Keys.DOWN)
                    elif quiry == '其他（外观损坏）':
                        wd.switch_to.active_element.send_keys(11*Keys.DOWN)
                    elif quiry == '前大灯':
                        wd.switch_to.active_element.send_keys(12*Keys.DOWN)
                    elif quiry == '方向盘':
                        wd.switch_to.active_element.send_keys(13*Keys.DOWN)
                    elif quiry == '车把':
                        wd.switch_to.active_element.send_keys(14*Keys.DOWN)
                    elif quiry == '拧把':
                        wd.switch_to.active_element.send_keys(15*Keys.DOWN)
                    elif quiry == '刹车':
                        wd.switch_to.active_element.send_keys(16*Keys.DOWN)
                    elif quiry == '后大灯':
                        wd.switch_to.active_element.send_keys(17*Keys.DOWN)
                    elif quiry == '电机':
                        wd.switch_to.active_element.send_keys(18*Keys.DOWN)
                    elif quiry == '开关锁':
                        wd.switch_to.active_element.send_keys(19*Keys.DOWN)
                    elif quiry == '行驶断电':
                        wd.switch_to.active_element.send_keys(20*Keys.DOWN)
                    elif quiry == '其他（功能故障）':
                        wd.switch_to.active_element.send_keys(21*Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '上报来源':
                    element = WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_id('reporterType'))
                    element.click()
                    # wd.find_element_by_id('reporterType').click()
                    if quiry == '员工':
                        wd.switch_to.active_element.send_keys(Keys.DOWN)
                    wd.switch_to.active_element.send_keys(Keys.ENTER)
                elif condition == '上报时间':
                    element = WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_id('createAt'))
                    element.click()
                    wd.implicitly_wait(5)
                    starttime = quiry.split('，')[0]
                    endtime = quiry.split('，')[1]
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]').click()
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[5]/td[5]').click()
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(19*Keys.BACK_SPACE)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div/input').send_keys(starttime)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').click()
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(19*Keys.BACK_SPACE)
                    wd.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[1]/div[2]/div[1]/div/input').send_keys(endtime)
                    ActionChains(wd).move_by_offset(300, 100).click().perform()
            element = WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div[1]/div/div/div/div/div[1]/form/div[3]/div/button[1]'))
            element.click()
            time.sleep(2)
            try:
                msg = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]').text
                Flag = True
            except:
                Flag = False
            if Flag:
                for key in data.keys():
                    condition = key
                    quiry = data[key]
                    if condition == '用户姓名':
                        msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[6]').text
                    elif condition == '车辆编码':
                        msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]').text
                    elif condition == '报障类型（用户）':
                        msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[3]').text
                    elif condition == '报障类型（员工）':
                        msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[3]').text
                    elif condition == '上报来源':
                        msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[5]').text
                    elif condition == '上报时间':
                        msg1 = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[8]').text
                        time1 = msg1.split(' ')[0].split('-')
                        time1 = datetime.date(*map(int, time1))
                        starttime = datetime.date(*map(int, quiry.split(',')[0].split(' ')[0].split('-')))
                        endtime = datetime.date(*map(int, quiry.split(',')[1].split(' ')[0].split('-')))
                        if time1 >= starttime and time1 <= endtime:
                            msg = msg + ';' + quiry
                        else:
                            msg = msg + ';' + ' '
                    condition1 = condition1 + ';' + condition
                    quiry1 = quiry1 + ';' + quiry
            else:
                msg = ' '
            print(msg+'======3')
            if quiry1 in msg:
                    print(caseid + ':'+condition1[1:]+'=>'+quiry1[1:]+'--------------sucesss', file=f)
            else:
                    print(caseid + ':'+condition1[1:]+'=>'+quiry1[1:]+'--------------fail', file=f)
        except:
            print(caseid + ':execute====================>error', file=f)


if __name__ == '__main__':
    test = Test_vehiclefailure()
    # test.test_vehiclefailure('test_vehiclefailure', '车辆编码：511502000288', '')
    # test.test_vehiclefailure('test_vehiclefailure', '上报时间：2020-07-10 00:00:00,2020-07-11 00:00:00', '')
    # test.test_vehiclefailure('test_vehiclefailure', '报障类型（员工）：坐垫', '')
    # test.test_vehiclefailure('test_vehiclefailure', '上报来源：员工', '')
    test.test_vehiclefailure('test_vehiclefailure', '上报时间：2020-07-10 00:00:00,2020-07-11 00:00:00，车辆编码：511502000288，报障类型（员工）：坐垫', '')
