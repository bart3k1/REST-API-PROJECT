from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import UsersSerializer, UserSerializer, UserOLDSerializer  # GuestSerializer, UserGetSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

# Create your views here.
# from cms_body.models import Guest

# User = get_user_model()


class UsersView(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UsersSerializer(users, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        pass


class UserView(APIView):
    def get(self, request, format=None):
        user = request.user
        token, created = Token.objects.get_or_create(user=user)
        # serializer = UsersSerializer(user, context={"request": request})
        return Response({
            'user_id': user.id,
            'email': user.email,
            'token': token.key,
        })
        # return Response(serializer.data)


class UserLoginView(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk=pk)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user_id': user.id,
            'email': user.email,
            'token': token.key,
            })


# class GuestsView(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'guests_list.html'
#
#     def get(self, request, format=None):
#         serializer = GuestSerializer()
#         return Response({'serializer': serializer})
#
#     def post(self, request, format=None):
#         serializer = GuestSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response({'serializer': serializer})

#
# class GuestViewSet(ModelViewSet):
#     queryset = Guest.objects.all()
#     serializer_class = GuestSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    # serializer_class = UserSerializer
    serializer_class = UserOLDSerializer

    # def get_serializer_class(self):
    #     if self.request.user.is_staff:
    #         return UserGetSerializer
    #     return UserSerializer
        # if self.request.method.post:
        #     return UserGetSerializer
        # return UserSerializer
