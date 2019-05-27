#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------------------
    Creator : 汪春旺
       Date : 2019-05-25
    Project : myblog
   FileName : urls.py
Description : 
-------------------------------------------------------------
"""
from django.urls import path
from blogapp.views import *

app_name = 'blogapp'

urlpatterns = [
    # 首页
    path('', IndexView.as_view(), name='index'),
    # 文章分类菜单，显示该分类下所有文章列表
    path('<str:catecode>/', ArticalListView.as_view(), name='article_list'),
    # 文章详情
    path('<str:catecode>/<int:pk>/', ArticalDetailView.as_view(), name='article_detail'),
    # 标签
    path('tag/<str:tagcode>/', TagView.as_view(), name='tag_article_list'),
    # 搜索关键字
    path('<str:catecode>/search/', SearchView.as_view(), name='search'),
]


