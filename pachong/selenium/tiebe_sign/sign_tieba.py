"""
author:lightfish
Time:2018.10.22
note:实现对贴吧的签到
"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
import re
import weixin
from selenium.webdriver.chrome.options import Options

#无头浏览器的设置（无界面）
chrome_options = Options()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(browser,10)

#由于贴吧会检测是否不是人工操作，会进行检测，所以我用time模块的sleep函数来躲过检测
def login():
    browser.get('https://tieba.baidu.com/')
    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#com_userbar > ul > li.u_login > div > a')))
    login_btn.click()
    login_btn1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#TANGRAM__PSP_10__footerULoginBtn')))
    login_btn1.click()
    user = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#TANGRAM__PSP_10__userName')))
    user.send_keys('15990184749')
    time.sleep(3)
    passwd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#TANGRAM__PSP_10__password')))
    passwd.send_keys('qwer123qg')
    time.sleep(4)
    submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#TANGRAM__PSP_10__submit')))
    submit.click()
    sign()

#检测是否签到成功，并向微信好友发送消息
def sign():
    #btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#likeforumwraper > a:nth-child(1)')))
    #btn.click()
    #browser.switch_to_window(browser.window_handles(1))
    #sign_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#signstar_wrapper > a')))
    #sign_btn.click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#likeforumwraper > a')))
    html = browser.page_source
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all(attrs={'class': 'u-f-item'})
    for n,item in enumerate(items):
        print(item.attrs['class'])
        if 'sign' in item.attrs['class']:
            print(item.get_text()+'贴吧已签到')
            weixin.send_msg(item.get_text()+'贴吧已签到')
        else:
            print(item.get_text() + '贴吧未签到，正在跳转签到...')
            weixin.send_msg(item.get_text() + '贴吧未签到，请前往签到...')
            #sign_in(n)

#由于贴吧的关系，个人认为鼠标得放到签到上面才行，但是我模拟了鼠标移动到签到元素上，
#但是依然不能完成签到，等待后期跟进啦
def sign_in(n):
    actions = ActionChains(browser)
    btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#likeforumwraper > a:nth-child(%s)' % str(n+1))))
    btn.click()
    browser.switch_to_window(browser.window_handles[1])
    sign_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#signstar_wrapper > a')))
    actions.move_to_element(sign_btn).perform()
    time.sleep(2)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.find(attrs={'id':'signstar_wrapper'}).attrs['class'])

    sign_btn.click()






if __name__=='__main__':
    #browser.get(
    #    'http://tieba.baidu.com/home/main?id=91dce594afe585813636466e?t=1529379231&fr=userbar&red_tag=i2029902479')
    login()

    """
    browser.get('https://www.baidu.com')

    ActionChains(browser).move_to_element(browser.find_element_by_link_text("设置")).perform()
    time.sleep(2)
    browser.find_element_by_link_text("高级搜索").click()"""

