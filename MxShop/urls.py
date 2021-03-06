"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from django.urls import path,include, re_path
from django.views.static import serve
from MxShop.settings import MEDIA_ROOT
from rest_framework.documentation import include_docs_urls

#from goods.views import GoodsListView
from rest_framework.routers import DefaultRouter
from goods.views import GoodsListViewSet, GoodsCategoryViewSet, BannerViewSet
from users.views import SendMsgViewSet, UserViewSet
from user_operation.views import UserFavViewSet, LeaveMessageViewSet,UserAddressViewSet

router = DefaultRouter()
# 配置goods的URL
router.register(r'goods',GoodsListViewSet, base_name="goods")
router.register(r'categorys', GoodsCategoryViewSet, base_name="categorys")
router.register(r'banners',BannerViewSet,base_name='banners')
router.register(r'code',SendMsgViewSet,base_name='code')
router.register(r'users',UserViewSet,base_name='users')
router.register(r'userfavs',UserFavViewSet,base_name='userfavs')
router.register(r'messages',LeaveMessageViewSet,base_name='messages')
router.register(r'address',UserAddressViewSet,base_name='address')

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    path('docs/',include_docs_urls(title="Api文档")),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('login/',obtain_jwt_token),

#    path('goods/',GoodsListView.as_view())
    re_path('^',include(router.urls))
]
