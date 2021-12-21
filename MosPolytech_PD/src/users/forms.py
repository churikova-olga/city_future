from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from users.models import UserProfile


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-12 input1'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'col-12  input1'}))

    class Meta:
        model = UserProfile
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-12 input1'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'col-12 input1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'col-12 input1'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-12 input1'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-12 input1'}))
    mobile = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'col-12 input1'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'col-12 input1'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-12 input1'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-12 input1'}))

    class Meta:
        model = UserProfile
        fields = ('first_name', 'password1', 'password2', 'last_name', 'username', 'mobile', 'email', 'address', 'city')

class AdministrationRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-12 input1'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'col-12 input1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'col-12 input1'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-12 input1'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-12 input1'}))
    mobile = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'col-12 input1'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'col-12 input1'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-12 input1'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-12 input1'}))
    role = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-12 input1'}))
    organization = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-12 input1'}))

    class Meta:
        model = UserProfile
        fields = ('first_name', 'password1', 'password2', 'last_name', 'username', 'mobile', 'email', 'address', 'city',
                  'role', 'organization')