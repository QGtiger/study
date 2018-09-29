"""
time:2018.9.29
author:lightfish
爬取网址：https://fh.dujia.qunar.com，爬取该网址的度假方案
"""
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
import pandas as pd
browser = webdriver.Chrome()
wait=WebDriverWait(browser, 10)
def get_page(start, end, page, dict):
    print('正在爬取第',page,'页...')
    try:
        if int(page)>1:
            next_btn=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#pager > div > a[data-pager-link="next"]')))
            next_btn.click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.list .item')))
        get_info(dict)
    except TimeoutException:
        browser.refresh()
        reget=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#j_submit')))
        reget.click()
        get_page(start, end, page, dict)

def get_info(dict):
    html=browser.page_source
    doc=pq(html)
    items=doc('.list .item').items()
    for item in items:
        dict['方案'].append(item.find('h4').text())
        dict['评价'].append(item.find('.point').text()[:3])
        dict['价格'].append(item.find('.pack').text())
        dict['住处'].append(item.find('.h_title').text())
        dict['去程'].append(item.find('div:nth-child(2) > div.c1').text().replace('"',''))
        dict['去程时间'].append((item.find('div:nth-child(2) > div.c2').text()))
        dict['来程'].append(item.find('div:nth-child(3) > div.c1').text())
        dict['来程时间'].append(item.find('div:nth-child(3) > div.c1').text())




if __name__=='__main__':
    url='https://fh.dujia.qunar.com'
    start = input('请输入您的出发点:')
    end = input('请输入您的目的地:')
    page= input('请输入您要爬取的页码:')
    browser.get(url)
    input1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#depCity')))
    input2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#arrCity')))
    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                    'body > div.reset-wrap > div.qn_warp > div.b_ct.qn_page.cf > div.b_search > div > div.cr4_group.cf > div')))
    input1.clear()
    input1.send_keys(start)
    input2.clear()
    input2.send_keys(end)
    submit.click()
    dict={'方案':[],
          '评价':[],
          '价格':[],
          '住处':[],
          '去程':[],
          '去程时间':[],
          '来程':[],
          '来程时间':[]}
    for i in range(1,int(page)+1):
        get_page(start, end, i, dict)

    df = pd.DataFrame(dict)
    table = pd.DataFrame(df)
    # 需要安装openpyxl
    table.to_excel("度假.xlsx")



