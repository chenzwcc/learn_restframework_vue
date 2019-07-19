# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/19 下午3:46

from rest_framework import generics
from django_filters import rest_framework as filters

from goods.models import Goods


class GoodsFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")  # 模糊查询name

    class Meta:
        model = Goods
        fields = ['min_price','max_price','name']
