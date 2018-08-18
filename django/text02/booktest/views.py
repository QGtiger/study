# -*- coding:utf-8 -*-
from datetime import date,datetime
from django.shortcuts import render,redirect
from booktest.models import BookInfo
from django.http import HttpResponse,request
from django.http.response import HttpResponse, HttpResponseRedirect
from django import forms


class BookForm(forms.Form):
    bookname=forms.CharField(label='书名',max_length=10,error_messages={'requierd':'书名不能为空!','invalid':'书名不能超过十个字符!'})


def index(request):
    books=BookInfo.objects.all()
    # BookInfo.objects.filter(btitle='玄天邪尊').delete()
    # BookInfo.objects.create(btitle='大主宰',bpub_date=date.today(),bread='88',sub_date=datetime.today())
    BookInfo.objects.order_by('sub_date')
    # BookInfo.objects.filter(id=16).delete()
    return render(request,'index.html',{'books':books})
    # print(type(books))
    # print(len(books))
    # str=' '
    # for i in range(len(books)):
    # 	str+=books[i].btitle+' '
    # return HttpResponse(str)

def addBook(request):
    books=BookInfo.objects.all()
    # book=BookInfo()
    # book.btitle='飞剑问道'
    # book.bpub_date=date.today()
    # book.sub_date=datetime.today()
    # book.save()
    # # return HttpResponse('ok')
    # # 重定向跳转到首页
    # return redirect('/index/')
    Method = request.method
    if Method=='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['bookname']
            try:
                addJudge = BookInfo.objects.filter(btitle=name).get()
                return render(request,'index.html',{'addJudge':addJudge})
            except:
                registAdd = BookInfo.objects.create(btitle=name,bpub_date=date.today(),sub_date=datetime.today())
                return render(request,'index.html',{'registAdd':registAdd,'name':name,'books':books})
        else:
            form = BookForm()
            return render(request,'index.html',{'form':form,'books':books,'Method': Method})


def delBook(request,bid):
    # 查询出图书
    b=BookInfo.objects.filter(id=bid)
    b.delete()
    return redirect('/index/')