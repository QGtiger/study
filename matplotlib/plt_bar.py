"""
aythor:lightfish
Time:2018.10.10
note:matplotlib.pyplot的简单的教程：网址 https://blog.csdn.net/baidu_37366272/article/details/80115021
柱状图的简单绘制
"""
import matplotlib.pyplot as plt
import numpy as np

#条形图
n = 12
X = np.arange(n)
Y1 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)

plt.figure(figsize=(12, 8))
plt.title('test')
#facecolor是条形图的颜色，edgecolor是条形边沿的颜色
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X,Y1):
    # ha: horizontal alignment水平方向
    # va: vertical alignment垂直方向
    plt.text(x, y+0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X,-Y2):
    # ha: horizontal alignment水平方向
    # va: vertical alignment垂直方向
    plt.text(x, y+0.05, '%.2f' % y, ha='center', va='top')

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
# 定义范围和标签
plt.xlim(-5, n)
#消除x轴的标识
plt.xticks(())
plt.ylim(-1.25, 1.25)
#消除y轴的标识
plt.yticks(())

plt.show()