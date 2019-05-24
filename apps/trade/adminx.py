# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/5/23 下午2:21

import xadmin
from .models import ShoppingCart, OrderGoods, OrderInfo


class ShoppingCartAdmin(object):
    list_display = ['user', 'goods', 'nums', ]


class OrderInfoAdmin(object):
    list_display = ["user", "order_sn", "trade_no", "pay_status", "post_script", "order_mount",
                    "order_mount", "pay_time", "add_time"]


xadmin.site.register(ShoppingCart, ShoppingCartAdmin)
xadmin.site.register(OrderInfo, OrderInfoAdmin)
