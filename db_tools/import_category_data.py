# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/5/23 下午10:11

import os
import sys


pwd = os.path.dirname(os.path.abspath(__file__))

sys.path.append(pwd+'../')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MxShop.settings')

import django
django.setup()

from goods.models import GoodsCategory

from db_tools.data.category_data import row_data

for lev1_cat in row_data:
    instance1 = GoodsCategory()
    instance1.code = lev1_cat['code']
    instance1.name = lev1_cat['name']
    instance1.category_type = 1
    instance1.save()

    for lev2_cat in lev1_cat['sub_categorys']:
        instance2 = GoodsCategory()
        instance2.code = lev2_cat['code']
        instance2.name = lev2_cat['name']
        instance2.category_type = 2
        instance2.parent_category = instance1
        instance2.save()

        for lev3_cat in lev2_cat['sub_categorys']:
            instance3 = GoodsCategory()
            instance3.code = lev3_cat['code']
            instance3.name = lev3_cat['name']
            instance3.category_type = 3
            instance3.parent_category = instance2
            instance3.save()
