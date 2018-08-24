from tkinter import *

root=Tk()
root.title('Radiobutton')
root.geometry('300x200')
group=LabelFrame(root,text='最好的语言',padx=10,pady=10)
group.pack(padx=15,pady=15)
v=IntVar()
v.set(1)
Langs=[
    ('Python',1),
    ('C',2),
    ('C++',3),
    ('Django',4)]
for lang,num in Langs:
    b=Radiobutton(group,text=lang,variable=v,value=num,
                  #indicatoron=False
                  )
    b.pack(anchor=W)
mainloop()
