from django.conf.urls import url
from django.contrib import admin
from api.views import UsersView, UserView, UserLoginView, UserViewSet, RegisterUser

urlpatterns = [

    url(r'^users/$', UsersView.as_view(), name='usersX'),
    url(r'^user/me/$', UserView.as_view(), name='me'),
    url(r'^login/(?P<pk>\d+)/$', UserLoginView.as_view(), name='login'),
    url(r'^user/$', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='users'),
    url(r'^register/$', RegisterUser.as_view(), name='register'),

]
