import time
from commom.login import Login
from commom.zone_change import Zone_change
from util.excel_read import excel_read

# 终端查询车辆
class Terminal_inqury:
    def terminal_inqury(self, data, wd):
        f = open('D:/testing/testfile/terminal_inqury_result.txt', 'a')
        if wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/main/div/div/div[1]/div/div/div[1]').text not in '首页/IOT管理/车辆':
            wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/aside/div/ul/li[2]/div[1]').click()
            time.sleep(1)
            wd.find_element_by_xpath('//*[@id="/iot$Menu"]/li[8]/a').click()
            time.sleep(0.5)
        wd.find_element_by_css_selector("#terminalId").clear()
        wd.find_element_by_css_selector("#terminalId").send_keys(data)
        time.sleep(0.5)
        flag = True
        wd.find_element_by_css_selector("#root > div > div > div > section > section > main > div > div > div.ant-pro-grid-content > div > div > div > div > div > div > div.antd-pro-pages-iot-bike-list-style-tableListForm > form > div > div:nth-child(4) > span > button.ant-btn.ant-btn-primary").click()
        time.sleep(0.5)
        try:
            msg = wd.find_element_by_css_selector("#root > div > div > div > section > section > main > div > div > div.ant-pro-grid-content > div > div > div > div > div > div > div.antd-pro-components-standard-table-index-standardTable > div > div > div > div > div > div > table > tbody > tr > td:nth-child(2)").text
            print(msg)
            flag = True
        except:
            flag = False
        if flag:
            print(str(data)+'=============111', file=f)
        else:
            print(str(data)+'=============222', file=f)
        f.close()
        return wd


if __name__ == '__main__':
    ter = Terminal_inqury()
    login = Login()
    zone_change = Zone_change()
    wd = login.login('15095859543', '123456')  # 登录
    wd = zone_change.zone_change('翠屏区', wd)     # 切换翠屏区
    file_path = 'C:\\Users\\Administrator\\Desktop\\中控号.xlsx'
    datas = excel_read(file_path)   # 读取终端号
    # 循环遍历每个终端号查询
    for data in datas:
        print(int(data[0]))     # 转为int类型
        wd = ter.terminal_inqury(int(data[0]), wd)  # 查询并把结果写入result.txt