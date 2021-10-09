'''
Date: 2021-09-12 19:35:16
LastEditors: Azus
LastEditTime: 2021-09-12 20:15:15
FilePath: /Py/getcookie.py
'''
from selenium import webdriver
import time
import json
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument(
    '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
)
driver = webdriver.Chrome(options=chrome_options)

#填写webdriver的保存目录
# driver = webdriver.Chrome()

#记得写完整的url 包括http和https
driver.get('https://www.huazhu.com')

#程序打开网页后20秒内手动登陆账户
time.sleep(1)

with open('cookies', 'w') as cookief:
    #将cookies保存为json格式
    cookief.write(json.dumps(driver.get_cookies()))

driver.close()