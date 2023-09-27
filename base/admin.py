from django.contrib import admin
from .models import User, Product_Assets, Employee

# Register your models here.
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Product_Assets)
