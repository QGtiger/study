from tkinter import *

def calback():
    var.set('吹吧你！')

root=Tk()
root.title('这是一个button组件')
root.iconbitmap(r'C:\Users\Administrator\Desktop\爬虫\tkinter组件\button\yoona.ico')
root.geometry('500x280')
root.resizable(width=False,height=False)
frame1=Frame(root)
frame2=Frame(root)
var=StringVar()
var.set('您所下载的影片含有未成年人限制内容，\n请满十八岁后再点击观看！')
textLabel=Label(frame1,textvariable=var,justify=LEFT)
textLabel.pack(side=LEFT)
photo=PhotoImage(file=r'C:\Users\Administrator\Desktop\爬虫\img\yoona.gif')
imgLabel=Label(frame1,image=photo)
imgLabel.pack(side=RIGHT)

theButton=Button(frame2,text='已满十八岁',command=calback)
theButton.pack()
frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)
mainloop()
