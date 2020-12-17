from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

# 登录
class Login:

    def login(self, username, password):

        wd = webdriver.Chrome()
        wd.maximize_window()
        wd.get("http://boss.nm666.cn/#/user/login")
        wd.find_element_by_id("userName").send_keys(username)
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_css_selector("#root > div > div.antd-pro-layouts-user-layout-content > div.antd-pro-pages-user-login-style-main > div.antd-pro-pages-user-login-components-login-index-login > form > div.ant-row.ant-form-item > div > div > span > button").click()
        flag = True
        wd.implicitly_wait(5)
        try:
            wd.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button[2]")
        except:
            flag = False
        if flag:
            wd.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button[2]").click()

        return wd


# def baidu():
#     wd = webdriver.Chrome()
#     wd.get("https://www.baidu.com")
#     time.sleep(1)
#     wd.find_element_by_id('kw').send_keys('1')
#     time.sleep(1)
#     ActionChains(wd).move_by_offset(500, 200).click().perform()
#     wd.find_element_by_id('su').click()
#     time.sleep(3)


if __name__ == '__main__':
    # Login  = Login()
    # username = "15095859543"
    # password = "123456"
    # wd = Login.login(username, password)
    # time.sleep(0.1)
    # print(wd.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/form/div[1]/div[3]/div/div[2]').text)
    wd = webdriver.Chrome()
    wd.get("https://passport.jd.com/new/login.aspx?ReturnUrl=http%3A%2F%2Fcart.jd.com%2Fgate.action%3Fpid%3D4047821%26pcount%3D1%26ptype%3D1&r=1606976032784")
    wd.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]').click()
    wd.find_element_by_id('loginname').send_keys('13688164282')
    # time.sleep(1)
    # wd.find_element_by_id('kw').send_keys('易烊千玺')
    # time.sleep(1)
    wd.find_element_by_id('loginsubmit').click()