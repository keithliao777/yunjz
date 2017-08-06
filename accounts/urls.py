#-*- coding:utf-8 -*-
__author__ = 'keithliao'


from django.conf.urls import url,include
from django.contrib import admin
from accounts import views

admin.autodiscover()


urlpatterns = [
    url(r'^/$', views.login,name='login'),
    url(r'^login/$', views.login,name='login'),
    url(r'^logout/$', views.logout,name='logout'),
    url(r'^register/$', views.register,name = 'register')
]

