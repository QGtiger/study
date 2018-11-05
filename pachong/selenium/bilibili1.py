from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from PIL import ImageGrab,Image

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)

browser.get('https://passport.bilibili.com/login')
html = browser.page_source
btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.gt_slider_knob')))
action = ActionChains(browser)
action.move_to_element(btn).perform()
captcha = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#login-username')))
location,size = captcha.location,captcha.size
print(captcha.location,captcha.size)
#print(location['x'])
img = ImageGrab.grab(bbox=(1,1,111,111))

img.show()
print(captcha.location,captcha.size)
