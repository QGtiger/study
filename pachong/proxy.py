import urllib.request
import random

url='http://httpbin.org/ip'
print('添加代理IP地址(IP:端口)，多个IP地址间用分号隔开')
iplist=input('请开始输入:').split(sep=';')
print(iplist)
while True:
    ip=random.choice(iplist)
    proxy_support=urllib.request.ProxyHandler({'http':ip})
    opener=urllib.request.build_opener(proxy_support)
   
    urllib.request.install_opener(opener)
    try:
        print('正在尝试使用%s访问...' % ip)
        rep=urllib.request.urlopen(url)
        print(rep.getcode())
    except:
        print('Error')
    else:
        print('Successful')
    if input('Is continbu?(Y/N)').upper()=='N':
        break


