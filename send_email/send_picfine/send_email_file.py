"""
authoe:lightfish
Time:2018.10.27
note:如果Email中要加上附件怎么办？带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，
所以，可以构造一个MIMEMultipart对象代表邮件本身，
然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象即可
"""
import smtplib
from email.utils import parseaddr,formataddr
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#重点中的重点就是下面这个函数，格式化一个邮件地址
#注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码
def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

if __name__=='__main__':
    from_addr = input('From:')
    passwd = input('Passwd:')
    to_addr = input('To:')
    smtp_server = input('Smtp server:')
    #邮件对象
    msg = MIMEMultipart()

    msg['From'] = _format_addr('Python学习者<%s>' % from_addr)
    msg['To'] = _format_addr('管理者<%s>' % to_addr)
    msg['Subject'] = Header('来自一位SMTP学习者的问候...','utf-8').encode()
    #邮件正文MIMEText用attach添加
    msg.attach(MIMEText('send with a Picfile...','plain','utf-8'))

    #添加附件就是加上一个MIMEBase，从本地读取一个图片：
    with open(r'E:\PythonPic\允儿2\58.jpg','rb') as f:
        #设置附件的MIME和文件，这里是jpg类型
        mime = MIMEBase('image','jpg',filename='text.jpg')
        #加上必要的头信息
        mime.add_header('Content_Disposition','attachment',filename='test.jpg')
        mime.add_header('Content-ID','<0>')
        mime.add_header('X-Attachment-Id','0')
        #把附件的内容读进来
        mime.set_payload(f.read())
        #用Base64编码
        encoders.encode_base64(mime)
        #添加到MIMEMultipart:
        msg.attach(mime)
    server = smtplib.SMTP(smtp_server,25)
    server.set_debuglevel(1)
    server.login(from_addr,passwd)
    server.sendmail(from_addr,to_addr,msg.as_string())
    server.quit()


