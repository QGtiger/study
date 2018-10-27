"""
author:lightfish
Time:2018.10.27
note:使用python实现电子邮件的发送。
SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。

Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。


"""

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib
#重点中的重点就是下面这个函数，格式化一个邮件地址
#注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
    #name.addr = parseaddr(s)
    #return formataddr((Header(name,'utf-8').encode(),addr))

# 输入Email地址和口令:
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入SMTP服务器地址:(如果是qq的话是smtp.qq.com)
smtp_server = input('SMTP server: ')

#第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，
# 最后一定要用utf-8编码保证多语言兼容性。
#msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

#如果要发送HTML邮件，在构造MIMEText对象，把html字符串传进去，第二个参数改为html
msg = MIMEText('<html><body><h1>Hello</h1><p>send by <a href="http://www.python.org">Python</a>...</p></body></html>','html','utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)#SMTP协议默认端口是25
#set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)
server.login(from_addr, password)
#as_string()把MIMEText对象变成str。
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()