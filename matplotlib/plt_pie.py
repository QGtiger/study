"""
author:lightfish
Time:2018.10.10
note:matplotlib.pyplot的简单的教程：网址 https://blog.csdn.net/baidu_37366272/article/details/80115021
画饼图的简单绘制
"""
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

cos = ['b', 'r', 'y', 'g']
slices = [7, 2, 2, 13]
activaties = ['sleeping', 'eating', 'working', 'playing']

plt.pie(slices,
        labels=activaties,
        colors=cos,
        startangle=90,  # 从90度处开始循环
        shadow=True,  # 有阴影，显得更加立体
        explode=(0, 0, 0, 0.1),  # 把其中一块拉出来
        autopct='%1.1f%%')  # 显示比例

plt.xlabel('x')
plt.ylabel('y')
plt.title('ok')
plt.legend()
plt.show()
