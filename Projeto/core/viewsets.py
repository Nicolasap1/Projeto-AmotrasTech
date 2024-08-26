from rest_framework import viewsets

from .models import Cadastro_Livro, Cadastro_Usuario, Category
from .serializers import CadastroLSerializer, CadastroUSerializer, CategorySerializer
from .filters import CadastroLFilter, CadastroUFilter, CategoryFilter

class CadastroLViewSet(viewsets.ModelViewSet):
    queryset = Cadastro_Livro.objects.all()
    serializer_class = CadastroLSerializer
    filterset_class = CadastroLFilter
    ordering_fields = '__all__'
    ordering = '-id'

class CadastroUViewSet(viewsets.ModelViewSet):
    queryset = Cadastro_Usuario.objects.all()
    serializer_class = CadastroUSerializer
    filterset_class = CadastroUFilter
    ordering_fields = '__all__'
    ordering = '-id'

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter
    ordering_fields = '__all__'
    ordering = '-id'
