# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/29 上午10:58

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """

    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user