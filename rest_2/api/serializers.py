# from cms.cms_body.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model
# from cms_body.models import Guest
from django.contrib.auth.models import User

# Create your views here.


User = get_user_model()


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserOLDSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'token']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "email", "password"]
        # fields = '__all__'






class UserGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["first_name", "last_name"]

#
# class GuestSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Guest
#         fields = ["id", "name", "surname", "phone", "alt_phone", "notes", "ocena"]
