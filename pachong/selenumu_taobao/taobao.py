"""
time:2018年9月27日 22：34
author:lightfish
爬取地址淘宝，输入要爬取的商品和页数进行爬取
"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
import pymongo

browser = webdriver.Chrome()
#设置时间10秒
wait = WebDriverWait(browser, 10)

def index_page(page, KEY_WORD):
    '''
    爬取索引页
    :param page: 页码
    :return:
    '''
    print('正在爬取第',page,'页...')
    try:
        url = 'https://s.taobao.com/search?q='+quote(KEY_WORD)
        browser.get(url)
        if int(page) > 1:
            #指定presence_of_element_located这个条件，判断是否加载成功
            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        #使用另一个等待条件text_to_be_present_in_element,等待指定的文本出现在某个节点里即返回成功
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'),str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products(KEY_WORD)
    except TimeoutException:
        index_page(page, KEY_WORD)

def get_products(word):
    """
    提取商品数据
    :return:
    """
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        save_to_mongodb(product, word)

def save_to_mongodb(result, keyw):
    client = pymongo.MongoClient('localhost')
    db=client['mydb']
    taobao=db['taobao_'+keyw]
    try:
        if taobao.insert_one(result):
            print('存储到MongoDB成功!')
    except Exception:
        print('存储失败!')


if __name__=='__main__':
    KEY_WORD = input('请输入要爬取的商品:')
    page = input('输入要爬取淘宝页数：')
    for i in range(1,int(page)+1):
        index_page(i,KEY_WORD)