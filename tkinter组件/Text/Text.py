from tkinter import *
import urllib.request
from bs4 import BeautifulSoup
import hashlib

root=Tk()
text=Text(root,width=50,height=20,undo=True,autoseparators=False)
text.pack()
text.insert(INSERT,'This is a Text')
img=PhotoImage(file=r'C:\Users\Administrator\Desktop\允儿\5.gif')
def show():
    #text.image_create(END,image=img)
    
    #label=Label(text,text='pyhton\n我瞧你吗',justify=LEFT,image=img,fg='#fff',compound=CENTER,font=('DFKai-SB',15))
    #text.window_create(END,window=label)
    '''
    group=LabelFrame(text,text='LabelFrame',bg='#fff',padx=10,pady=10)
    group.pack(padx=15,pady=15)
    L=[
        ('python',1),
        ('Perl',2),
        ('Ruby',3),
        ('Lua',4)]
    v=IntVar()
    for lang,n in L:
        b=Radiobutton(group,text=lang,bg='#fff',textvariable=v,value=n)
        b.pack(anchor=W)
    text.window_create(END,window=group)
    '''
    t=Entry(text)
    t.pack()
    text.window_create(END,window=t)
    text.insert(INSERT,'emm')
    

b1=Button(text,text='create Image',command=show)
text.insert(INSERT,'\n')
text.window_create(INSERT,window=b1)
text.insert(END,'I love FishC!')
text.mark_set('here','2.2')
text.mark_gravity('here','left')
text.insert('here','差')
text.insert('here','如')

text.tag_add('tag1','1.5','1.7','1.9')
text.tag_config('tag1',background='red',foreground='skyblue')
text.tag_config('tag2',foreground='yellow')
text.tag_lower('tag2')
text.insert(INSERT,'I love FishC',('tag2','tag1'))

text.insert(INSERT,'\nI love FishC')
text.tag_add('link','3.7','3.16')
text.tag_config('link',foreground='blue',underline=True)

def show_hand_cursor(event):
    text.config(cursor='arrow')

def show_arrow_cursor(event):
    text.config(cursor='xterm')

def click(event):
    soup=BeautifulSoup(urllib.request.urlopen('http://www.fishc.com').read().decode('utf-8'),'html.parser')
    text.insert(INSERT,'\n'+str(soup.link))

text.tag_bind('link','<Enter>',show_hand_cursor)
text.tag_bind('link','<Leave>',show_arrow_cursor)
text.tag_bind('link','<Button-1>',click)

#检查是否change
contents=text.get('1.0',END)
def getSig(contents):
    s=hashlib.md5(contents.encode())
    return s.digest()

print(getSig(contents))
s=getSig(contents)
def check():
    contents=text.get('1.0',END)
    if s!=getSig(contents):
        print('警告！内容发生了变化')
    else:
        print('风平浪静~')
Button(root,text='check',command=check).pack(side=LEFT)

#查找
def getIndex(text,index):
    return tuple(map(int,str.split(index,'.')))

start=1.0
while True:
    pos=text.search('o',start,stopindex=END)
    if not pos:
        break
    
    print('找到了啦，位置是:',getIndex(text,pos))
    start=pos+'+1c'
#撤销 undo=True edit_undo()实现 恢复用edit_redo()实现
def undo():
    text.edit_undo()
def separator(event):
    text.edit_separator()
text.bind('<Key>',separator)
Button(root,text='undo',command=undo).pack()
#text.insert('4.2','4')
#print(text.get('1.2','1.end'))
mainloop()
