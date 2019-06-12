# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/6/12 下午9:35
from rest_framework.pagination import PageNumberPagination

class GoodsPagination(PageNumberPagination):
    """
    自定义商品分页
    """
    page_size = 1

    # 指定每页多少个
    page_size_query_param = "page_size"

    #页码参数
    page_query_param = "page"

    #  最多显示多少页
    max_page_size = 100