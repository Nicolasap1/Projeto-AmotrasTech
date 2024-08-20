
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name="login"),
    path('category', views.category, name="category"),
    path('cart', views.cart, name= "cart"),
    path('checkout', views.checkout, name="checkout"),
    path('description', views.description, name="description"),
]

