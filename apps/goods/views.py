
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Goods
from .serializers import GoodsSerializer
from .custom_pagin import GoodsPagination

from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from rest_framework import filters

class GoodsListViewSet(ListModelMixin,GenericViewSet):
    queryset = Goods.objects.all()
    pagination_class = GoodsPagination  # 分页
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('name',)
    serializer_class = GoodsSerializer