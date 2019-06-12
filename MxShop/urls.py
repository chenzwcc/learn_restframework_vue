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
import xadmin
from django.urls import path,include, re_path
from django.views.static import serve
from MxShop.settings import MEDIA_ROOT
from rest_framework.documentation import include_docs_urls

#from goods.views import GoodsListView
from rest_framework.routers import DefaultRouter
from goods.views import GoodsListViewSet

router = DefaultRouter()
# 配置goods的URL
router.register(r'goods',GoodsListViewSet)

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    path('docs/',include_docs_urls(title="Api文档")),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),

#    path('goods/',GoodsListView.as_view())
    re_path('^',include(router.urls))
]
