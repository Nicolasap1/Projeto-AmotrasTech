from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from .forms import LoginForm, RegistroForm


from .models import Cadastro_Livro, Cadastro_Usuario, Category
from .serializers import CadastroLSerializer, CadastroUSerializer, CategorySerializer
from .filters import CadastroLFilter, CadastroUFilter, CategoryFilter

class CadastroLViewSet(viewsets.ModelViewSet):
    queryset = Cadastro_Livro.objects.all()
    serializer_class = CadastroLSerializer
    filterset_class = CadastroLFilter
    ordering_fields = '__all__'
    ordering = '-id'


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter
    ordering_fields = '__all__'
    ordering = '-id'


class CadastroUViewSet(viewsets.ModelViewSet):
    queryset = Cadastro_Usuario.objects.all()
    serializer_class = CadastroUSerializer
    filterset_class = CadastroUFilter
    ordering_fields = '__all__'
    ordering = '-id'
    def register(self, request):
        form = RegistroForm(request.data)
        if form.is_valid():
            usuario = form.save()
           
            return Response({'token': 'some_token'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

    def login(self, request):
        form = LoginForm(request.data)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['password']
            usuario = Cadastro_Usuario.objects.get(email=email)
            if usuario.check_password(senha):
                # Login bem-sucedido, retornar token ou dados do usuário
                return Response({'token': 'some_token'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)