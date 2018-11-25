## 利用smtp协议进行发邮件

#### 在Python3自带smtplib模块，能够进行操作，不需要进行第三方库的安装
#### Python3对SMTP支持的有`smtplib`和'eamil'两个模块,`email`负责构造邮件，`smtplib`负责发送邮件

### 1.首先我们当然要引入我们需要的模块和函数
```
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from email.utils import parseaddr,formataddr
from email.mime.multipart import MIMEMultipart
import re
import os
```
![模块的引入](https://github.com/QGtiger/study/blob/master/Python_image/Email_SEND/1.jpg)

### 2.我们编写了一个函数`_format_addr()`来格式化一个邮件地
* 注意不能简单地传入`name <addr@example.com>`，因为如果包含中文，需要通过Header对象进行编码。
```
def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))
```

### 3.发送HTML邮件
* 如果我们要发送HTML邮件，而不是普通的纯文本文件怎么办？方法很简单，在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了
```
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
```
![img](https://github.com/QGtiger/study/blob/master/Python_image/Email_SEND/2.jpg)
