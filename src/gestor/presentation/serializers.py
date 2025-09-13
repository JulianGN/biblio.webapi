from rest_framework import serializers
from gestor.domain.entities.livro import Livro
from gestor.domain.entities.unidade import Unidade
from gestor.domain.entities.livro_unidade import LivroUnidade
from gestor.domain.entities.tipo_obra import TipoObra

class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields = ['id', 'nome', 'endereco', 'telefone', 'email', 'site']

class LivroUnidadeSerializer(serializers.ModelSerializer):
    unidade = serializers.PrimaryKeyRelatedField(queryset=Unidade.objects.all())

    class Meta:
        model = LivroUnidade
        fields = ['unidade', 'exemplares']

class LivroSerializer(serializers.ModelSerializer):
    unidades = LivroUnidadeSerializer(source='livrounidade_set', many=True)
    tipo_obra = serializers.PrimaryKeyRelatedField(queryset=TipoObra.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Livro
        fields = '__all__'

    def create(self, validated_data):
        unidades_data = validated_data.pop('livrounidade_set', [])
        livro = Livro.objects.create(**validated_data)
        for unidade_data in unidades_data:
            LivroUnidade.objects.create(livro=livro, **unidade_data)
        return livro

    def update(self, instance, validated_data):
        unidades_data = validated_data.pop('livrounidade_set', [])
        instance = super().update(instance, validated_data)

        # Atualizar as relações de unidades
        instance.livrounidade_set.all().delete()
        for unidade_data in unidades_data:
            LivroUnidade.objects.create(livro=instance, **unidade_data)

        return instance
