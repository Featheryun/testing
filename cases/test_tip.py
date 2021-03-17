import datetime

from selenium.webdriver.common.keys import Keys
import time
from commom.login import Login
from commom.zone_change import Zone_change
from util.str_to_dict import str_to_dict


class Test_tip:
    def test_tip(self, data):
        data = str_to_dict(data)
        f = open('D:/testing/testfile/test_tip_result.txt', 'a')
        login = Login()
        wd = login.login('15095859543', '123456')
        zone = Zone_change()
        wd = zone.zone_change('翠屏区', wd)
        time.sleep(1)
        if wd.find_element_by_xpath('//*[@class="ant-breadcrumb"][1]').text not in '首页/举报管理/举报明细':
            # wd.find_element_by_css_selector('#root > div > div > div > section > aside > div > ul > li:nth-child(5) > div.ant-menu-submenu-title').click()
            wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/aside/div/ul/li[5]/div').click()
            time.sleep(1)
            wd.find_element_by_xpath('//*[@id="/report$Menu"]/li').click()
            wd.implicitly_wait(5)
        msg = ''
        query1 = ''
        condition1 = ''
        wd.find_element_by_link_text('展开').click()
        wd.implicitly_wait(5)
        for key in data.keys():
            condition = key
            query = data[key]
            if condition == '车辆编码':
                wd.find_element_by_id('deviceSn').send_keys(query)
            elif condition == '发生时间':
                wd.find_element_by_id('createAt').click()
                wd.implicitly_wait(2)
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
            elif condition == '举报类型（运维）':
                wd.find_element_by_id('staffFlag').click()
                if query == '停放标准-马路上-马路中间':
                    wd.switch_to.active_element.send_keys(Keys.DOWN)
                elif query == '停放标准-马路上-绿化区域':
                    wd.switch_to.active_element.send_keys(2*Keys.DOWN)
                elif query == '停放标准-马路上-道路施工区域':
                    wd.switch_to.active_element.send_keys(3*Keys.DOWN)
                elif query == '停放标准-马路上-斑马线上':
                    wd.switch_to.active_element.send_keys(4*Keys.DOWN)
                elif query == '停放标准-马路上-汽车停车位':
                    wd.switch_to.active_element.send_keys(5*Keys.DOWN)
                elif query == '停放标准-马路上-停车场出入口':
                    wd.switch_to.active_element.send_keys(6*Keys.DOWN)
                elif query == '停放标准-马路上-大型车辆旁':
                    wd.switch_to.active_element.send_keys(7*Keys.DOWN)
                elif query == '停放标准-马路上-盲道上':
                    wd.switch_to.active_element.send_keys(8*Keys.DOWN)
                elif query == '停放标准-封闭区域内-楼道口内':
                    wd.switch_to.active_element.send_keys(9*Keys.DOWN)
                elif query == '停放标准-封闭区域内-道路中间':
                    wd.switch_to.active_element.send_keys(10*Keys.DOWN)
                elif query == '停放标准-封闭区域内-人员聚集区域':
                    wd.switch_to.active_element.send_keys(11*Keys.DOWN)
                elif query == '停放标准-封闭区域内-停车场出入口':
                    wd.switch_to.active_element.send_keys(12*Keys.DOWN)
                elif query == '停放标准-封闭区域内-绿化区域':
                    wd.switch_to.active_element.send_keys(13*Keys.DOWN)
                elif query == '停放标准-封闭区域内-出入口通道':
                    wd.switch_to.active_element.send_keys(14*Keys.DOWN)
                elif query == '停放标准-封闭区域内-建筑工地':
                    wd.switch_to.active_element.send_keys(15*Keys.DOWN)
                elif query == '骑行标准-违规骑行-多人骑行':
                    wd.switch_to.active_element.send_keys(16*Keys.DOWN)
                elif query == '骑行标准-违规骑行-未成年骑行':
                    wd.switch_to.active_element.send_keys(17*Keys.DOWN)
                elif query == '骑行标准-违规骑行-肇事逃逸':
                    wd.switch_to.active_element.send_keys(18*Keys.DOWN)
                elif query == '骑行标准-违规用车-私藏车辆':
                    wd.switch_to.active_element.send_keys(19*Keys.DOWN)
                elif query == '骑行标准-违规用车-上私锁':
                    wd.switch_to.active_element.send_keys(20*Keys.DOWN)
                wd.switch_to.active_element.send_keys(Keys.ENTER)
            elif condition == '举报类型（用户）':
                # wd.find_element_by_xpath('//*[@id="userFlag"]/div')
                wd.find_element_by_id('userFlag').click()
                if query == '上私锁':
                    wd.switch_to.active_element.send_keys(Keys.DOWN)
                elif query == '私藏车辆':
                    wd.switch_to.active_element.send_keys(2*Keys.DOWN)
                elif query == '二维码损坏':
                    wd.switch_to.active_element.send_keys(3*Keys.DOWN)
                elif query == '车身有广告':
                    wd.switch_to.active_element.send_keys(4*Keys.DOWN)
                elif query == '一车载多人':
                    wd.switch_to.active_element.send_keys(5*Keys.DOWN)
                elif query == '未成年人骑行':
                    wd.switch_to.active_element.send_keys(6*Keys.DOWN)
                elif query == '恶意毁坏车辆':
                    wd.switch_to.active_element.send_keys(7*Keys.DOWN)
                elif query == '肇事逃逸':
                    wd.switch_to.active_element.send_keys(8*Keys.DOWN)
                elif query == '其他':
                    wd.switch_to.active_element.send_keys(9*Keys.DOWN)
                wd.switch_to.active_element.send_keys(Keys.ENTER)
            elif condition == '举报来源':
                wd.find_element_by_id('reporterType').click()
                if query == '用户':
                    wd.switch_to.active_element.send_keys(Keys.DOWN)
                wd.switch_to.active_element.send_keys(Keys.ENTER)
            elif condition == '核实状态':
                wd.find_element_by_id('verifyStatus').click()
                if query == '核实有效':
                    wd.switch_to.active_element.send_keys(Keys.DOWN)
                elif query == '核实无效':
                    wd.switch_to.active_element.send_keys(2*Keys.DOWN)
                wd.switch_to.active_element.send_keys(Keys.ENTER)
            elif condition == '处罚结果':
                wd.find_element_by_id('processingStatus').click()
                if query == '罚金':
                    wd.switch_to.active_element.send_keys(Keys.DOWN)
                elif query == '黑名单':
                    wd.switch_to.active_element.send_keys(2*Keys.DOWN)
                elif query == '不处罚':
                    wd.switch_to.active_element.send_keys(3*Keys.DOWN)
                wd.switch_to.active_element.send_keys(Keys.ENTER)
        wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div[1]/div/div/div/div/div[1]/form/div[3]/div/button[1]').click()
        time.sleep(1)
        try:
            wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]')
            Flag = True
        except:
            Flag = False
        if Flag:
            for key in data.keys():
                condition = key
                query = data[key]
                if condition == '车辆编码':
                    msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]').text
                elif condition == '发生时间':
                    time1 = wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[9]').text
                    time1 = datetime.date(*map(int, time1.split(' ')[0].split('-')))
                    starttime = datetime.date(*map(int, query.split(',')[0].split(' ')[0].split('-')))
                    endtime = datetime.date(*map(int, query.split(',')[1].split(' ')[0].split('-')))
                    if time1 >= starttime and time1 <= endtime:
                        msg = msg + ';' +query
                    else:
                        msg = msg + ';' + ' '
                elif condition == '举报类型（运维）':
                    msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[6]').text
                elif condition == '举报类型（用户）':
                    msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[6]').text
                elif condition == '举报来源':
                    msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[5]').text
                elif condition == '核实状态':
                    msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[7]/span/span[2]').text
                elif condition == '处罚结果':
                    msg = msg + ';' + wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[8]/span').text
                condition1 = condition1 + ';' +condition
                query1 = query1 + ';' + query
        else:
            msg = ''
        print(msg)
        if query1 in msg:
            print('test_tip:' + condition1[1:] + ' ==> ' +query1[1:] + ' ========================>sucess', file=f)
        else:
            print('test_tip:' + condition1[1:] + ' ==> ' +query1[1:] + ' ========================>fail', file=f)
        wd.quit()
        f.close()

if __name__ == '__main__':
    test = Test_tip()
    test.test_tip('车辆编码：511502000361，举报来源：用户，发生时间：2020-06-10 00:00:00,2020-07-11 00:00:00')
    # test.test_tip('举报类型（运维）：停放标准-封闭区域内-出入口通道')
    # test.test_tip('处罚结果：不处罚')
    # test.test_tip('核实状态：待处理')
    # test.test_tip('举报类型（用户）：恶意毁坏车辆，处罚结果：不处罚，核实状态：核实')