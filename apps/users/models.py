from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    用户信息
    """
    name = models.CharField("姓名", max_length=30, null=True, blank=True)
    birthday = models.DateField("出生日期", null=True, blank=True)
    mobile = models.CharField("手机号码", max_length=11)
    gender = models.CharField("性别", choices=(("male", "男"), ("female", "女")), default="female")
    email = models.EmailField("邮箱", max_length=100, null=True, blank=True)
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField("验证码", max_length=10)
    mobile = models.CharField("手机号码", max_length=11)
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
