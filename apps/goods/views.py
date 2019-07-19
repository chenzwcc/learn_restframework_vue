import django_filters
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Goods
from .serializers import GoodsSerializer
from .custom_pagin import GoodsPagination

#class GoodsListView(APIView):
#    def get(self,request,format=None):
#        goods = Goods.objects.all()
#        goods_serializer = GoodsSerializer(goods,many=True)
#        return Response(goods_serializer.data)

from rest_framework.generics import ListAPIView


#class GoodsListView(ListAPIView):
#    """
#    商品列表
#    """
#    pagination_class = GoodsPagination  # 分页
#    queryset = Goods.objects.all()
#    serializer_class = GoodsSerializer

from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from goods.custom_filter import GoodsFilter

class GoodsListViewSet(ListModelMixin,GenericViewSet):
    queryset = Goods.objects.all()
    pagination_class = GoodsPagination  # 分页
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filter_fields = ('name',)
    filter_class = GoodsFilter
    serializer_class = GoodsSerializer