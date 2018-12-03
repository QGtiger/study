# index的admin文件
# 修改title和header
from django.contrib import admin
from .models import *

# Register your models here.
# 一：直接将模型注册到admin后台
# admin.site.register(Product)
# admin.site.register(Type)

# 修改title和header
admin.site.site_header = 'MyDjango'
admin.site.site_title = 'MyDjango 后台管理'


# 二：自定义ProductAdmin类并集成ModelAdmin
# 注册方法一，使用Python装饰器讲ProductAdmin和模型Product绑定并注册到后台
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # 设置显示的字段
    list_display = ['id','name','weight','size','type',]
    list_display.append('colored_type')
    # 设置可搜索的字段并在Admin后台数据生成搜索框，如有外键，因使用双下划线连接两个模型地方字段
    search_fields = ['id', 'name', 'type__type_name']
    # 设置过滤器，在后台数据的右侧生成导航栏，如有外键，因使用双下划线连接两个模型的字段
    list_filter = ['name', 'type__type_name']
    # 设置排序方式,['id']为升序，降序为['-id']
    ordering = ['id']
    # 设置时间选择器，如字段中有时间格式才可以使用
    # date_hierarchy = Field
    # 添加新数据时，设置可添加数据的字段
    fields = ['name', 'weight', 'size', 'type']
    # 设置可读字段，在修改或新增数据时使其无法设置
    readonly_fields = ['name']
    # 重写get_readonly_fields()函数，设设置超级用户和普通用户 的权限
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = []
        return self.readonly_fields
    def get_queryset(self, request):
        qs = super(ProductAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(id__lt=6)

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_name']

# 注册方法二
# admin.site.register(Product, ProductAdmin)