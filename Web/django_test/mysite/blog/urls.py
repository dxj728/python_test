# --coding:utf-8--
# File: urls.py
# Author: dxj728
# Time: 2021年12月01日23时
# 说明：

'''urls.py 应用中的URL配置文件("URL.conf"),此文件并不像项目中的URL.conf那样会自动创建，根据需要进行手动创建此文件
'''
from django.urls import path, include
from . import views

urlpatterns = [
    path('hello_world', views.hello_world),
    path('content', views.article_content),
    path('index', views.get_index_page),
    # path('detail', views.get_detail_page),
    path('detail/<int:article_id>', views.get_detail_page),
]