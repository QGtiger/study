from django import forms
from .models import *
from django.core.exceptions import ValidationError


class ProductModelForm(forms.ModelForm):
    # 重写ProductModelForm类的初始化函数
    def __init__(self, *args, **kwargs):
        super(ProductModelForm, self).__init__(*args, **kwargs)
        # 设置下拉框
        type_obj = Type.objects.values('type_name')
        choice_list = [(i+1, v['type_name']) for i,v in enumerate(type_obj)]
        self.fields['type'].choices = choice_list
        # 初始化字段name
        self.fields['name'].initial = '我的手机'

    # 添加模型外的表单字段
    productId = forms.CharField(max_length=20, label='产品序列', initial='No1')
    # 模型和表单的设置

    class Meta:
        # 绑定模型：
        model = Product
        # fields属性用于设置转换字段，'__all__'是将全部模型字段转换成表单字段
        # fields = '__all__'
        fields = ['name', 'weight', 'size', 'type']
        # exclude 用于禁止模型字段转换成表单字段
        exclude = []
        # labels 设置HTML元素控件的label
        labels = {
            'name': '产品名称',
            'weight': ' 重量 ',
            'size': ' 尺寸 ',
            'type': ' 产品类型 '
        }
        # 定义widgets,设置表单字段的CSS样式
        widgets = {
            'name': forms.widgets.TextInput(
                attrs={
                    'class': 'ip_name',
                    'placeholder': 'Please input...'}),
        }
        # 定义字段的类型，一般情况下模型的字段会自动转换成表单字段
        field_classes = {
            'name': forms.CharField
        }
        # 帮助提示信息
        help_texts = {
            'name': '',
        }
        # 自定义错误信息
        error_message = {
            # '__all__' 设置全部错误信息
            '__all__': {'required': '请输入内容',
                        'invalid': '请检查输入的内容'},
            # 设置某个字段的错误信息
            'weight': {'required': '请输入重量数值',
                       'invalid': '请检查数值是否正确'}

        }
    # 自定义表单字段weight的数据清洗

    def clean_weight(self):
        data = self.cleaned_data['weight']
        return data + 'g'
