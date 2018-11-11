"""
author:lightfish
Time:2018.11.7
note:pyecharts的学习
"""
import numpy as np
from pyecharts import Pie,Page

page = Page()

attr=['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
v1=[np.random.randint(10,20) for _ in range(6)]
v2=[np.random.randint(10,20) for _ in range(6)]

#title_pos 标题位置  title-color 标题颜色 page_title='网页标题栏的名称' title_top='bottom' 标题在下方
pie=Pie('饼状图-玫瑰图实例',title_pos='center',title_top='bottom',width=900)
pie.use_theme('dark')
#is_label_show 显示每个点的值 is_legend_show显示每个颜色的属性
# is_random为是否随即排列颜色列表（bool）
# radius为半径，第一个为内半径，第二个是外半径
# rosetype为是否展示成南丁格尔图:'radius' 圆心角展现数据半分比，半径展现数据大小;'area'圆心角相同，为通过半径展现数据大小(默认）
# label_text_size为调整标签字体大小
pie.add('商品A',attr,v1,center=[25,50],is_random=True,radius=[30,75],rosetype='radius')
pie.add('商品B',attr,v2,center=[75,50],is_random=True,radius=[30,75],rosetype='area',is_legend_show=True,is_label_show=True)

page.add(pie)

pie2 = Pie('各类电影中好片所占的比例','数据来自豆瓣',title_pos='center',title_top='bottom',width=900)
pie2.use_theme('dark')
pie2.add("",["剧情",""],[np.random.randint(10,30),np.random.randint(70,90)],center=[10,30],radius=[18,24],label_pos='center',is_label_show=True, label_text_color=None)
pie2.add("",["奇幻",""],[np.random.randint(10,30),np.random.randint(70,90)],center=[30,30],radius=[18,24],label_pos='center',is_label_show=True, label_text_color=None, legend_pos='left')
pie2.add("",["爱情",""],[np.random.randint(10,30),np.random.randint(70,90)],center=[50,30],radius=[18,24],label_pos='center',is_label_show=True, label_text_color=None)
pie2.add("",["惊悚",""],[np.random.randint(10,30),np.random.randint(70,90)],center=[70,30],radius=[18,24],label_pos='center',is_label_show=True, label_text_color=None)
pie2.add("",["冒险",""],[np.random.randint(10,30),np.random.randint(70,90)],center=[90,30],radius=[18,24],label_pos='center',is_label_show=True, label_text_color=None)
pie2.add("",["动作",""],[np.random.randint(10,30),np.random.randint(70,90)],center=[10,70],radius=[18,24],label_pos='center',is_label_show=True, label_text_color=None)
pie2.add("",["喜剧",""],[np.random.randint(10,30),np.random.randint(70,90)],center=[30,70],radius=[18,24],label_pos='center',is_label_show=True, label_text_color=None)
pie2.add("",["科幻",""],[np.random.randint(10,30),np.random.randint(70,90)],center=[50,70],radius=[18,24],label_pos='center',is_label_show=True, label_text_color=None)
pie2.add("",["悬疑",""],[np.random.randint(10,30),np.random.randint(70,90)],center=[70,70],radius=[18,24],label_pos='center',is_label_show=True, label_text_color=None)
#is_legend_show 是显示该颜色是哪种属性  legend_pos就是它的现实位置
pie2.add("",["犯罪",""],[np.random.randint(10,30),np.random.randint(70,90)],center=[90,70],radius=[18,24],label_pos='center',is_label_show=True, label_text_color=None, is_legend_show=True, legend_top="center")

page.add(pie2)
page.render(r'E:\python_project\pyecharts\ex4.html')
