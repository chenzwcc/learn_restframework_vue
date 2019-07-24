from django.db.models import Q
from django.shortcuts import render

# Create your views here.

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户认证
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        print('zizizizi',username,password)
        try:
            user = User.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None