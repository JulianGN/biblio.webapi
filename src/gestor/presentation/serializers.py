from rest_framework import serializers
from gestor.domain.entities.livro import Livro

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
