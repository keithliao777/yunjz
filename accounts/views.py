# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    username = "keithliao"
    return render(request,"accounts/index.html",{"username":username})


def register(request):
    if request.method=="POST":
        HttpResponseRedirect("accounts/index")
    return render(request,"accounts/register.html")

def login(request):
    template_var = {}
    if request.method=="POST":
        username = request.POST.get("username")
        template_var = {"error":"must first register","username":username}
    return render(request,"accounts/login.html",template_var)

def logout(request):
    return render(request,"accounts/logout.html")