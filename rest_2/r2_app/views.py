from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from r2_app.forms import LoginForm, RegisterUserForm

User = get_user_model()

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
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
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
        ctx = {
            'logged_user': logged_user,
        }
        return render(request, 'me.html', ctx)

