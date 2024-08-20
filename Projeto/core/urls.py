
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('category', views.category),
    path('cart', views.cart),
    path('promo', views.promo),
    path('description', views.description),
]

