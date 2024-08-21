
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from core import viewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Cadastro_Livro', viewsets.CadastroLViewSet)
router.register(r'Cadastro_Usuario', viewsets.CadastroUViewSet)

urlpatterns = [
    path('', lambda request: redirect('admin/', permanent=False)),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api', include(router.urls)),
]
