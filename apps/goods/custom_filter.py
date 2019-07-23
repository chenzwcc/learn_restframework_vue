# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/19 下午3:46
from django.db.models import Q
from rest_framework import generics
from django_filters import rest_framework as filters

from goods.models import Goods


class GoodsFilter(filters.FilterSet):
    pricemin = filters.NumberFilter(name="shop_price", lookup_expr='gte')
    pricemax = filters.NumberFilter(name="shop_price", lookup_expr='lte')
    top_category = filters.NumberFilter(name="category", mathod="top_category_filter")

    def top_category_filter(self,queryset,name,value):
        # 不管当前点击的是一级分类二级分类还是三级分类，都能找到。
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin','pricemax']
