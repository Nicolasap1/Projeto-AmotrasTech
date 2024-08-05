import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains', field_name='author__username')

    class Meta:
        model = Post
        fields = ['title', 'author']