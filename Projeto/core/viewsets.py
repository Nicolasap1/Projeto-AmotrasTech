from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializer
from .filters import PostFilter

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostFilter
    ordering_fields = '__all__'
    ordering = '-id'
