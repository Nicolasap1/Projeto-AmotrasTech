import django_filters
from .models import Cadastro_Livro, Cadastro_Usuario, Category

class CadastroLFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    content = django_filters.CharFilter(lookup_expr='icontains')
    criado_por = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains', field_name='author__username')
    image = django_filters.CharFilter(lookup_expr='icontains')
    Category = django_filters.CharFilter(lookup_expr='icontans')
    class Meta:
        model = Cadastro_Livro
        fields = ['title','content','criado_por','author','image','category']

class CadastroUFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    password = django_filters.CharFilter(lookup_expr='icontains')
    created_at = django_filters.DateFilter(lookup_epx= 'contains')
    class Meta:
        model = Cadastro_Usuario
        fields = ['name', 'email', 'password','created_at']

class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Category
        fields = ['name']