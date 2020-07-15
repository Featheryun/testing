from selenium import webdriver
import time

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
        time.sleep(1)
        try:
            wd.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button[2]")
        except:
            flag = False
        if flag:
            wd.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button[2]").click()

        return wd

if __name__ == '__main__':
    Login  = Login()
    username = "15095859543"
    password = "12"
    wd = Login.login(username, password)
    time.sleep(0.1)
    print(wd.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/form/div[1]/div[3]/div/div[2]').text)
