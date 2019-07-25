# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/24 下午9:48
from users.models import VerifyCode
from django.core.mail import send_mail
from MxShop.settings import EMAIL_FROM

def send_email(email,host,code):
    email_title = "商城注册验证码"
    email_body= "验证码为:{0},有效期为五分钟。".format(code)

    send_status = send_mail(email_title,email_body,EMAIL_FROM,[email])
    return send_status
