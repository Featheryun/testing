from selenium import webdriver
import json,time
from  selenium.webdriver import ChromeOptions
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
    # wd = webdriver.Chrome()
    # wd.get("https://passport.jd.com/new/login.aspx?ReturnUrl=http%3A%2F%2Fcart.jd.com%2Fgate.action%3Fpid%3D4047821%26pcount%3D1%26ptype%3D1&r=1606976032784")
    # wd.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]').click()
    # # wd.find_element_by_id('kw').send_keys('易烊千玺')

    # wd.find_element_by_id('loginsubmit').click()
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    wd = webdriver.Chrome(options=option)
    # cookie = {'__jdu':'757256939','shshshfpa':'67fdf4ce-32ca-50c4-e78f-04a1646a7bdc-1600408044','shshshfpb':'zH70VLuAAJBk5R4gdO%2FQwlw%3D%3D','user-key':'328befc9-3bd9-442c-9d9c-98263b781828','_c_id':'co1j87hlr9z3cpuscgj1606975845858gpuq','DeviceSeq':'36a3b096e709492f99accbdb66b02e3d','pinId':'U9axV7FAoXkiXtRzlG-kRbV9-x-f3wj7','pin':'jd_5e943efa0a390','unick':'jd_150958lii','_tp':'7RXC1m8NVG1XG6sPiiddV6IF4jp4AXWlM6RE7ivb8qg%3D','_pst':'jd_5e943efa0a390','ipLoc-djd':'22-1930-49324-0','areaId':'22','PCSYCityID':'CN_510000_510100_510116','mp':'15095859543','unpl':'V2_ZzNtbUMCEEIiXEFVfBtUAWJXEVtLX0UdIA8RXHMaWQVnVhRfclRCFnQURldnGVUUZwoZXkpcQxNFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZH0dWgZjBBpfSmdzEkU4dlJ6GFoAYzMTbUNnAUEpAUZcch9YSGEHFF5GUEsXfThHZHg%3d','__jdv':'76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_0dbffe6063954e278979d6f992411d73|1608287428794','cn':'4','_s_id':'smun7bwca3qsuqosipg1608538035177uggy','TrackID':'1i5d5utvRMn9DjCdRSsJNqCKy6AFsgUUBLhQcSse3qDM5RZsk9M7khPN_2kHqy74c5rPbttaYKYECS5DJb41sV1zVYj6iZyvEG1hxeWnqRZJjgYktlT-9veQ-sqBU0cF5','shshshfp':'6a1cab3b83b8bc94a9b272949f9e2739','shshshsID':'91e0cc47fd447e18c5afc9a3aae297d0_2_1608541417522','alc':'4JYepcHKWXjU+PaPR0cKxg==','_t':'gtLiGPMCmcZqD6SVpM2mr+VzzAvPMMegMbZEG2IxJRs=','smun7bwca3qsuqosipg1608538035177uggy':'-19292','__jda':'122270672.757256939.1598600573.1608538032.1608541410.16','__jdc':'122270672','3AB9D23F7A4B3C9B':'I5OC5ET33DMAOO7VSCJPDS6AEAECFWPGX2DWG4GADXHQXT4LTL4Y2ZNXZADVQXX7NDYEA2MUR2BIVR4MPQ5TSWQGPU','__jdb':'122270672.4.757256939|16.1608541410','wlfstk_smdl':'3l05i9maz81wyr4v2tgmv6wtagmehu3l'}
    cookies = '__jdu=757256939; shshshfpa=67fdf4ce-32ca-50c4-e78f-04a1646a7bdc-1600408044; shshshfpb=zH70VLuAAJBk5R4gdO%2FQwlw%3D%3D; user-key=328befc9-3bd9-442c-9d9c-98263b781828; pinId=U9axV7FAoXkiXtRzlG-kRbV9-x-f3wj7; pin=jd_5e943efa0a390; unick=jd_150958lii; _tp=7RXC1m8NVG1XG6sPiiddV6IF4jp4AXWlM6RE7ivb8qg%3D; _pst=jd_5e943efa0a390; ipLoc-djd=22-1930-49324-0; areaId=22; PCSYCityID=CN_510000_510100_510116; unpl=V2_ZzNtbUMCEEIiXEFVfBtUAWJXEVtLX0UdIA8RXHMaWQVnVhRfclRCFnQURldnGVUUZwoZXkpcQxNFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZH0dWgZjBBpfSmdzEkU4dlJ6GFoAYzMTbUNnAUEpAUZcch9YSGEHFF5GUEsXfThHZHg%3d; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_0dbffe6063954e278979d6f992411d73|1608287428794; cn=4; TrackID=1JWFz9nKmw5UC3B3xwpkUYYVz-ali4Pu-woiP0_UT0jPNZeqpYdYeOHn7IYlkCAkDbbdAPLKHssZcLB31ILHRoZISHWz5sDOJ0n7ElbKQ8CXR0fM-ZG_CqRUgdmHms8Y3; ceshi3.com=201; __jda=122270672.757256939.1598600573.1608541410.1608543985.17; __jdc=122270672; thor=F3620D7E25537683E864FB3C1C117CAEC6DDF084EBC5EF6930527B62A5BF3A111E68552F7C625ED4CBDA5EB0610E6084A75C2FAD23F257B377F1A8B93BB86AC15FB26B796CFBA83EA6ABBA297A20EF76402FA94A6169373889B672B43E170BCF8348F49CAB29BB1F4443190D8A620EFB081A7821C434418CDC017247CF539296BFE22D5DAAFED147BCF1D7613CA4442EB0D4915418F9668645751B4871051688; 3AB9D23F7A4B3C9B=I5OC5ET33DMAOO7VSCJPDS6AEAECFWPGX2DWG4GADXHQXT4LTL4Y2ZNXZADVQXX7NDYEA2MUR2BIVR4MPQ5TSWQGPU; shshshfp=6a1cab3b83b8bc94a9b272949f9e2739; shshshsID=d5b6bfb897b1383252d15c9fa4823960_1_1608543998586; __jdb=122270672.5.757256939|17.1608543985'
    cookie1 = {}
    for i in cookies.split(';'):
        name, value = i.strip().split('=', 1)
        cookie1[name] = value
    cookie = {}
    wd.get('https://www.jd.com/')
    for name, value in cookie1.items():
        cookie = {'domain': 'jd.com', 'name': name, 'value': value}
        wd.add_cookie(cookie)
    print(cookie)
    wd.get('https://item.jd.com/100012043978.html')
    while wd.find_element_by_id('btn-reservation').text == '抢购':
        wd.find_element_by_id('btn-reservation').click()
        print(1)
