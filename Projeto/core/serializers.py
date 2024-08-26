from rest_framework import serializers
from .models import Cadastro_Livro , Cadastro_Usuario, Category

class CadastroLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro_Livro
        fields = '__all__'

class CadastroUSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro_Usuario
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'