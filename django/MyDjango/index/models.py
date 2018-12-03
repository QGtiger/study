from django.db import models
from django.utils.html import format_html
# Create your models here.
class Type(models.Model):
    id = models.AutoField(' 序号 ', primary_key=True)
    type_name = models.CharField(' 产品类型 ', max_length=20)
    # 设置返回值，若不设置，则默认返回Type对象
    # 如果存在多个下拉框，需要重写初始化函数__init__()
    def __str__(self):
        return self.type_name



# 设置中文
# 设置字段中文名，用于admin后天显示
class Product(models.Model):
    id = models.AutoField(' 序号 ', primary_key=True)
    name = models.CharField(' 名称 ', max_length=50)
    weight = models.CharField(' 重量 ', max_length=20)
    size = models.CharField(' 尺寸 ', max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name=' 产品类型 ')
    class Meta:
        # 设置verbose_name，在Admin会显示为'产品信息s'
        verbose_name = '产品信息'
        verbose_name_plural = '产品信息'

    # 自定义函数，设置字体颜色
    def colored_type(self):
        if '手机' in self.type.type_name:
            color_code = 'red'
        elif '平板电脑' in self.type.type_name:
            color_code = 'blue'
        elif '智能穿戴' in self.type.type_name:
            color_code = 'green'
        else:
            color_code = 'yellow'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            self.type
        )

    # 设置Admin标题
    colored_type.short_description = '带颜色的产品类型'