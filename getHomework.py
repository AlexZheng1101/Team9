from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

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


def gethw(user,passwd):
    import time
    hwCount = []
    hwName = []
    hwDue = []
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--headless")
    global chrome
    chrome = webdriver.Chrome('/home/peng/Team9/chromedriver', chrome_options=options)
    chrome.get("https://elearning.nkust.edu.tw/mooc/login.php")
    login(user, passwd)
    time.sleep(2)
    switchfr()
    soup = BeautifulSoup(chrome.page_source, 'html.parser')
    titles = soup.find_all('div', {'class': "text-left"})
    hwTMPCount = soup.find_all('div', {'class': "text-center"})
    #print(hwTMPCount)
    cnt = 1
    for count in hwTMPCount:
        if count.getText() != '應繳作業' and count.getText() != '未繳作業':
            if (cnt % 2) == 0 and count.getText() != '0':
                hwCount.append(count.getText())
            cnt += 1
            
    for i in range(len(hwCount)):
        hwCount[i] = int(hwCount[i])
    #print(hwCount)
    '''
    for title in titles:
        if title.getText() != '課程編號' and title.getText() != '課程名稱':
            course.append(title.getText())
    print(course)
    '''
    for i in range(len(hwCount)):
        import time
        course_btn = chrome.find_elements_by_class_name("btn.btn-gray")
        
        course_btn[i].click()
        time.sleep(2)
        chrome.switch_to.default_content()
        chrome.switch_to.frame('s_main')
        soup = BeautifulSoup(chrome.page_source, 'html.parser')
        hwtitle = soup.find_all('span', {'style': "width: 230px;"})
        tmp = 0
        for title in hwtitle:
            if tmp < hwCount[i]:
                hwName.append(title.getText())
                tmp += 1
                
        hwtime = soup.find_all('div', {'class': "sub-text"})
        tmp = 0
        for time in hwtime:
            if time.getText() != '':
                if tmp < hwCount[i]:
                    hwDue.append(time.getText())
                    tmp += 1

        chrome.quit()
        chrome = webdriver.Chrome('/home/peng/Team9/chromedriver', chrome_options=options)
        chrome.get("https://elearning.nkust.edu.tw/mooc/login.php")
        login(user, passwd)
        import time
        time.sleep(2)
        switchfr()
    return hwName,hwDue