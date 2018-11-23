# Python基础要点

### 1.一行代码实现1--100之和
```
sum(range(101))
```
![img](https://github.com/QGtiger/study/blob/master/Python_image/1.jpg)

### 2.如何在一个函数内部修改全局变量
利用`global`修改全局变量<br>
```global```<br>
![global](https://github.com/QGtiger/study/blob/master/Python_image/2.jpg)

### 3.列出5个Python的标准库
* `os`: 提供了不少于操作系统相关联的函数
* `sys`: 通常用于命令行参数
* `re`: 正则匹配
* `math`: 数学运算
* `datetime`: 处理日期时间

### 4.字典如何删除键和合并两个字典
    删除用 del,合并用 update
```
dic = {'name':'qg','age':18}
del dic['name']
dic2 = {'name':'fh'}
dic.update(dic2)
```
![del update](https://github.com/QGtiger/study/blob/master/Python_image/3.jpg)

### 5.谈下python的GIL
* GIL是Python的全局解释器锁，同一个进程加入由多个线程运行，一个线程在运行python程序的时候会霸占python解释器(加了一个锁即GIL)
，使进程内的其他线程无法运行，等该线程运行完后其他线程才能运行。如果线程运行过程中遇到耗时操作，则解释器锁解开，使其他线程
运行。所以在多线程中，线程的运行仍是有先后顺序，并不是同时运行。
* 多进程中因为每个进程都能被喜用分批资源，相当于每个进程有了个python解释器，多以多进程可以实现多个进程的同时运行，缺点是金城系统资源开销大

### 6.python实现列表去重的方法
>熟悉使用`set`
```
list=[np.random.randint(10,15) for _ in range(10)]
print(list)
a = set(list)
print(a)
[i for i in a]
```
![set](https://github.com/QGtiger/study/blob/master/Python_image/6.jpg)

### 7.fun(*args,**kwargs)中*args，**kwargs是什么意思？
* *args和*kwargs主要用于函数的定义。你可以将不定数量的参数传递给一个函数。这里的不定的意思是：预先并不知道，函数使用者会传递多少个参数给你，所以在这个场景下使用这两个关键字。*args是用来发送一个非键值对的可变数量的参数列表给一个函数。这里有一个例子
```
def demo(args_f,*args_v):
    print(args_f)
    for x in args_v:
        print(x)
demo('a','b','c','d',e')
```
![*args](https://github.com/QGtiger/study/blob/master/Python_image/7.jpg)

* **kwargs 允许你将不定长度的键值对传递给一个函数。如果你想要一个函数里处理带名字的参数，你因该使用**kwargs，这里有一个例子
```
def demo(**args_v):
    for k,v in args_v.items():
        print(k,v)
demo(name='light',name='fish)
```
![*kwargs](https://github.com/QGtiger/study/blob/master/Python_image/7-2.jpg)

### 8.python2和python3的range的区别
```python2返回一个列表，python3返回一个迭代器，节约内存```

### 9.一句话解释什么样的语言能过用装饰器
```函数可以作为参数传递的语言，可以使用装饰器```

### 10.python内建函数类型有哪些
* 整型 -- `int`
* 布尔型 -- `bool`
* 字符串 -- `str`
* 列表 -- `list`
* 元组 -- `tuple`
* 字典 -- `dict`
* 集合 -- `set`

### 11.简述面向对象中__new__和__init__的区别
* __init__是初始化方法，创建对象后，就立刻被默认调用，相当于C语言的构造函数，可接受参数，如下图：
![__init__](https://github.com/QGtiger/study/blob/master/Python_image/11.jpg)
* __new__至少要有一个参数cls，代表是当前类，此参数在实例化的时候由Python解释器自动识别
* __new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类(通过super(当前类，cls)) __new__出来的实例，或者直接是object的__new__出来的实例
* 
