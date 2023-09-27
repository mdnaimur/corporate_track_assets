from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('employee-add/', views.employee_add, name='employee-add'),
    path('employee-list/', views.employee_details, name='employee-list'),

]
