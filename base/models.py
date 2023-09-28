from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Employee(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    designation = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=150, null=True)
    phone_number = models.IntegerField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.name


class Product_Assets(models.Model):
    user_host = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_user = models.ManyToManyField(
        Employee, blank=True)
    product_name = models.CharField(max_length=200, null=True)
    given_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    stock = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name
