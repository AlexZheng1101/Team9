from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

import time
course = []
hwCount = []
hwName = []
hwDue = []
options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--headless")

username = 'C108118129'
password = '5515'

def login(user,pwd):
    chrome.find_element_by_id("username").send_keys(user)
    password = chrome.find_element_by_id("password")
    password.send_keys(pwd)
    password.submit()

def switchfr():
    import time
    chrome.switch_to.frame('mooc_sysbar')
    time.sleep(3)
    chrome.find_element_by_id("SYS_06_01_004").click()
    chrome.switch_to.default_content()
    chrome.switch_to.frame('s_main')

chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://elearning.nkust.edu.tw/mooc/login.php")
login(username, password)
time.sleep(3)
switchfr()
soup = BeautifulSoup(chrome.page_source, 'html.parser')
titles = soup.find_all('div', {'class': "text-left"})
hwTMPCount = soup.find_all('div', {'class': "text-center"})
print(hwTMPCount)
cnt = 1
for count in hwTMPCount:
    if count.getText() != '應繳作業' and count.getText() != '未繳作業':
        if (cnt % 2) == 0 and count.getText() != '0':
            hwCount.append(count.getText())
        cnt += 1
        
print(hwCount)

for title in titles:
    if title.getText() != '課程編號' and title.getText() != '課程名稱':
        course.append(title.getText())
print(course)
for i in range(len(hwCount)):
    import time
    course_btn = chrome.find_elements_by_class_name("btn.btn-gray")
    hwName = []
    hwDue = []
    course_btn[i].click()
    time.sleep(3)
    chrome.switch_to.default_content()
    chrome.switch_to.frame('s_main')
    soup = BeautifulSoup(chrome.page_source, 'html.parser')
    hwtitle = soup.find_all('span', {'style': "width: 230px;"})
    for title in hwtitle:
        hwName.append(title.getText())
    print(hwName)
    hwtime = soup.find_all('div', {'class': "sub-text"})
    for time in hwtime:
        if time.getText() != '':
            hwDue.append(time.getText())
    print(hwDue)
    chrome.switch_to.default_content()
    chrome.switch_to.frame('s_sysbar')
    chrome.find_element_by_class_name("logo").click()
    chrome.find_element_by_xpath("/html/body/div[2]/div/table/tbody/tr/td[5]/a").click()
    chrome.find_element_by_xpath("/html/body/div[2]/div/table/tbody/tr/td[5]/input").click()
    login(username, password)
    switchfr()
chrome.quit()