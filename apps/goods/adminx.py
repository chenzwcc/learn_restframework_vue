# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/5/23 下午2:04

import xadmin

from goods.models import Goods, GoodsCategory, GoodsImage, GoodsCategoryBrand, Banner, HotSearchWords, IndexAd


class GoodsAdmin(object):
    list_display = ['name', 'click_num', 'sold_num', 'fav_num', 'goods_num', 'market_price', 'shop_price',
                    'goods_brief',
                    'goods_desc', 'is_new', 'is_hot', 'add_time']

    search_fields = ['name', ]

    list_editable = ['is_hot', 'is_new']

    list_filter = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                   "shop_price", "is_new", "is_hot", "add_time", "category__name"]

    style_fields = ['goods_desc', 'ueditor']


class GoodsCategoryAdmin(object):
    list_display = ["name", "category_type", "parent_category", "add_time"]
    list_filter = ["category_type", "parent_category", "name"]
    search_fields = ['name', ]


class GoodsBrandAdmin(object):
    list_display = ["category", "image", "name", "desc"]


class BannerGoodsAdmin(object):
    list_display = ['goods', 'image', 'index']


class IndexAdmin(object):
    list_dispaly = ['category', 'goods']


class HotSearchAdmin(object):
    list_display = ['keywords', 'index', 'add_time']


xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(GoodsCategoryBrand, GoodsBrandAdmin)
xadmin.site.register(Banner, BannerGoodsAdmin)
xadmin.site.register(IndexAd, IndexAdmin)
xadmin.site.register(HotSearchWords, HotSearchAdmin)
