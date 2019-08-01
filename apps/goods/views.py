
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from goods.custom_filter import GoodsFilter
from .models import Goods, GoodsCategory, Banner
from .serializers import GoodsSerializer, CategorySerializer, BannerSerializer
from .custom_pagin import GoodsPagination

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class GoodsListViewSet(ListModelMixin,RetrieveModelMixin,GenericViewSet):
    """
    list:
        商品列表，分页，搜索，过滤，排序
    retrieve:
        查看商品详情
    """
    queryset = Goods.objects.all().order_by('id')
    pagination_class = GoodsPagination  # 分页
    filter_backends = (filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend)
    filter_class = GoodsFilter
    ordering_fields = ['sold_num','shop_price']
    search_fields = ['name', 'goods_brief', 'goods_desc']
    serializer_class = GoodsSerializer


class GoodsCategoryViewSet(ListModelMixin,RetrieveModelMixin,GenericViewSet):
    """
    商品分类列表
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class BannerViewSet(ListModelMixin,GenericViewSet):
    queryset = Banner.objects.all().order_by('index')
    serializer_class = BannerSerializer