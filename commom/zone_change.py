from commom.login import Login
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


# 切换区域
class Zone_change:
    def zone_change(self, zone, wd):
        wd.implicitly_wait(5)
        wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/header/div/div/div[2]/div/div').click()
        # WebDriverWait(wd, 10).until(lambda driver: wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/header/div/div/div[2]/div/div'))
        wd.find_element_by_xpath('//*[@id="root"]/div/div/div/section/section/header/div/div/div[2]/div/div/div/div/div[3]/div/input').send_keys(zone)
        ActionChains(wd).move_by_offset(500, 200).click().perform()     # 点击空白处
        wd.implicitly_wait(5)
        return wd



if __name__ == '__main__':
    zone_change = Zone_change()
    login = Login()
    wd = login.login('15095859543', '123456')
    wd = zone_change.zone_change('翠屏区', wd)