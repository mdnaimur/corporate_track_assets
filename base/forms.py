from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, fields

from .models import User, Product_Assets, Employee

# ? Custom User from class making


class MyUserFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class Products_Form(ModelForm):
    class Meta:
        model = Product_Assets
        fields = '__all__'
        exclude = ['user_host']


class Employee_Form(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['host']
