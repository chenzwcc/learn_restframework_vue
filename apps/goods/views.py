
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Goods, GoodsCategory
from .serializers import GoodsSerializer, CategorySerializer
from .custom_pagin import GoodsPagination

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from rest_framework import filters

class GoodsListViewSet(ListModelMixin,GenericViewSet):
    queryset = Goods.objects.all()
    pagination_class = GoodsPagination  # 分页
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('name',)
    serializer_class = GoodsSerializer


class GoodsCategoryViewSet(ListModelMixin,RetrieveModelMixin,GenericViewSet):
    """
    商品分类列表
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer