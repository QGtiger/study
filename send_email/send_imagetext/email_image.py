"""
author:lightfish
Time:2018.10.28
note:smtp发送邮件附带图片python MIMEImage
"""
# coding: utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import parseaddr,formataddr
from email.header import Header
import os

img_file=r'E:\PythonPic\yuner'
allfile=[]

def getallfile(path):
    allfilelist = os.listdir(path)
    for file in allfilelist:
        filepath = os.path.join(path,file)
        if os.path.isdir(filepath):
            getallfile(filepath)
        else:
            allfile.append(filepath)
    return allfile

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

def sendmail(filelist):
    From='qg12148@163.com'
    passwd = 'qwer123QG'
    To = '1426286337@qq.com'
    smtpserver = 'smtp.163.com'

    #创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = _format_addr('Python学习者<%s>' % From)
    msg['To'] = _format_addr('管理者<%s>' % To)
    msg['Subject'] = Header('send with some image...','utf-8').encode()
    content = '<b>Some <i>HTML</i> text</b> and some image.<br>'
    for index in range(len(filelist)):
        if index%2 != 0 :
            content+='<img src="cid:'+str(index)+'">'
        else:
            content+='<img src="cid:'+str(index)+'"><br>'

    msgHTML = MIMEText(content,'html','utf-8')
    msg.attach(msgHTML)

    """
    将图片和id位置对应起来
    """

    for index,file in enumerate(filelist):
        fp = open(file,'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID','<'+str(index)+'>')
        msg.attach(msgImage)
    server = smtplib.SMTP(smtpserver,25)
    server.set_debuglevel(1)
    server.login(From,passwd)
    server.sendmail(From,To,msg.as_string())
    server.quit()

if __name__=='__main__':
    sendmail(getallfile(img_file))
