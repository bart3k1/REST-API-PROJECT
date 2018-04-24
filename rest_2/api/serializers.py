from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from rest_framework import serializers

User = get_user_model()

# Create your views here.


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password':
                            {'write_only': True}
                        }

    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        password = data['password']
        if not email:
            raise ValidationError("No such user")
        user = User.objects.filter(email=email)
        if user.exists():
            user_obj = user.first()
        else:
            raise ValidationError("Email not valid")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect data")
        return data
