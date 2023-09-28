from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('product/', views.getProducts),
    path('product/<str:pk>/', views.getProduct)
]
