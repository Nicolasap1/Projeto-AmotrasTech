from rest_framework import serializers
from .models import Cadastro_Livro , Cadastro_Usuario, Category

class CadastroLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro_Livro
        fields = '__all__'

    def get_imagem_url(self, obj):
        request = self.context.get('request')
        if obj.imagem and hasattr(obj.imagem, 'url'):
            return request.build_absolute_uri(obj.imagem.url)
        return None     

class CadastroUSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro_Usuario
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'