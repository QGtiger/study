"""
author: lightfish
Time:2018.11.27
note:CPU调度运算
"""
import re
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt


class Process:
    def __init__(self, Pn, reach_time, server_time):
        self.Pn = Pn
        self.reach_time = reach_time
        self.server_time = server_time


def gantetu(name, df):
    plt.figure(num=name + ' 甘特图', figsize=(8, 5))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.ylim((0, 5))
    plt.xticks([x for x in range(28)])
    plt.xlabel('time')
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    for i in range(len(df)):
        pcolor = int(re.search('\d+',df.iloc[i]['进程']).group())
        plt.broken_barh([(int(df.iloc[i]['到达时间']), int(df.iloc[i]['服务时间']))], [
                        0, 1], facecolors=color[pcolor], label='进程 ' + df.iloc[i]['进程'])
        plt.text(df.iloc[i]['到达时间'], 1.1, df.iloc[i]['进程'])
    plt.legend()
    plt.show()


if __name__ == '__main__':
    print('---------author: lightfish-----------------')
    print('---------time: 2018.11.28------------------')
    print('---------本程序用于模拟CPU进程调度---------')
    print('---------请按提示进行操作------------------')
    print('---------非抢占式短作业优先请输入1---------')
    print('---------抢占式短作业优先请输入2-----------')
    print('---------先来先服务优先调度算法请输入3-----')
    print('---------时间片轮转调度算法请输入4---------')
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
            print('调试时间:{}s'.format(end - start))
            is_look = input('是否展示甘特图(Y/N): ')
            color = (
                "turquoise",
                "crimson",
                "yellow",
                "green",
                "red",
                "brown",
                "blue")  # 颜色，不够再加
            if is_look.upper() == 'Y':
                gantetu('非抢占式短作业优先', df)
            else:
                print('不看算了 QAQ...')
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
                min_reach_time = int(
                    inprocess1[0]) if int(
                    inprocess1[0]) < min_reach_time else min_reach_time
                processn = Process(i, *[int(inprocess1[i])
                                        for i in range(len(inprocess1[:2]))])
                p.append(processn)
            p.sort(key=lambda x: x.reach_time)
            running_process = []
            running_time = []
            start = time.clock()
            for i in range(min_reach_time, max_time):
                for p1 in p:
                    if i < p1.reach_time:
                        break
                    if i >= p1.reach_time:
                        p.remove(p1)
                        running_process.append(p1)
                r1 = min(running_process, key=lambda x: x.server_time)
                running_process[running_process.index(r1)].server_time -= 1
                if running_process[running_process.index(r1)].server_time == 0:
                    running_process.remove(r1)
                running_time.append(r1.Pn)
            # print(running_time)
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

            # print(get_process)
            # print(get_process_reach)
            for i in range(len(get_process_reach)):
                if i < len(get_process_reach) - 1:
                    get_process_server.append(
                        get_process_reach[i + 1] - get_process_reach[i])
                    continue
                get_process_server.append(max_time - get_process_reach[i])

            end = time.clock()

            d1 = pd.Series(get_process)
            d2 = pd.Series(get_process_reach)
            d3 = pd.Series(get_process_server)
            df = pd.concat((d1, d2, d3), axis=1)
            df.columns = ['进程', '到达时间', '服务时间']
            df.index = [
                '第{}次调度'.format(
                    i +
                    1) for i in range(
                    len(get_process))]
            print(df)
            print('调试时间:{}s'.format(end - start))

            is_look = input('是否展示甘特图(Y/N): ')
            color = (
                "turquoise",
                "crimson",
                "yellow",
                "green",
                "red",
                "brown",
                "blue")  # 颜色，不够再加
            if is_look.upper() == 'Y':
                gantetu('抢占式短作业优先', df)
            else:
                print('不看算了 QAQ...')

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
                min_reach_time = int(
                    inprocess1[0]) if int(
                    inprocess1[0]) < min_reach_time else min_reach_time
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
                    d2.append(d2[i - 1] + d3[i - 1])
            end = time.clock()
            d2 = pd.Series(d2)
            df = pd.concat((d1, d2, d3), axis=1)
            df.columns = ['进程', '到达时间', '服务时间']
            df.index = ['第{}次调度'.format(i + 1) for i in range(len(p))]

            print(df)
            print('调试时间:{}s'.format(end - start))

            is_look = input('是否展示甘特图(Y/N): ')
            color = (
                "turquoise",
                "crimson",
                "yellow",
                "green",
                "red",
                "brown",
                "blue")  # 颜色，不够再加
            if is_look.upper() == 'Y':
                gantetu('先来先服务优先调度', df)
            else:
                print('不看算了 QAQ...')

            print('---------模拟先来先服务优先调度算法调试结束---------\n')
        if instruction == '4':
            print('---------模拟时间片轮转调度算法---------')
            Pn = input('请输入要模拟的进程数量: ')
            num = int(input('请输入每个时间片消耗的资源时间: '))
            p = []
            for i in range(int(Pn)):
                inprocess = input('请输入P{}进程的服务时间: '.format(i))
                inprocess1 = re.findall(r'\d+', inprocess)
                processn = Process(i, 0, *[int(inprocess1[i])
                                           for i in range(len(inprocess1[:1]))])
                p.append(processn)
            start = time.clock()
            d1 = []
            d2 = []
            check_p = p[:]
            while True:
                p = check_p[:]
                if not p:
                    break
                for i in range(len(p)):
                    if p[i].server_time > num:
                        p[i].server_time -= num
                        d1.append('P{}'.format(p[i].Pn))
                        d2.append(int(num))
                    else:
                        d1.append('P{}'.format(p[i].Pn))
                        d2.append(int(p[i].server_time))
                        check_p.remove(p[i])

            d3 = [y - d2[x] for x, y in enumerate(np.cumsum(d2))]
            end = time.clock()
            df = pd.concat(
                (pd.Series(d1), pd.Series(d3), pd.Series(d2)), axis=1)
            df.columns = ['进程', '到达时间', '服务时间']
            df.index = ['第{}次调度'.format(i + 1) for i in range(len(d1))]
            print(df)
            print('调试时间:{}s'.format(end - start))
            is_look = input('是否展示甘特图(Y/N): ')
            color = (
                "turquoise",
                "crimson",
                "yellow",
                "green",
                "red",
                "brown",
                "blue")  # 颜色，不够再加
            if is_look.upper() == 'Y':
                gantetu('时间片轮转调度算法', df)
            else:
                print('不看算了 QAQ...')

            print('---------模拟时间片轮转调度算法调试结束---------\n')
        if instruction == 'quit':
            print('程序已退出...')
            break
