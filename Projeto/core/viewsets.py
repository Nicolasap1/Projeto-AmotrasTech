from rest_framework import viewsets

from .models import Cadastro_Livro, Cadastro_Usuario
from .serializers import CadastroLSerializer, CadastroUSerializer
from .filters import CadastroLFilter, CadastroUFilter

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
