"""
author；lightfish
Time:2018.10.18

"""
import matplotlib.pyplot as plt
import random
import numpy as np
'''
#使用内建模块random实现
position = 0
walk = []
steps=1000
for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position+=step
    walk.append(position)

plt.plot(walk[:10])

#np.random模块来实现
nsteps = 1000
draws = np.random.randint(0,2,size=nsteps)
draw = np.where(draws>0,1,-1)
draw=draw.cumsum()
plt.figure(num='np.random')
plt.plot(draw[:10])
print(draw[:10]>0)
'''
#一次性模拟多次随机漫步
"""
nwalks = 5000
nsteps=1000
draws=np.random.randint(0,2,size=(nwalks,nsteps))
draw = np.where(draws>0,1,-1)
walks = draw.cumsum(1)
print(walks)
print(walks.max(),walks.min())
print(len((walks>=30).any(1)))
print((np.abs(walks)).max())"""

#判断sum,any,cumsum等函数axis的方向性
arr = np.random.randint(-5,6,size=(5,5))
print(arr)
#axis为1时，横向相加
sum = np.sum(arr,axis=1)
print(sum)
#cumsum,axis为1时，横向相加
cumsum = np.cumsum(arr,axis=1)
print(cumsum)
#any和all,为1时，横向为一个整体
print((arr>0).sum())
