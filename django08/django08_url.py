# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 14:28
# @File    : django08_url.py
from django.urls import path, re_path
from django08 import views


app_name = 'django08'


urlpatterns = [
    path('', views.index, name="django08_home"),
    re_path(r'^(?P<pid>\d+)/(?P<del_pass>\w+)/$', views.index, name="django08_home_delete"),
    path('list/', views.listing, name="django08_list"),
    path('post/', views.posting, name="django08_post"),
    path('contact/', views.contact, name="django08_contact"),
    path('post2db/', views.post2db, name="django08_post2db"),


]
