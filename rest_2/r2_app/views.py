from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from r2_app.forms import LoginForm, RegisterUserForm


# Create your views here.


class RegisterUserView(View):
    def get(self, request):
        ctx = {
            'form': RegisterUserForm,
        }
        return render(request, 'register_user_form.html', ctx)

    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password'],
                                            email=form.cleaned_data['email'])
            return HttpResponse('New user: {}'.format(user.username))
        ctx = {
            'form': form,
        }
        return render(request, 'register_user_form.html', ctx)


class UserLoginView(View):
    def get(self, request):
        ctx = {
            'form': LoginForm,
        }
        return render(request, 'login_form.html', ctx)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            #todo https://stackoverflow.com/questions/37332190/django-login-with-email
            user = User.objects.get(email=email) # to zle
            password = form.cleaned_data['password']
            user = authenticate(username=user.username, password=password)
            if user:
                login(request, user)
                return HttpResponse("Hello: {}".format(user.username))

            form.add_error(field=None, error='Bad login or password')

        ctx = {
            'form': form,
        }
        return render(request, 'login_form.html', ctx)


class UserView(ListView):
    model = User
    template_name = 'user_list.html'


class LoggedUserView(View):
    def get(self, request):
        logged_user = request.user
        print(logged_user.username)
        ctx = {
            'logged_user': logged_user,
        }
        return render(request, 'me.html', ctx)

