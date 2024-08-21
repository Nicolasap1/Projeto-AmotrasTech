from rest_framework import serializers
from .models import Cadastro_Livro

class CadastroLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro_Livro
        fields = '__all__'