import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr,formataddr
import requests
from bs4 import BeautifulSoup

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

def get_page(url):
    html = requests.get(url)
    html = html.text
    soup = BeautifulSoup(html,'lxml')
    return soup.find('h1').get_text().split(' ')[1]

def get_text(url):
    html = requests.get(url)
    html = html.text
    soup = BeautifulSoup(html, 'lxml')
    return soup.find(attrs={'id':'content'}).get_text()

def send_yz_email(addr,bookurl):
    from_addr = 'qg12148@163.com'
    passwd = 'qwer123QG'
    smtp_server = 'smtp.163.com'

    #创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = _format_addr('lightfish<%s>' % from_addr)
    msg['To'] = _format_addr('Python学习者<%s>' % addr)
    msg['Subject'] = Header('元尊小说更新...','utf-8').encode()

    content = '<h1>元尊</h1><h3>元尊已更新至最新章节: <a href="%s">%s</a></h3><br><p>%s</p>' % (bookurl,get_page(bookurl),get_text(bookurl))
    content+='<img src="cid:0">'
    msgHTML = MIMEText(content,'html','utf-8')
    msg.attach(msgHTML)

    with open('image/11.jpg','rb') as f:
        msgImage = MIMEImage(f.read())
        msgImage.add_header('Content-ID','<0>')
        msg.attach(msgImage)

    server = smtplib.SMTP(smtp_server,25)
    server.login(from_addr,passwd)
    #server.set_debuglevel(1)
    server.sendmail(from_addr,addr,msg.as_string())
    server.quit()

if __name__=='__main__':
    send_yz_email('1426286337@qq.com','https://www.ddbiquge.com/chapter/1586_20712404.html')
