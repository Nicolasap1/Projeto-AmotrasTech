
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from core import viewsets
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'Cadastro_Livro', viewsets.CadastroLViewSet)
router.register(r'Cadastro_Usuario', viewsets.CadastroUViewSet)
router.register(r'Categoria', viewsets.CategoryViewSet)

urlpatterns = [
    path('', lambda request: redirect('admin/', permanent=False)),
    path('admin/', admin.site.urls),
    path('api', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
