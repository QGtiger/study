"""
author:lightfish
Time:2018.10.27
note:G2加油,失败，由于虎牙好像会检测你是否是键盘输入，所以失败，但是python调用js代码可以学学
browser.execute_script()调用js方法
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
wait=WebDriverWait(browser,10)

browser.get('https://www.baidu.com')
actions = ActionChains(browser)
actions.move_to_element(browser.find_element_by_link_text("设置")).perform()
"""
虎牙的登录
login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_duyaHeaderRight > div > div.hy-nav-right.un-login > a:nth-child(1)')))
login_btn.click()
btn_img = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.UDBSdkLgn > div.UDBSdkLgn-box > div.UDBSdkLgn-inner.qrCode.login > div.UDBSdkLgn-switch.UDBSdkLgn-webQuick > img')))
btn_img.click()
user = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.E_acct')))
passwd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.E_passwd')))
user.send_keys('15990184749')
passwd.send_keys('qwer123qg')
submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.UDBSdkLgn > div.UDBSdkLgn-box > div.UDBSdkLgn-inner.account.login > div.UDBSdkLgn-body > div.UDBSdkLgn-main > div.UDBSdkLgn-login.J_UDBSdkLgnPane > div:nth-child(1) > div.UDBSdkLgn-modal > div.UDBSdkLgn-mt20.clearfix > a')))
submit_btn.click()
"""
"""
player_video = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.player-video')))
actions = ActionChains(browser)
actions.move_to_element(player_video).perform()
stop_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.player-pause-btn')))
stop_btn.click()
"""



def G2_fighting(msg):
    time.sleep(4)
    js = 'document.getElementById("pub_msg_input").innerHTML="%s"' % msg
    browser.execute_script(js)
    js1 = '$("#btn_sendMsg").click()'
    browser.execute_script(js1)



if __name__=='__main__':
    #G2_fighting('G2 ...')
    print('find_element_by_link_text()函数测试...')