"""
author: lightfish
Time:2018.11.27
note:CPU调度运算
"""
import re
import numpy as np

class Process:
    def __init__(self, Pn, reach_time, server_time):
        self.Pn = Pn
        self.reach_time = reach_time
        self.server_time = server_time


if __name__ == '__main__':
    print('---------本程序用于模拟CPU进程调度---------')
    print('---------请按提示进行操作---------')

    Pn = input('请输入要模拟的进程数量: ')
    p = []
    for i in range(int(Pn)):
        inprocess = input('请输入P{}进程的到达时间和服务时间: '.format(i + 1))
        inprocess1 = re.findall(r'\d+', inprocess)
        # print(inprocess1)
        processn = Process(i + 1, *[inprocess1[i]
                                    for i in range(len(inprocess1[:2]))])
        p.append(processn)
        # print(processn.Pn)
    p = sorted(p, key=lambda x: x.server_time)
    print(len(p))
    a = np.array([i.server_time for i in p])
    print(a)
    np.cumsum(a)
    print(a)
    for index,i in enumerate(p):
        print('P{}'.format(i.Pn), end='->' if index != len(p) - 1 else ' ')
