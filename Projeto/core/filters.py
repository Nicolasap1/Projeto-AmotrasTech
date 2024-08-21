import django_filters
from .models import Cadastro_Livro

class CadastroLFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains', field_name='author__username')

    class Meta:
        model = Cadastro_Livro
        fields = ['title', 'author']