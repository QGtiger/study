"""
author:lightfish
Time:2018.10.14
note:用subplot和subplots绘制子图
网址：https://blog.csdn.net/sinat_35930259/article/details/80002213
"""
import matplotlib.pyplot as plt
import numpy as np
plt.figure(num='subplot')

x=np.linspace(0,5)
y1=np.sin(np.pi*x)
y2=np.sin(np.pi*x*2)
plt.subplot(2,1,1)
plt.plot(x,y1,'b--',label='sin(pi*x)')
plt.ylabel('y1 value')
plt.subplot(2,1,2)
plt.plot(x,y2,'r--',label='sin*2x')
plt.ylabel('y2 value')
plt.xlabel('x value')

#subplots返回的值的类型为元组，其中包含两个元素：第一个为一个画布，第二个是子图
a=plt.subplots(2,2)
plt.show()