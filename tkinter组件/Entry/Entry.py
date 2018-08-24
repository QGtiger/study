from tkinter import *

root=Tk()
root.title('Entry')
Label(root,text='作品:').grid(row=0)
Label(root,text='作者:').grid(row=1)
e1=Entry(root)
e2=Entry(root,show='*')
e1.grid(row=0,column=1,padx=10,pady=5)
e2.grid(row=1,column=1,padx=10,pady=5)

def show():
    a=Tk()
    a.title('结果')
    a.geometry('180x70')
    Label(a,text='作品：'+e1.get()+'\n'+'作者：'+e2.get(),justify=LEFT,padx=10).pack()
    e1.delete(0,END)
    e2.delete(0,END)
    a.mainloop()

def a():
    root.destroy()

Button(root,text='获取信息',width=10,command=show).grid(row=2,column=0,sticky=W,padx=10,pady=5)
Button(root,text='退出',width=10,command=a).grid(row=2,column=1,sticky=E,padx=10,pady=5)
mainloop()
