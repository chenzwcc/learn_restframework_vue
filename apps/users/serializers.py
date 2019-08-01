# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/7/24 下午9:12
import re
from datetime import datetime,timedelta

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

from users.models import VerifyCode

User = get_user_model()

EMAIL_REGEX = '^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'


class SendMsgSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100)

    def validate_email(self, email):
        """
        邮箱格式验证
        """
        if User.objects.filter(email=email).count():
            raise serializers.ValidationError("该邮箱已被注册")

        if not re.match(EMAIL_REGEX,email):
            raise serializers.ValidationError("该邮箱格式不正确")

        one_mintes = datetime.now()-timedelta(hours=0,minutes=1,seconds=0)

        if VerifyCode.objects.filter(add_time__gt=one_mintes,email=email).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return email


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    用户注册
    """
    # UserProfile中没有code字段，这里需要自定义一个code序列化字段
    code = serializers.CharField(required=True,write_only=True,max_length=4,min_length=4,label="验证码",
                                 error_messages={
                                    "blank": "请输入验证码",
                                    "required": "请输入验证码",
                                    "max_length": "验证码格式错误",
                                    "min_length": "验证码格式错误"
                                 })
    # 验证用户名是否存在
    username = serializers.CharField(label="用户名",required=True,
                                     allow_blank=False,validators=[UniqueValidator(queryset=User.objects.all(),message="用户已存在")])
    password = serializers.CharField(
        style={
            "input_type":"password",
        },
        label="密码",
        write_only=True
    )

    def validate_code(self,code):
        # 用户注册，已post方式提交注册信息，post的数据都保存在initial_data里面
        verify_code = VerifyCode.objects.filter(email=self.initial_data['username']).order_by("-add_time")
        if verify_code:
            last_verify_code = verify_code[0]
            five_mintes = datetime.now()-timedelta(hours=0,minutes=5,seconds=0)
            if five_mintes>last_verify_code.add_time:
                raise serializers.ValidationError("验证码过期")

            if last_verify_code.code != code:

                raise serializers.ValidationError("验证码错误")
        else:

            raise serializers.ValidationError("验证码错误")

    # 所有字段。attrs是字段验证合法之后返回的总的dict
    def validate(self, attrs):
        # print('attars',attrs) attars OrderedDict([('username', '3169664183@qq.com'), ('code', None), ('password', 'chenzwcc')])
        # 前段并没有传email，这里添加进来
        attrs["email"] = attrs["username"]
        # code是自己添加得，数据库中并没有这个字段，验证完就删除掉
        del attrs["code"]
        return attrs

    class Meta:
        model = User
        fields = ('username','code','email','password','mobile')


class UserDetailSeralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','gender','birthday','email','mobile')
