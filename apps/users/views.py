from random import choice, Random

from django.db.models import Q
from django.shortcuts import render

# Create your views here.

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins, authentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from rest_framework import permissions

from users.serializers import SendMsgSerializer, UserRegisterSerializer, UserDetailSeralizer
from utils.email_send import send_email
from utils.conf import DOMAIN_PREFIX
from users.models import VerifyCode

User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户认证
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class SendMsgViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    """
    邮箱验证码
    """
    serializer_class = SendMsgSerializer

    def generate_code(self):
        """
        生成四位字符验证码
        """
        str1 = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        length = len(chars) - 1
        random = Random()
        for i in range(4):
            str1 += chars[random.randint(0, length)]
        return str1

    # 重写了mixins.CreateModelMixin的create方法
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # 获取验证通过的email
        email = serializer.validated_data["email"]
        code = self.generate_code()
        # 想注册邮箱发送邮件
        send_status = send_email(email,DOMAIN_PREFIX,code)
        if send_status == 0:
            return Response({
                "email":"发送失败"
            },status=status.HTTP_400_BAD_REQUEST)
        else:
            code_recode = VerifyCode(code=code,email=email)
            code_recode.save()
            return Response({
                "email":email
            },status=status.HTTP_201_CREATED)


class UserViewSet(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    """
    create:
        创建用户
    retrieve:
        用户详情信息
    """
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication,authentication.SessionAuthentication)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        # 生成token的两个重要步骤，一是payload，二是encode
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)

        return Response(re_dict,status=status.HTTP_201_CREATED,headers=headers)

    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == 'create':
            return []
        return []

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializer
        return UserDetailSeralizer

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()
