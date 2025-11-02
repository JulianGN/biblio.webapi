# 📄 src/gestor/presentation/serializers.py
from rest_framework import serializers

from gestor.domain.entities.livro import Livro
from gestor.domain.entities.unidade import Unidade
from gestor.domain.entities.livro_unidade import LivroUnidade
from gestor.domain.entities.tipo_obra import TipoObra
from gestor.domain.entities.genero import Genero  # ⬅️ necessário porque o Livro usa "genero" (FK)


# ============== Unidades ==============
class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields = ["id", "nome", "endereco", "telefone", "email", "site"]


# ============== LivroUnidade (write / read) ==============
class LivroUnidadeWriteSerializer(serializers.ModelSerializer):
    # recebe ID de unidade
    unidade = serializers.PrimaryKeyRelatedField(queryset=Unidade.objects.all())

    class Meta:
        model = LivroUnidade
        fields = ["unidade", "exemplares"]


class LivroUnidadeReadSerializer(serializers.ModelSerializer):
    # devolve dados da unidade
    unidade = UnidadeSerializer(read_only=True)

    class Meta:
        model = LivroUnidade
        fields = ["unidade", "exemplares"]


# HÍBRIDO para manter compatibilidade com LivroUnidadeViewSet (read + write)
class LivroUnidadeSerializer(LivroUnidadeWriteSerializer):
    """
    - Na escrita (create/update), usa PrimaryKeyRelatedField (como Write).
    - Na leitura (response), serializa como Read (com Unidade detalhada).
    """
    def to_representation(self, instance):
        return LivroUnidadeReadSerializer(instance).data


# ============== Livro ==============
class LivroSerializer(serializers.ModelSerializer):
    # entrada (write) das unidades aninhadas
    unidades = LivroUnidadeWriteSerializer(many=True, write_only=True, required=False)

    # saída (read) detalhada
    unidades_detalhe = serializers.SerializerMethodField(read_only=True)

    # FKs como IDs (ambos opcionais, se fizer sentido no seu domínio)
    genero = serializers.PrimaryKeyRelatedField(
        queryset=Genero.objects.all(),
        allow_null=True,
        required=False,
    )
    tipo_obra = serializers.PrimaryKeyRelatedField(
        queryset=TipoObra.objects.all(),
        allow_null=True,
        required=False,
    )

    class Meta:
        model = Livro
        fields = (
            "id",
            "titulo",
            "autor",
            "editora",
            "data_publicacao",
            "isbn",
            "paginas",
            "capa",
            "idioma",
            "genero",       # FK (ID, opcional)
            "tipo_obra",    # FK (ID, opcional)
            "unidades",             # write-only
            "unidades_detalhe",     # read-only
        )

    def get_unidades_detalhe(self, obj):
        rows = LivroUnidade.objects.select_related("unidade").filter(livro=obj)
        return LivroUnidadeReadSerializer(rows, many=True).data

    def create(self, validated_data):
        unidades_payload = validated_data.pop("unidades", [])
        livro = Livro.objects.create(**validated_data)

        if unidades_payload:
            bulk = []
            for u in unidades_payload:
                bulk.append(
                    LivroUnidade(
                        livro=livro,
                        unidade=u["unidade"],                 # instância de Unidade
                        exemplares=u.get("exemplares", 1),
                    )
                )
            # evita erro em duplicidade (livro, unidade)
            LivroUnidade.objects.bulk_create(bulk, ignore_conflicts=True)

        return livro

    def update(self, instance, validated_data):
        # Só sincroniza unidades se o campo vier no payload; caso contrário, mantém como está
        unidades_payload = validated_data.pop("unidades", None)

        # Atualiza campos simples do livro
        instance = super().update(instance, validated_data)

        if unidades_payload is not None:
            # limpa vínculos antigos e recria
            LivroUnidade.objects.filter(livro=instance).delete()

            if unidades_payload:
                bulk = []
                for u in unidades_payload:
                    bulk.append(
                        LivroUnidade(
                            livro=instance,
                            unidade=u["unidade"],               # instância de Unidade
                            exemplares=u.get("exemplares", 1),
                        )
                    )
                LivroUnidade.objects.bulk_create(bulk, ignore_conflicts=True)

        return instance
