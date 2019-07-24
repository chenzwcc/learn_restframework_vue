# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/5/31 下午9:57
from rest_framework import serializers

from goods.models import Goods, GoodsCategory, Banner


class CategorysSeralizer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorysSeralizer2(serializers.ModelSerializer):
    sub_cat = CategorysSeralizer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


# ModelSerializer类似Django中的ModelForm
class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorysSeralizer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = "__all__"


class BannerSerializer(serializers.Serializer):
    class Meta:
        model = Banner
        field = "__all__"