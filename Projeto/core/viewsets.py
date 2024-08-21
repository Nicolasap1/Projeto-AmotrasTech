from rest_framework import viewsets

from .models import Cadastro_Livro
from .serializers import CadastroLSerializer
from .filters import CadastroLFilter

class PostViewSet(viewsets.ModelViewSet):
    queryset = Cadastro_Livro.objects.all()
    serializer_class = CadastroLSerializer
    filterset_class = CadastroLFilter
    ordering_fields = '__all__'
    ordering = '-id'
