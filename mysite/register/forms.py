from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    #would be smarter to use 'django_widget_tweaks' but this works
    #force the basic forms to use bootstrap forms instead
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Email"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Last Name"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Username"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Confirm Password"}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
   

        