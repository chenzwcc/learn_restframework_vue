# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/5/31 下午9:22

from django.urls import path

from .view_base import GoodsListView

urlpatterns = [
    path('good_list',GoodsListView.as_view(),)
]
