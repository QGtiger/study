#百度翻译API的使用

import hashlib
import urllib.request,urllib.parse
import json
import random
from tkinter import *

def helpl():
    help=Tk()
    help.title('help')
    help.geometry('400x160')
    L='提供的语言翻译有:'
    count=0
    for x in Langs:
        count+=1
        if count%4:
            L+=x+' '
            continue
        L+=x+'\n'
    Label(help,text=L,font=('DFKai-SB',15)).pack()
    mainloop()

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

def lang():
    
        if Langs.get(e2.get(),None):
            return True
        else:
            error=Tk()
            error.title('错误')
            error.geometry('200x100')
            Label(error,text='输入错误！\n如果不知道请点击\'help\'',justify=LEFT,pady=30).pack()
            mainloop()
            e2.delete(0,END)
            return False

def translate():
    if Langs.get(e2.get(),None):
        f=BaiduFanyi(Langs.get(e2.get()))
        v3.set(f.translate(e1.get()))
    else:
        error=Tk()
        error.title('错误')
        error.geometry('200x100')
        Label(error,text='输入错误！\n如果不知道请点击\'help\'',justify=LEFT).pack()
        mainloop()
        e2.delete(0,END)
        
    


if __name__=='__main__':
    Langs={'中文':'zh','英语':'en','粤语':'yue','文言文':'wyw','日语':'jp','韩语':'kor','法语':'fra','西班牙语':'spa','泰语':'th','阿拉伯语':'ara','俄语':'ru','德语':'de','繁体中文':'cht','捷克语':'cs','瑞典语':'swe','芬兰语':'fin','波兰语':'pl','意大利语':'it','葡萄牙语':'pt','丹麦语':'dan'}
    root=Tk()
    root.title('百度翻译')
    root.geometry('600x200')
    group=LabelFrame(root,text='百度翻译',padx=10,pady=10)
    group.pack(padx=10,pady=10)
    Label(group,text='翻译文本:').grid(row=0)
    Label(group,text='翻译至:').grid(row=1)
    Label(group,text='百度翻译:').grid(row=2)
    v1,v2,v3=StringVar(),StringVar(),StringVar()
    e1=Entry(group,textvariable=v1,width=40)
    e2=Entry(group,textvariable=v2,width=40,validate='focusout',validatecommand=lang)
    e3=Entry(group,textvariable=v3,width=40)
    e1.grid(row=0,column=1,padx=10,pady=5)
    e2.grid(row=1,column=1,padx=10,pady=5)
    e3.grid(row=2,column=1,padx=10,pady=5)

    Button(group,text='translate',width=10,command=translate).grid(row=3,column=0,sticky=W,padx=10,pady=5)
    Button(group,text='help',width=10,command=helpl).grid(row=3,column=1,sticky=N,padx=10,pady=5)
    Button(group,text='quit',width=10,command=root.destroy).grid(row=3,column=2,sticky=E,padx=10,pady=5)
    mainloop()
    '''
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
    '''
