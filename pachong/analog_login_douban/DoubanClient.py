"""
author:lightfish
Time:2018.11.13
note:豆瓣模拟登录和自动写短评
"""
import requests
from PIL import Image
from bs4 import BeautifulSoup
import getpass
from urllib import request


def index_page(html):
    soup = BeautifulSoup(html,'lxml')
    captcha_url = soup.find(attrs={'id':'captcha_image'}).attrs['src']
    captcha_id = soup.find(attrs={'name':'captcha-id'}).attrs['value']
    return captcha_url,captcha_id

class DoubanClient:
    def __init__(self):
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        self.session = requests.session()
        self.session.headers.update(headers)

    def send_message(self):
        post_data={
            'ck':'IG2-',
            'interest': 'wish',
            'foldcollect': 'F',
            'comment':'来自python的一条留言,just for me,嘻嘻',
            'tags':'悬疑 漫画改编 剧场版'
            #'bp_text':'Python +1',
            #'bp_submit':' 留言 '
        }
        res = self.session.post(url='https://movie.douban.com/j/subject/27110363/interest',data=post_data)
        print(res.url)
        #print(res.text)
        if res.status_code == 200:
            print('评论成功...')
        else:
            print('评论失败...')

    def login_douban(self,username,passwd,source='index_nav',redir='https://www.douban.com',login='登录'):
        url='https://accounts.douban.com/login'
        r = self.session.get(url)
        captcha_url,capcha_id = index_page(r.text)
        post_data={
            'source':source,
            'redir':redir,
            'form_email':username,
            'form_password':passwd,
            'login':login
        }
        if captcha_url:
            #with open('captcha.jpg','wb') as f:
            #   f.write()
            request.urlretrieve(captcha_url,'captcha.jpg')
            img = Image.open('captcha.jpg')
            img.show()

            captcha_solution = input('Please input captcha:')
            post_data['captcha-solution'] = captcha_solution
            post_data['captcha-id'] = capcha_id
        print(post_data)
        res = self.session.post(url,data=post_data)
        #print(self.session.get('https://www.douban.com/note/696076607/').text)
        print(res.url)
        if res.url == 'https://www.douban.com':
            print("登陆成功...")
        else:
            print('登录失败...')




if __name__=='__main__':
    username = input('Please input username:')
    password = input('Please input password:')
    douban = DoubanClient()
    douban.login_douban(username,password)
    douban.send_message()

