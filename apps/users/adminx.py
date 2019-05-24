# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/5/23 下午1:20

import xadmin
from xadmin import views

from .models import VerifyCode


class BaseSetting(object):
    """
    添加主题
    """
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    """
    全剧配置，后台管理标题和页脚
    """
    site_title = "MxShop电商平台"
    site_footer = "版权所有"

    # 菜单收缩
    menu_style = "accordion"


class VerifyCodeXadmin(object):
    list_display = ['code', 'mobile', 'add_time']


xadmin.site.register(VerifyCode,VerifyCodeXadmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)