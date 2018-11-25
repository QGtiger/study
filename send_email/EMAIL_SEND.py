"""
author:lightfish
Time:2018.11.25
note:邮件的发送
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from email.utils import parseaddr,formataddr
from email.mime.multipart import MIMEMultipart
import re
import os

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

def _email_image_path(i):
    while True:
        image_path = input('请输入第{}张图片的路径:'.format(i))
        if os.path.exists(image_path):
            break
        else:
            print('请输入正确的图片路径')
    return image_path

if __name__=='__main__':
    while True:
        From_addr = input('请输入你的账号: ')
        sm = re.findall('.*?@(.*?)\.', From_addr)
        if sm:
            smtp_server = 'smtp.{}.com'.format(sm[0])
            break
        else:
            print('请输入正确的账号...')
    From_passwd = input('请输入你的授权密码: ')
    To_addr = input('请输入你要发送的账号: ')
    subject = input('请输入主题: ')
    _send_format = input('邮件支持html和plain,是否使用html格式(y/n): ')
    if _send_format.upper()=='Y':
        send_format = 'html'
    else:
        send_format = 'plain'

    msg = MIMEMultipart()
    msg['From'] = _format_addr('Python爱好者 <%s>' % From_addr)
    msg['To'] = _format_addr('管理员 <%s>' % To_addr)
    msg['Subject'] = Header(subject,'utf-8').encode()
    content = input('请输入内容: ')


    _is_Image = input('是否发送图片: ')
    if _is_Image.upper() == 'Y':
        image_num = input('请输入要发送几张图片: ')
        for i in range(int(image_num)):
            image_path = _email_image_path(i+1)
            content += '<br><img src="cid:'+str(i)+'"><br>'
            with open(image_path,'rb') as f:
                msgImage = MIMEImage(f.read())
            msgImage.add_header('Content-ID','<'+str(i)+'>')
            msg.attach(msgImage)


    msgText = MIMEText(content, send_format, 'utf-8')
    msg.attach(msgText)
    server = smtplib.SMTP(smtp_server,25)
    server.set_debuglevel(1)

    server.ehlo()
    server.starttls()
    server.login(From_addr,From_passwd)
    server.sendmail(From_addr,[To_addr],msg.as_string())
    server.quit()

