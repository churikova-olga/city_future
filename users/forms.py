from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import UserProfile


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'password1', 'password2', 'last_name', 'username', 'mobile', 'email', 'address', 'city',
                  'role', 'organization', 'is_administration')