from tkinter import *

root=Tk()
root.title('Listbox')
scroll=Scrollbar(root)
scroll.pack(side=RIGHT,fill=Y)
theLb=Listbox(root,height=15,width=50,selectmode=EXTENDED,setgrid=True,yscrollcommand=scroll.set)
theLb.pack()
scroll.config(command=theLb.yview)
for item in range(30):
    theLb.insert(END,item)
Button(root,text='delete',command=lambda x=theLb:x.delete(ACTIVE)).pack()
mainloop()
                                                                        
