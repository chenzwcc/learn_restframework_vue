# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/5/23 下午2:26

import xadmin
from .models import UserFav, UserAddress, UserLeavingMessage


class UserFavAdmin(object):
    list_display = ['user', 'goods', 'add_time']


class UserAddressAdmin(object):
    list_display = ['signer_name', 'signer_mobile', 'district', 'address']


class UserLeaveAdmin(object):
    list_display = ['user', 'message_type', "message", "add_time"]


xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserAddress, UserAddressAdmin)
xadmin.site.register(UserLeavingMessage, UserLeaveAdmin)
