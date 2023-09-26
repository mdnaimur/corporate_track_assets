from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, fields

from .models import User

# ? Custom User from class making


class MyUserFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
