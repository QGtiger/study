from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import csv
from index.models import Product, Type
from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
import json
from .form import *


def weight_validate(value):
    if not str(value).isdigit():
        raise ValidationError('请输入正确的重量')


class ProductForm(forms.Form):
    name = forms.CharField(
        max_length=20,
        label=' 名字 ',
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'ip_name',
                'placeholder': 'Please input...'}),
        error_messages={
            'required': '名字不能为空'})
    weight = forms.CharField(
        max_length=50,
        label=' 重量 ',
        validators=[weight_validate])
    size = forms.CharField(max_length=50, label=' 尺寸 ')
    choice_list = [(i + 1, v['type_name'])
                   for i, v in enumerate(Type.objects.values('type_name'))]
    type = forms.ChoiceField(
        widget=forms.widgets.Select(
            attrs={
                'class': 'type',
                'size': '1'}),
        choices=choice_list,
        label=' 产品类型 ')

# Create your views here.


def index(request):
    type_list = Type.objects.values('type_name', 'id').distinct()
    # print(request.user)
    name_list = Product.objects.values('name', 'type_id')
    # content = {'title': '首页', 'type_list': type_list, 'name_list': name_list}
    form = ProductForm()
    if request.method == 'GET':

        return render(request, 'app_index.html', locals(), status=200)
    else:
        product = ProductForm(request.POST)
        if product.is_valid():  # 获取网页数据
            # 方法一 name = product['name']
            # 方法二
            name = product.cleaned_data['name']
            weight = product.cleaned_data['weight']
            size = product.cleaned_data['size']
            type = product.cleaned_data['type']
            Product.objects.create(
                name=name,
                weight=weight + 'g',
                size=size,
                type_id=type)
            return HttpResponse('提交成功')
        else:
            error_msg = product.errors.as_json()
            json_error = json.loads(error_msg)

            error = {'error': json_error['weight'][0]['message']}
            print(json_error['weight'][0]['message'])
            return render(request, 'app_index.html', locals(), status=200)


def model_index(request, id):
    if request.method == 'GET':
        instance = Product.objects.filter(id=id)
        # 判断数据是否存在
        if instance:
            # 相当于对表单数据的初始化
            product = ProductModelForm(instance=instance[0])
        else:
            # 也是对表单数据的初始化
            product = ProductModelForm(initial={'name':'我的手机'})
        return render(request, 'data_form.html', locals())
    else:
        product = ProductModelForm(request.POST)
        if product.is_valid():
            # 获取weight的数据，并通过clean_weight进行数据清洗，转换成Python数据类型
            weight = product.cleaned_data['weight']
            # 数据保存方法一
            # 直接将数据保存到数据库
            product.save()
            # 数据库保存方法二
            # save 设置commit = False，讲生成数据库对象product_db，然后对该对象的属性值修改保存
            # product_db = product.save(commit=False)
            # product_db.name = '我的iPone'
            # product_db.save()
            # 数据保存方法三
            # save_m2m() 方法用于保存ManyToMany的数据模型
            # product.save_m2m()
            return HttpResponse('提交成功！ weight清洗后的数据为：' + weight)
        else:
            error_msg = product.errors.as_json()
            print(error_msg)
            return render(request, 'data_form.html', locals())


def mydate(request, year, month, day):
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day))


def myyear(request, year, month):
    return render(request, 'app_index.html', {'month': month})


def download(request):
    res = HttpResponse(content_type='text/csv')
    #res = HttpResponse(content_type='image/jpg')
    res['Content-Disposition'] = 'attachment; filename="Yoona.csv"'
    writer = csv.writer(res)
    writer.writerow(['First row', 'A', 'B', 'C'])
    return res


def login(request):
    if request.method == 'Post':
        name = request.POST.get('name')
        return redirect('/')
    else:
        if request.GET.get('name'):
            name = request.GET.get('name')
        else:
            name = 'Everyone'
        return HttpResponse('user is ' + name)
