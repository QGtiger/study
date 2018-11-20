"""
author:lightfish
Time:2018.11.19
note:socket聊天室服务端
"""
from time import ctime
import socket
import threading

con = threading.Condition() #判断条件 锁 线程同步
host = input('input the servers ip address: ')
port = 8888
data = '' #客服端发送来的数据

s = socket.socket() #创建一个服务 套接字

print('Socket created...')
s.bind((host,port)) #绑定
s.listen(1)  #监听连接

print('Socket new listening...')

def NotifyAll(sss):
    global data
    if con.acquire(): #获取锁
        data = sss
        con.notifyAll() #表示当前线程放弃对资源的占有 通知其他线程从wait方法后面执行
        con.release() #释放

def threadOut(conn,nick): #发送消息
    global data
    while True:
        if con.acquire():
            con.wait() #放弃对当前资源的占有 等消息通知
            if data:
                try:
                    conn.send(data.encode()) #发送
                    con.release()
                except:
                    con.release()
                    return

def threadIn(conn,nick): #接收消息
    while True:
        try:
            temp = conn.recv(1024).decode()
            if not temp:
                conn.close()
                return
            NotifyAll(temp) #
            print(data)
        except:
            NotifyAll(nick+' error...')
            print(data)
            return




while True:
    conn,addr = s.accept()  #接受到了连接  addr包含ip和port
    print('Connected with'+addr[0]+':'+str(addr[1]))
    nick = conn.recv(1024).decode() #1024个字节
    NotifyAll('Welcome '+nick+' to the room...')
    print(ctime() + ': ' +data)
    conn.send(data.encode())
    threading.Thread(target=threadOut,args=(conn,nick)).start()
    threading.Thread(target=threadIn,args=(conn,nick)).start()
