# src/gestor/presentation/views.py
from django.db.models import Q
from rest_framework import viewsets, filters, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

from gestor.domain.entities.livro import Livro
from gestor.domain.entities.unidade import Unidade
from gestor.domain.entities.livro_unidade import LivroUnidade
from gestor.domain.entities.genero import Genero
from gestor.domain.entities.tipo_obra import TipoObra
from gestor.presentation.serializers import (
    LivroSerializer,
    UnidadeSerializer,
    LivroUnidadeSerializer,
)

# =========================================================
# ViewSets sem paginação (array puro) e com acesso liberado
# =========================================================

class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all().order_by("id")
    serializer_class = UnidadeSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None  # <- sem paginação

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["nome", "endereco", "telefone", "email", "site"]
    ordering_fields = ["id", "nome"]
    ordering = ["id"]

    # força resposta como array puro (defensivo)
    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        s = self.get_serializer(qs, many=True)
        return Response(s.data)


class LivroUnidadeViewSet(viewsets.ModelViewSet):
    queryset = (
        LivroUnidade.objects.all()
        .select_related("livro", "unidade")
        .order_by("id")
    )
    serializer_class = LivroUnidadeSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["id"]
    ordering = ["id"]

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        s = self.get_serializer(qs, many=True)
        return Response(s.data)


class LivroViewSet(viewsets.ModelViewSet):
    """
    GET /gestor/livros/?titulo=...&autor=...&tipo_obra=ID&editora=...&isbn=...&unidades=1,2
    Suporta também ?unidades=NOME_DA_UNIDADE (exato ou parcial).
    """
    serializer_class = LivroSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None

    # Busca e ordenação DRF
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["titulo", "autor", "editora", "isbn"]  # busca livre adicional
    ordering_fields = ["id", "titulo"]
    ordering = ["id"]

    def get_queryset(self):
        # Perf: carrega FKs/M2M com antecedência
        qs = (
            Livro.objects.all()
            .select_related("tipo_obra")   # se Livro.tipo_obra é FK
            .prefetch_related("unidades")  # se Livro.unidades é M2M
            .order_by("id")
        )

        p = self.request.query_params

        titulo = p.get("titulo")
        if titulo:
            qs = qs.filter(titulo__icontains=titulo)

        autor = p.get("autor")
        if autor:
            qs = qs.filter(autor__icontains=autor)

        tipo_obra = p.get("tipo_obra")
        if tipo_obra:
            qs = qs.filter(tipo_obra_id=tipo_obra)

        editora = p.get("editora")
        if editora:
            qs = qs.filter(editora__icontains=editora)

        isbn = p.get("isbn")
        if isbn:
            qs = qs.filter(isbn__icontains=isbn)

        unidades = p.get("unidades")
        if unidades:
            # Aceita IDs separados por vírgula (1,2,3) ou nomes (parciais)
            raw = [u.strip() for u in unidades.split(",") if u.strip()]
            ids = [int(u) for u in raw if u.isdigit()]
            nomes = [u for u in raw if not u.isdigit()]

            q = Q()
            if ids:
                q |= Q(unidades__in=ids)  # ManyToMany
                # Se fosse through: Q(livro_unidades__unidade_id__in=ids)

            if nomes:
                q |= Q(unidades__nome__icontains=" ".join(nomes))

            if q:
                qs = qs.filter(q).distinct()

        return qs

    # ---------- Documentação Swagger dos parâmetros ----------
    @extend_schema(
        parameters=[
            OpenApiParameter("titulo", OpenApiTypes.STR, OpenApiParameter.QUERY, description="Busca parcial por título"),
            OpenApiParameter("autor", OpenApiTypes.STR, OpenApiParameter.QUERY, description="Busca parcial por autor"),
            OpenApiParameter("tipo_obra", OpenApiTypes.INT, OpenApiParameter.QUERY, description="ID exato do tipo de obra"),
            OpenApiParameter("editora", OpenApiTypes.STR, OpenApiParameter.QUERY, description="Busca parcial por editora"),
            OpenApiParameter("isbn", OpenApiTypes.STR, OpenApiParameter.QUERY, description="Busca parcial por ISBN"),
            OpenApiParameter(
                "unidades",
                OpenApiTypes.STR,
                OpenApiParameter.QUERY,
                description="IDs separados por vírgula (ex.: 1,2) ou nome da unidade (ex.: Central). Aceita múltiplos."
            ),
            OpenApiParameter("search", OpenApiTypes.STR, OpenApiParameter.QUERY, description="Busca livre (DRF SearchFilter)"),
            OpenApiParameter("ordering", OpenApiTypes.STR, OpenApiParameter.QUERY, description="Ordenação (ex.: titulo ou -titulo)"),
        ]
    )
    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        s = self.get_serializer(qs, many=True)
        return Response(s.data)  # array puro


# ---------- Endpoint utilitário ----------
@api_view(["GET"])
def dados_iniciais(_request):
    generos = Genero.objects.all().values("id", "nome")
    unidades = Unidade.objects.all().values("id", "nome", "endereco", "telefone", "email", "site")
    tipos = TipoObra.objects.all().values("id", "nome")
    return Response({
        "generos": list(generos),
        "unidades": list(unidades),
        "tipo_obras": list(tipos),
    })
