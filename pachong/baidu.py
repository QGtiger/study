#百度翻译API的使用

import hashlib
import urllib.request,urllib.parse
import json
import random

def helpl(x):
    for e in x:
        print('\t',e)

class BaiduFanyi:
    appid='20180802000191233'
    secretKey='UpF7CdysLTTo_0X40cz4'
    myurl='http://api.fanyi.baidu.com/api/trans/vip/translate'
    fromLang='auto'
    salt=random.randint(32768,65536)
    
    
    def __init__(self,toLang='zh'):
        self.toLang=toLang
    def translate(self,q):
        self.sign=self.appid+str(q)+str(self.salt)+self.secretKey
        m1=hashlib.md5()
        m1.update(self.sign.encode('utf-8'))
        self.sign=m1.hexdigest()
        self.myurl=self.myurl+'?appid='+self.appid+'&q='+urllib.parse.quote(q)+'&from='+self.fromLang+'&to='+self.toLang+'&salt='+str(self.salt)+'&sign='+self.sign
        res=urllib.request.urlopen(self.myurl).read().decode('utf-8')
        rep=json.loads(res)
        #print(rep)
        return rep['trans_result'][0]['dst']

if __name__=='__main__':
    Langs={'中文':'zh','英语':'en','粤语':'yue','文言文':'wyw','日语':'jp','韩语':'kor','法语':'fra','西班牙语':'spa','泰语':'th','阿拉伯语':'ara','俄语':'ru','德语':'de','繁体中文':'cht','捷克语':'cs','瑞典语':'swe','芬兰语':'fin','波兰语':'pl','意大利语':'it','葡萄牙语':'pt','丹麦语':'dan'}
    print('百度翻译QAQ：')
    while True:
        lang=input('\t翻译至什么语言(默认中文):')
        if lang=='help':
            helpl(Langs)
        elif lang.strip()=='':
            text=input('\t请输入您要翻译的内容:')
            f=BaiduFanyi()
            print('\t百度翻译:',f.translate(text),end='\n\n')
        elif Langs.get(lang,None):
            text=input('\t请输入您要翻译的内容:')
            f=BaiduFanyi(Langs.get(lang))
            print('\t百度翻译:',f.translate(text),end='\n\n')
        else:
            print('\t输入错误!示范输入(中文)\n\n')
