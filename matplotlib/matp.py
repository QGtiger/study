"""
author:lightfish
Time:2018.10,9
note:matplotlib.pyplot的简单的教程：网址 https://blog.csdn.net/Notzuonotdied/article/details/77876080
"""
import matplotlib.pyplot as plt
import numpy as np
"""
x=np.linspace(-1,1,50)
print(x,type(x))
y=2*x+1
plt.plot(x,y)
plt.show()
"""
# 多个figure
x = np.linspace(-1, 1, 50)
y1 = 2*x + 1
y2 = 2**x + 1

# 使用figure()函数重新申请一个figure对象
# 注意，每次调用figure的时候都会重新申请一个figure对象
#plt.figure()
# 第一个是横坐标的值，第二个是纵坐标的值
#plt.plot(x, y1)

# 第一个参数表示的是编号，第二个表示的是图表的长宽
plt.figure(num = 'asd', figsize=(8, 5))
# 当我们需要在画板中绘制两条线的时候，可以使用下面的方法：
plt.plot(x, y2)
plt.plot(x, y1,
         color='red',   # 线颜色
         linewidth=1.0,  # 线宽
         linestyle='--'  # 线样式
        )
# 设置取值参数范围
plt.xlim((-1, 2))  # x参数范围
plt.ylim((1, 3))  # y参数范围

# 设置点的位置
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
# 为点的位置设置对应的文字。
# 第一个参数是点的位置，第二个参数是点的文字提示。
plt.yticks([-2, -1.8, -1, 1.22, 3],
          [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$readly\ good$'])


# 设置轴线的lable（标签）
plt.xlabel("I am x")
plt.ylabel("I am y")

# gca = 'get current axis'
ax = plt.gca()
# 将右边和上边的边框（脊）的颜色去掉
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 绑定x轴和y轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 定义x轴和y轴的位置
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

#曲线说明
l1, = plt.plot(x, y2,
               label='y=2^x+1'
              )
l2, = plt.plot(x, y1,
               color='red',  # 线条颜色
               linewidth = 1.0,  # 线条宽度
               linestyle='-.',  # 线条样式
               label='y=2*x+1'  #标签
              )

# 使用ｌｅｇｅｎｄ绘制多条曲线
plt.legend(handles=[l1, l2],
           labels = ['y=2^x+1', 'y=2*x+1'],
           loc = 'best'
          )

#条形图
n = 12
X = np.arange(n)
Y1 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)

plt.figure(figsize=(12, 8))
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
