from django.conf.urls import url

from api.views import LoginUser, RegisterUser, UsersView, UserView

urlpatterns = [

    url(r'^users/$', UsersView.as_view(), name='usersX'),
    url(r'^users/me/$', UserView.as_view(), name='me'),
    url(r'^register/$', RegisterUser.as_view(), name='register'),
    url(r'^login/$', LoginUser.as_view(), name='login'),

]
