"""
author: lightfish
Time:2018.11.27
note:CPU调度运算
"""
import re
import numpy as np
import pandas as pd
import time

class Process:
    def __init__(self, Pn, reach_time, server_time):
        self.Pn = Pn
        self.reach_time = reach_time
        self.server_time = server_time


if __name__ == '__main__':
    print('---------author: lightfish-----------------')
    print('---------time: 2018.11.28------------------')
    print('---------本程序用于模拟CPU进程调度---------')
    print('---------请按提示进行操作------------------')
    print('---------非抢占式短作业优先请输入1---------')
    print('---------抢占式短作业优先请输入2-----------')
    print('---------先来先服务优先调度算法请输入3-----')
    print('---------输入quit退出此程序----------------')
    while True:
        instruction = input('请输入指令: ')
        if instruction == '1':
            print('---------模拟非抢占式短作业优先调试...---------')
            Pn = input('请输入要模拟的进程数量: ')
            p = []
            for i in range(int(Pn)):
                inprocess = input('请输入P{}进程的服务时间: '.format(i))
                inprocess1 = re.findall(r'\d+', inprocess)
                # print(inprocess1)
                processn = Process(i, 0, *[inprocess1[i]
                                           for i in range(len(inprocess1[:1]))])
                p.append(processn)
                # print(processn.Pn)
            start = time.clock()
            p = sorted(p, key=lambda x: x.server_time)
            a = np.array([int(i.server_time) for i in p])
            d2 = [y - a[x] for x, y in enumerate(np.cumsum(a))]
            # for index, i in enumerate(p):
            #     print(
            #         'P{}'.format(
            #             i.Pn),
            #         end='->' if index != len(p) -
            #         1 else '\n')
            d1 = ['P{}'.format(x.Pn) for x in p]
            df1 = pd.Series(d1)
            df2 = pd.Series(d2)
            df = pd.concat((df1, df2, pd.Series(
                [i.server_time for i in p])), axis=1)
            df.columns = ['进程', '到达时间', '服务时间']
            df.index = ['第{}次调度'.format(i + 1) for i in range(len(p))]

            end = time.clock()
            print(df)
            print('调试时间:{}s'.format(end-start))
            print('---------模拟非抢占式短作业优先调试结束---------\n')
        if instruction == '2':
            print('---------模拟抢占式短作业优先调试...---------')
            Pn = input('请输入要模拟的进程数量: ')
            p = []
            min_reach_time = 100
            max_time = 0
            for i in range(int(Pn)):
                inprocess = input('请输入P{}进程的到达时间和服务时间: '.format(i))
                inprocess1 = re.findall(r'\d+', inprocess)
                max_time += int(inprocess1[1])
                min_reach_time = int(inprocess1[0]) if int(inprocess1[0]) < min_reach_time else min_reach_time
                processn = Process(i, *[int(inprocess1[i])
                                        for i in range(len(inprocess1[:2]))])
                p.append(processn)
            p.sort(key=lambda x: x.reach_time)
            running_process = []
            running_time = []
            start = time.clock()
            for i in range(min_reach_time,max_time):
                for p1 in p:
                    if i < p1.reach_time:
                        break
                    if i >= p1.reach_time:
                        p.remove(p1)
                        running_process.append(p1)
                r1 = min(running_process,key=lambda x: x.server_time)
                running_process[running_process.index(r1)].server_time -= 1
                if running_process[running_process.index(r1)].server_time == 0:
                    running_process.remove(r1)
                running_time.append(r1.Pn)
            #print(running_time)
            c1 = -1
            get_process = []
            get_process_reach = []
            get_process_server = []
            for i in range(len(running_time)):
                if running_time[i] != c1:
                    t = running_time[i]
                    get_process.append('P{}'.format(t))
                    get_process_reach.append(i)
                    c1 = t

            #print(get_process)
            #print(get_process_reach)
            for i in range(len(get_process_reach)):
                if i < len(get_process_reach)-1:
                    get_process_server.append(get_process_reach[i+1] - get_process_reach[i])
                    continue
                get_process_server.append(max_time - get_process_reach[i])

            end = time.clock()

            d1 = pd.Series(get_process)
            d2 = pd.Series(get_process_reach)
            d3 = pd.Series(get_process_server)
            df = pd.concat((d1,d2,d3),axis=1)
            df.columns = ['进程','到达时间','服务时间']
            df.index = ['第{}次调度'.format(i + 1) for i in range(len(get_process))]
            print(df)
            print('调试时间:{}s'.format(end-start))
            print('---------模拟抢占式短作业优先调试结束---------\n')
        if instruction == '3':
            print('---------模拟先来先服务优先调度算法...---------')
            Pn = input('请输入要模拟的进程数量: ')
            p = []
            min_reach_time = 100
            max_time = 0
            for i in range(int(Pn)):
                inprocess = input('请输入P{}进程的到达时间和服务时间: '.format(i))
                inprocess1 = re.findall(r'\d+', inprocess)
                max_time += int(inprocess1[1])
                min_reach_time = int(inprocess1[0]) if int(inprocess1[0]) < min_reach_time else min_reach_time
                processn = Process(i, *[int(inprocess1[i])
                                        for i in range(len(inprocess1[:2]))])
                p.append(processn)
            start = time.clock()
            p.sort(key=lambda x: x.reach_time)
            d1 = pd.Series(['P{}'.format(i.Pn) for i in p])
            d3 = pd.Series([i.server_time for i in p])
            d2 = []
            for i in range(len(p)):
                if i == 0:
                    d2.append(0)
                else:
                    d2.append(d2[i-1]+d3[i-1])
            end = time.clock()
            d2 = pd.Series(d2)
            df = pd.concat((d1,d2,d3),axis=1)
            df.columns = ['进程', '到达时间', '服务时间']
            df.index = ['第{}次调度'.format(i + 1) for i in range(len(p))]

            print(df)
            print('调试时间:{}s'.format(end - start))
            print('---------模拟先来先服务优先调度算法调试结束---------\n')
        if instruction == 'quit':
            print('程序已退出...')
            break
