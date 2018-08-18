# -*- coding: GBK -*-
from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=50, unique=True)
    bpub_date = models.DateField()
    sub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    idDelete = models.BooleanField(default=False)


class HeroInfo(models.Model):
    hname=models.CharField(max_length=50,unique=False)
    hgender=models.BooleanField(default=False)
    isDelete=models.BooleanField(default=False)
    hcontent=models.CharField(max_length=500)
    #hbook=models.ForeignKey('BookInfo',on_delete=models.CASCADE)