"""
author:lightfish
Time:2018.11.21
note:银行家算法的实现
"""
import copy
import re
import pandas as pd



#初始化函数
def bank_init():
    Process = [0]


#安全性算法函数
def bank_safe(Available,Need,Allocation,Pn):
    #创建Work数组 初始值为Avaliable
    Work = copy.deepcopy(Available)
    #创建Finish数组  默认设为全0 （False）
    Finish = [0]*Pn
    #创建安全序列
    safeSequence = []
    #大循环5次
    count = 0
    while count<Pn:
        # 按进程编号顺序找到一个可加入安全序列的进程，即满足Finish[i]=False
        # 且Needi <= Work 的进程Pi，则假设该进程不久将完成任务
        i = 0  # 进程下标
        while i < Pn:
            isSafe = True  # 记录当前进程是否可以加入安全序列
            # 如果该进程finish值为0（False）
            if not Finish[i]:
                # 比较Need[i]与Work的各元素值
                for ch in Work.keys():
                    # 如果需求大于可用
                    if Need[i][ch] > Work[ch]:
                        isSafe = False
                # for循环之后根据isSafe判断该进程是否可以加入安全序列
                if isSafe:  # isSafe为True说明可以加入安全序列
                    safeSequence.append(i+1)  # 加入安全序列
                    Finish[i] = True  # 将此进程的finish值设为True
                    for ch2 in Work.keys():
                        # Work = Work+Allocation[i]
                        Work[ch2] = Work[ch2] + Allocation[i][ch2]
            i += 1  # 结束本次循环，开始判断下一个进程
        count += 1 # 开始下一轮判断
    #判断安全序列里面的元素个数，如果等于进程数Pn 说明安全，输出安全序列
    if len(safeSequence) ==Pn:
        print("系统处于安全状态，计算得出安全序列：",safeSequence)
        return True
    #不安全  返回False
    print("系统处于不安全状态,资源请求失败")
    return False


#模拟进程请求资源函数
#传入进程序号和请求request字典
def bank_request(processId,requestDict):
    print("接收到请求时分配情况Allocate:", Allocation)
    #第一步：如果请求的资源数是否超过它所需要的最大值
    for ch in requestDict.keys():
        # 如果请求资源数超过它所需要的最大值
        if requestDict[ch] > Need[processId-1][ch]:
            print("由于请求数超过最大值，请求资源被拒绝！")
            return False #返回错误
    #第二步：判断请求资源与可用资源的关系
    for ch2 in requestDict.keys():
        # 如果无足够资源
        if requestDict[ch2] > Available[ch2]:
            print("由于可用资源不足，请求资源被拒绝！")
            return False #返回错误

     # 第三步：分配资源
    for ch3 in requestDict.keys():
        #Available[j] = Available[j] - Requesti[j]
        Available[ch3] = Available[ch3] - requestDict[ch3]
    #Allocation[i,j] = Allocation[i,j] + Requesti[j]
    allo = Allocation[processId-1]
    for ch4 in allo.keys():
        allo[ch4] = allo[ch4] +requestDict[ch4]
    #Need[i, j] = Need[i, j] - Requesti[j]
    need = Need[processId - 1]
    for ch5 in need.keys():
        need[ch5] = need[ch5] - requestDict[ch5]


    #第四步：进行系统执行安全性检查,如果为安全状态，分配成功，否则还原到分配前的状态
    if  bank_safe(Available,Need,Allocation,Pn):
        print("请求完成时分配情况Allocate:", Allocation)
    else:
        # 还原到分配前的状态
        for ch3 in requestDict.keys():
            # Available[j] = Available[j] + Requesti[j]
            Available[ch3] = Available[ch3] + requestDict[ch3]
        # Allocation[i,j] = Allocation[i,j] - Requesti[j]
        allo = Allocation[processId - 1]
        for ch4 in allo.keys():
            allo[ch4] = allo[ch4] - requestDict[ch4]
        # Need[i, j] = Need[i, j] + Requesti[j]
        need = Need[processId - 1]
        for ch5 in need.keys():
            need[ch5] = need[ch5] + requestDict[ch5]

    return Allocation

#计算Need数组
def bank_need(Allocation,Max):
    Need = []
    cn = 0
    for allo in Allocation:
        tmp = copy.deepcopy(allo)  # 深拷贝一个同规格字典用于存放need
        for ch in allo.keys():
            tmp[ch] = Max[cn][ch] - allo[ch]
        Need.append(tmp)
        cn += 1
    return Need

#更新Available数组
def bank_Available(Available,Allocation):
    for allo in Allocation:
        for ch in allo.keys():
            Available[ch] =Available[ch] -  allo[ch]
    return Available


def is_checked(w,n):
    for i in w.keys():
        if n[i]>w[i]:
            return False
    return True

def add_resource(w,a):
    return {'A':w['A']+a['A'],'B':w['B']+a['B'],'C':w['C']+a['C']}

def sub_resouce(w,a):
    return {'A': w['A'] - a['A'], 'B': w['B'] - a['B'], 'C': w['C'] - a['C']}

#找出所有的安全序列
def find_list(work,need,allocation,list,p,b,c=0):
    for i in range(p):

        if is_checked(work,need[i]) and b[i] !=True:
            work = add_resource(work,allocation[i])
            b[i] = True
            list.append(i)
            find_list(work,need,allocation,list,p,b,i)
            work = sub_resouce(work,allocation[i])
    if not False in b:
        print(list)
    b[c]=False
    if list == []:
        return
    list.pop()

    return



if __name__ == '__main__':
    print("---------本程序用于演示银行家算法---------")
    print("---------即将开始收集初始数据，请按提示操作---------' ")

    # 得到进程数量Pn,作为参数创建进程列表
    Pn = int(input("请输入要模拟的进程数量n:"))
    bool = [False for _ in range(Pn)]
    # 得到可利用资源向量Available
    a = input("请输入系统初始资源信息:")
    a1 = re.findall('\d+', a)
    Available = {'A': int(a1[0]), 'B': int(a1[1]), 'C': int(a1[2])}
    print('资源数为：',Available)
    # 得到输入每个进程对每种资源的最大需求、已经获得的数量、每种类型资源的数目
    print("---------即将开始输入Max的信息---------' ")
    Max = []
    for i in range(0,Pn):
        m = input("请输入第{}个进程对每种资源的最大需求，请输入输入A,B,C的最大请求数:".format(i))


        m1 = re.findall('\d+',m)
        max={'A':int(m1[0]),'B':int(m1[1]),'C':int(m1[2])}

        Max.append(max)
    print(pd.DataFrame(Max))
    print("---------即将开始输入Allocation的信息---------' ")
    Allocation = []
    for i in range(0,Pn):
        a = input("请输入第{}个进程对每种资源的最大需求，请输入输入A,B,C的最大请求数:".format(i))

        a1 = re.findall('\d+',a)
        allo={'A':int(a1[0]),'B':int(a1[1]),'C':int(a1[2])}

        Allocation.append(allo)
    print(pd.DataFrame(Allocation))

    print("---------计算得到初次分配后的Need矩阵---------' ")
    Need =bank_need(Allocation, Max)#计算得到初次分配后的need矩阵
    print(pd.DataFrame(Need))

    print('安全序列：')
    list=[]
    find_list(Available,Need,Allocation,list,Pn,bool)

    # print("---------计算得到初次分配后的Available数组---------' ")
    # bank_Available(Available,Allocation)#计算得到初次分配后的Available字典

    # while True:
    #     print("---------模拟进程请求资源请输入1---------")
    #     print("---------对系统当前状态进行诊断请输入2---------")
    #     print("---------查看当前资源分配情况请输入3---------")
    #     print("---------退出程序请输入quit---------")
    #     x = input('请输入执行的功能序号x：')#提示输入
    #     if x == '1':
    #         print("---------即将开始模拟进程请求资源---------")
    #         processId = int(input("请输入要模拟的进程序号n:"))
    #         requestDict = eval(input("请输入请求资源信息，输入格式如'{'A':10, 'B':10, 'C':10}' :"))
    #         bank_request(processId, requestDict) #模拟请求资源
    #         print("---------模拟进程请求资源已结束---------")
    #     elif x == '2':
    #         print("---------即将开始诊断当前系统状态---------")
    #         bank_safe(Available, Need, Allocation, Pn)
    #         print("---------诊断当前系统状态已结束---------")
    #     elif x == '3':
    #         print("---------当前资源分配情况如下---------")
    #         print(Allocation)
    #     elif x=='quit':
    #         print('程序结束运行')
    #         break
