from django import forms
from django.core.exceptions import ValidationError

from r2_app.validators import validate_username


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput,)


class RegisterUserForm(forms.Form):
    username = forms.CharField(max_length=128, validators=[validate_username],)
    password = forms.CharField(widget=forms.PasswordInput,)
    password_c = forms.CharField(widget=forms.PasswordInput, label="Repeat password")
    email = forms.EmailField()

    def clean_password_c(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password_c']
        if password != password2:
            raise ValidationError("Passwords don't match")
        return password
