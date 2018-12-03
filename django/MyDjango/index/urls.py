from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index),
    #path('<year>/<month>/<day>',views.mydate)
    re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html',views.mydate),
    re_path('(?P<year>[0-9]{4}).html',views.myyear,{'month':[6,7,8]},name = 'myyear'),
    path('download.html',views.download),
    path('login',views.login),
    path('<int:id>.html',views.model_index)
]
