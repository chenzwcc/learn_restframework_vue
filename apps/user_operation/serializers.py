# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/26 上午9:51
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from user_operation.models import UserFav, UserLeavingMessage, UserAddress
from goods.serializers import GoodsSerializer


class UserFavSerializer(serializers.ModelSerializer):
    # 获取当前用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user','goods'),
                message="已经收藏"
            )
        ]
        model = UserFav
        fields = ("user","goods","id")


class UserFavDetailSerializer(serializers.ModelSerializer):
    """
    用户收藏详情
    """
    goods = GoodsSerializer()

    class Meta:
        model = UserFav
        fields = ("goods","id")


class LeavingMessageSerializer(serializers.ModelSerializer):
    """
    用户留言信息
    """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True,format="%Y-%m-%d %H:%M")
    class Meta:
        model = UserLeavingMessage
        fields = ("user","message_type","subject","message","file","id","add_time")


class UserAddressSerializer(serializers.ModelSerializer):
    """
    用户收货地址信息
    """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    province = serializers.CharField(max_length=100,required=True,help_text='省份')
    city = serializers.CharField(max_length=100,required=True,help_text='城市')
    district = serializers.CharField(max_length=100,required=True,help_text='区域')
    address = serializers.CharField(max_length=100,required=True,help_text='详细地址')
    signer_name = serializers.CharField(max_length=100,required=True,help_text='签收人')
    signer_mobile = serializers.CharField(max_length=11,required=True,help_text='签收人电话')
    add_time = serializers.DateTimeField(read_only=True,format="%Y-%m-%d %H:%M")

    class Meta:
        model = UserAddress
        fields = ("user","province","city","district","address","signer_name","signer_mobile","add_time","id")