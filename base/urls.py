from django.urls import path, include
from .import views


urlpatterns = [
    # path('', views.home, name='home'),
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('employee-add/', views.employee_add, name='employee-add'),
    path('employee-list/', views.employee_details, name='employee-list'),

    path('add_product/', views.add_product, name='add_product'),
    path('product_update/<str:pk>/', views.product_update, name='product_update'),
    path('delete-product/<str:pk>/', views.deleteProduct, name='delete-product'),
    path('', views.product_detail, name='home'),

]
