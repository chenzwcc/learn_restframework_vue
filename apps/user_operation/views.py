from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from user_operation.serializers import UserFavSerializer, UserFavDetailSerializer, LeavingMessageSerializer, UserAddressSerializer
from rest_framework import viewsets,mixins
from user_operation.models import UserFav, UserLeavingMessage, UserAddress
from utils.custom_permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


class UserFavViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    用户收藏
    """
    serializer_class = UserFavSerializer
    # queryset = UserFav.objects.all() # 因为在serializer中只能对本用户进行用户收藏操作，所以queryset需要改写成下面的get_queryset方式获取
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)

    lookup_field = 'goods_id'

    def get_serializer_class(self):
        if self.action == "list":
            return UserFavDetailSerializer
        else:
            return UserFavSerializer

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)


class LeaveMessageViewSet(mixins.ListModelMixin,mixins.DestroyModelMixin,mixins.CreateModelMixin,viewsets.GenericViewSet):
    """
    list:获取用户的所有留言信息
    delete:删除用户留言信息
    create:创建留言信息
    """
    serializer_class = LeavingMessageSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        return UserLeavingMessage.objects.filter(user=self.request.user)


class UserAddressViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    serializer_class = UserAddressSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)
