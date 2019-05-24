from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField


class GoodsCategory(models.Model):
    """
    商品多级分类
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )
    name = models.CharField(verbose_name="类别名", max_length=30, default="")
    code = models.CharField(verbose_name="类别code", max_length=30, default="")
    desc = models.TextField(verbose_name="商品类别描述", default="")
    category_type = models.IntegerField(verbose_name="商品类目级别", choices=CATEGORY_TYPE)
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, null=True,
                                        blank=True, verbose_name="父类目级别", related_name="sub_cat")
    is_tab = models.BooleanField(default=False, verbose_name="是否为导航拦")
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """
    某一大类下的宣传商标
    """
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, related_name='brands',
                                 null=True, blank=True, verbose_name="商品类目")
    name = models.CharField(verbose_name="品牌名", max_length=30, default="")
    desc = models.TextField(verbose_name="品牌描述", default="")
    image = models.ImageField(max_length=200, upload_to='brands/')
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "宣传品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    商品
    """
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name="商品类目")
    name = models.CharField(verbose_name="商品名称", max_length=100)
    goods_sn = models.CharField(verbose_name="商品唯一货号", max_length=50, default="")
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    sold_num = models.IntegerField(default=0, verbose_name="销售量")
    fav_num = models.IntegerField(default=0, verbose_name="被收藏数")
    goods_num = models.IntegerField(default=0, verbose_name="库存量")
    market_price = models.FloatField(default=0, verbose_name="市面价格")
    shop_price = models.FloatField(default=0, verbose_name="本店价格")
    goods_brief = models.TextField(max_length=500, verbose_name="商品简短描述")
    goods_desc = UEditorField(verbose_name=u"内容", imagePath="goods/images/", width=1000, height=300,
                              filePath="goods/files/", default='')
    ship_free = models.BooleanField(default=True, verbose_name="是否承担运费")
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="首页中展示的商品封面图")
    is_new = models.BooleanField(default=False, verbose_name="是否为新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否为热销品")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name="images", verbose_name="商品")
    image = models.ImageField(upload_to="", null=True, blank=True, verbose_name="图品")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """
    首页轮播的商品图，为适配首页大图
    """
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品")
    image = models.ImageField(upload_to='banner', verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "首页轮播"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class IndexAd(models.Model):
    """
    首页类别标签右边展示的七个商品广告
    """
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, related_name='category', verbose_name="商品类目")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name="goods")

    class Meta:
        verbose_name = "首页广告"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class HotSearchWords(models.Model):
    """
    搜索栏下的热搜词
    """
    keywords = models.CharField(default="", max_length=20, verbose_name="热搜词")
    index = models.IntegerField(default=0, verbose_name="排序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "热搜排行"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords
