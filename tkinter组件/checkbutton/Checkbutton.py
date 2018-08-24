from tkinter import *

root=Tk()
root.title('四大美女')
root.iconbitmap(r'c:\\Users\image\yoona.ico')
root.geometry('300x200')
GIRLS=['西施','王昭君','貂蝉','杨玉环']
v=[]
for girl in GIRLS:
    v.append(IntVar())
    b=Checkbutton(root,text=girl,variable=v[-1])
    a=Label(root,textvariable=v[-1])
    b.pack(anchor=W)
    a.pack(anchor=E)

mainloop()
