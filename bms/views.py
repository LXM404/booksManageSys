# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index_view(request):
    # 退出登录
    return render(request, 'index.html')

def index1_view(request):
    return render(request, 'index1.html')


def login_view(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        pass


def uselect_view(request):
    return render(request,'uselect.html')


def user_view(request):
    return render(request,'user.html')


def borrow_view(request):
    return render(request,'borrow.html')


def query_view(request):
    return render(request,'query.html')

def query1_view(request):
    return render(request,'query1.html')


def register_view(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        pass


def addbook_view(request):
    return render(request,'addbook.html')


def usermanage_view(request):
    return render(request,'usermanage.html')


def stuindex_view(request):
    return render(request,'stuindex.html')


def stuuselect_view(request):
    return render(request,'stuuselect.html')


def stuindex1_view(request):
    return render(request,'stuindex1.html')


def stuquery_view(request):
    return render(request,'stuquery.html')


def stuquery1_view(request):
    return render(request,'stuquery1.html')


def stuuser_view(request):
    return render(request,'stuuser.html')


def stuborrow_view(request):
    return render(request,'stuborrow.html')


def stulogin_view(request):
    return render(request,'stulogin.html')


def sturegister_view(request):
    return render(request,'sturegister.html')