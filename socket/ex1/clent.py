"""
author:lightfish
Time:2018.11.19
note:socker聊天室客户端
"""
import socket  #自带模块
import threading
from time import ctime

outString = ''
nick = ''
inString=''

def client_send(sock):
    global outString
    while True:
        #监听输入 如果有输入就发送服务端
        outString = input()#接受输入
        outString =ctime()+ ':' + nick+': '+outString
        sock.send(outString.encode())


def client_accept(sock):
    global inString
    while True:
        try:
            inString = sock.recv(1024).decode() #接收数据
            if not inString:
                break
            if outString != inString:
                print(inString)
        except:
            break


nick = input('input your nickname: ')
ip = input('input the server ip address: ')
port=8888 #端口
sock = socket.socket() #创建套接字
sock.connect((ip,port)) #连接
sock.send(nick.encode()) #把用户名发送给服务端

th_send = threading.Thread(target=client_send,args=(sock,))  #发送信息 target 方法 args 参数
th_send.start()

th_accept = threading.Thread(target=client_accept,args=(sock,))
th_accept.start()