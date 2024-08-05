
from django.contrib import admin
from django.urls import path, include
from core import viewsets
from django.shortcuts import redirect

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post', viewsets.PostViewSet)

urlpatterns = [
    path('', lambda request: redirect('api/', permanent=False)),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
