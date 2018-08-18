import re

from django import forms
from django.http import request, response
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.forms import widgets
# Create your views here.
from register_login.models import User

TOPIC_CHOICES = (
  ('leve1', '差评'),
  ('leve2', '中评'),
  ('leve3', '好评'),
)
#用户信息form类
class UserForm(forms.Form):
    name = forms.CharField(label='用户名',widget=forms.TextInput(attrs={'placeholder':u'请输入用户名','style':'position: relative'}), max_length=10, error_messages={'required': '用户名不能为空', 'invalid': "用户名不能超过10位字符"})
    pwd = forms.CharField(label='密  码',widget=forms.TextInput(attrs={'placeholder':u'请输入密码','style':'position: relative'}),  max_length=15, error_messages={'required': '密码不能为空', 'invalid': '密码不能超过15字符'})
    topic = forms.ChoiceField(choices=TOPIC_CHOICES,label='选择评分')
    # test = forms.CharField(max_length=128)


def regist(request):
    Method = request.method
    if Method=='POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['name']
            password = uf.cleaned_data['pwd']
            pattern = re.compile('[^\\w-]')
            t=re.findall('.*?([\u4E00-\u9FA5])',username)
            if  re.findall(pattern, username):
                return render(request, 'regist.html', {'uf': uf, 'registError': "用户名只能是字母,数字,下划线或者'-'组成"})
            elif t:
                return render(request, 'regist.html', {'uf': uf, 'registError': "用户名只能是字母,数字,下划线或者'-'组成"})

            try:
                registJudge = User.objects.filter(name=username).get()
                return render(request, 'regist.html', {'registJudge': registJudge})
            except :
                registAdd = User.objects.create(name=username, pwd=password)
                return render(request, 'regist.html', {'registAdd': registAdd, 'name': username})
    else:
        uf = UserForm()
        return render(request, 'regist.html', {'uf': uf, 'Method': Method})

def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['name']
            password = uf.cleaned_data['pwd']
            #对比输入的用户名和密码和数据库中是否一致
            userPassJudge = User.objects.filter(name=username, pwd=password)

            if userPassJudge:
                response = HttpResponseRedirect('/index/')
                response.set_cookie('cookie_username', username, 300)
                return response
            else:
                return render(request, 'login.html', {'uf': uf, 'error': "用户名或密码错误"})
    else:
        uf = UserForm()
        return render(request, 'login.html', {'uf': uf})


def index(request):
    username = request.COOKIES.get('cookie_username', '')
    return render(request, 'index.html', {'username': username})

def logout(request):
    response = HttpResponseRedirect('/index/')
    response.delete_cookie('cookie_username')
    return response