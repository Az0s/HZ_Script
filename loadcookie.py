'''
Date: 2021-09-12 19:35:24
LastEditors: Azus
LastEditTime: 2021-09-14 08:13:45
FilePath: /Huazhu/loadcookie.py
'''
from selenium import webdriver
import json
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument(
    '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
)
driver = webdriver.Chrome(executable_path='/opt/homebrew/bin/chromedriver', options=chrome_options)
# driver.get('https://www.google.com')

#填写webdriver的保存目录
# driver = webdriver.Chrome()

#记得写完整的url 包括http和https
# driver.get('https://www.huazhu.com')
driver.get('https://campaign.huazhu.com')
# driver.get
# driver.find_element_by_xpath('/html/body/div[2]/div[1]/section[1]/div/div[3]').click()
# # driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/span/a[1]').click()
# # 延时2秒，以便网页加载所有元素，避免之后找不到对应的元素
# time.sleep(2)

#首先清除由于浏览器打开已有的cookies
driver.delete_all_cookies()

with open('cookies', 'r') as cookief:
    #使用json读取cookies 注意读取的是文件 所以用load而不是loads
    cookieslist = json.load(cookief)
    # # 方法1 将expiry类型变为int
    # for cookie in cookieslist:
    #     #并不是所有cookie都含有expiry 所以要用dict的get方法来获取
    #     if isinstance(cookie.get('expiry'), float):
    #         cookie['expiry'] = int(cookie['expiry'])
    #     driver.add_cookie(cookie)

#方法2删除该字段
for cookie in cookieslist:
    #该字段有问题所以删除就可以  浏览器打开后记得刷新页面 有的网页注入cookie后仍需要刷新一下
    if 'expiry' in cookie:
        del cookie['expiry']
    driver.add_cookie(cookie)

# driver.refresh()
driver.get('https://campaign.huazhu.com/pointsShop/index.html#/')
time.sleep(1)

# 根据路径找到按钮,并模拟进行点击
# /html/body/div[2]/div[1]/section[1]/div/div[3]

# # 格式是PEP8自动转的
# # 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
# driver.find_element_by_xpath("//*[@id='aw-login-user-name']").send_keys("账号")
# driver.find_element_by_xpath("//*[@id='aw-login-user-password']").send_keys(
#     "密码")
# # 在输入用户名和密码之后,点击登陆按钮
# driver.find_element_by_xpath("//*[@id='login_submit']").click()
# time.sleep(2)

# 点击登陆后的页面中的签到,跳转到签到页面
# driver.find_element_by_xpath("//*[@id="root"]/div/div[1]/div/div[1]/div[2]/div[1]/a[1]/div").click()
time.sleep(3)
# driver.find_element_by_css_selector("#root > div > div.page.page-home.split > div > div.content > div.navigation.block > div.menu > a:nth-child(1) > div")
driver.get('https://campaign.huazhu.com/pointsShop/index.html#/signIn')
time.sleep(2)

# 点击签到,实现功能
# driver.find_element_by_xpath("//*[@id='qd_button']").click()
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div[2]/div/div[2]').click()
# driver.find_element_by_
time.sleep(2)
driver.close()

