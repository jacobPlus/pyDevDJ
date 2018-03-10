# -*- coding: utf-8 -*-
'''
Created on 2018年3月2日

@author: jacob
'''
 
from django.http import HttpResponse
 
from myApp.models import myTable

def mytbOp(request):
    myitem = myTable(name='runoob')
    myitem.save()
    return HttpResponse("<p>add my data !</p>")