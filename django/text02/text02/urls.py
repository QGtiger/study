from booktest import views
from django.contrib import admin
from django.conf.urls import url

urlpatterns=[
    url(r'^admin/', admin.site.urls),
    url(r'^index/$',views.index),
    url(r'^addBook/$',views.addBook),
    url(r'^delBook/(\d+)/$',views.delBook)
]