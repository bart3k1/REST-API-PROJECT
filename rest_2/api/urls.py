from django.conf.urls import url
from django.contrib import admin
from api.views import UsersView, UserView, UserLoginView, UserViewSet

urlpatterns = [

    url(r'^users/$', UsersView.as_view(), name='usersX'),
    url(r'^userOLD/$', UserView.as_view(), name='user'),
    url(r'^login/(?P<pk>\d+)/$', UserLoginView.as_view(), name='login'),
    url(r'^user/$', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='users'),

]
