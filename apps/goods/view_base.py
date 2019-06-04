# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/5/24 上午11:16

from django.http.response import JsonResponse
from django.views.generic.base import View

from goods.models import Goods


class GoodsListView(View):
    def get(self,request):
        json_list = []
        goods = Goods.objects.all()
        for good in goods:
            json_dict = {}
            json_dict['name'] = good.name
            json_dict['category'] = good.category.name
            json_dict['market_price'] = good.market_price
            json_list.append(json_dict)

        return JsonResponse(json_list,safe=False)