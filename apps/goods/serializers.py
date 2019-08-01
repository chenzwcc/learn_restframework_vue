# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/5/31 下午9:57
from rest_framework import serializers

from goods.models import Goods, GoodsCategory, Banner, GoodsImage


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ('image',)


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
    # images是数据库中设置的related_name="images"，把轮播图嵌套进来
    images = GoodsImageSerializer(many=True)
    class Meta:
        model = Goods
        fields = "__all__"


class BannerSerializer(serializers.Serializer):
    class Meta:
        model = Banner
        field = "__all__"