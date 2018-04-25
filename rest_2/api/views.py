from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import (LoginUserSerializer, RegisterUserSerializer,
                             UserSerializer, UsersSerializer, NewRegisterUserSerializer)

User = get_user_model()


class NewUserRegister(APIView):
    serializer_class = NewRegisterUserSerializer
    permission_classes = (AllowAny,)
    """
    Creates the user.
    """
    def post(self, request, format=None):
        serializer = NewRegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response({'token': token.key}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterUser(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            token, created = Token.objects.get_or_create(user=serializer.instance)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginUserSerializer

    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = User.objects.get(email=serializer.data['email'])
            token, created = Token.objects.get_or_create(user=user)
            serializer.data['token'] = token.key
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UsersSerializer(users, many=True, context={"request": request})
        return Response(serializer.data)


class UserView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        user = request.user
        serializer = UserSerializer(user, context={"request": request})
        return Response(serializer.data)
