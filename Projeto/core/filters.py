import django_filters
from .models import Cadastro_Livro, Cadastro_Usuario

class CadastroLFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains', field_name='author__username')

    class Meta:
        model = Cadastro_Livro
        fields = ['title', 'author']

class CadastroUFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains', field_name='author__username')

    class Meta:
        model = Cadastro_Usuario
        fields = ['title', 'author']