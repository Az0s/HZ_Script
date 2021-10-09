from selenium import webdriver
import json
import time
from selenium.webdriver.chrome.options import Options
from sys import stdout

driver = webdriver.Chrome(executable_path='/opt/homebrew/bin/chromedriver')
driver.get(
    'https://study.enaea.edu.cn/circleIndexRedirect.do?action=toNewMyClass&type=course&circleId=113342&syllabusId=693849&isRequired=true&studentProgress=9')
print("Waiting manually login")
# time.sleep(10)
try:
    input("Keypress to continue")
except:
    pass
print("Start:")
anchor = time.time()
# time.sleep(1)
# s = time.strftime('%M')
# print(anchor)

# print('{:.2}'.format(s-anchor))
wlkStk = -1
while True:
    try:
        driver.find_elements_by_css_selector('#rest_tip > table > tbody > tr:nth-child(2) > td.td-content > div.dialog-button-container > button').click()
        print("Element found")
    except:
        time.sleep(1)
    try:
        driver.find_elements_by_xpath('//*[@id="rest_tip"]/table/tbody/tr[2]/td[2]/div[3]/button').click()
        print("Element found")
    except:
        time.sleep(1)
    s = time.time()
    diff = (int)((s- anchor)/60)
    # print(wlkStk != diff)
    if((diff % 5 == 0) & (wlkStk != diff)):
        print(diff, end='')
        wlkStk = diff
    print('*',end="")
    stdout.flush()
    time.sleep(10)

