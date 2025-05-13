from rest_framework import viewsets
from gestor.domain.entities.livro import Livro
from gestor.domain.entities.unidade import Unidade
from gestor.domain.entities.livro_unidade import LivroUnidade
from gestor.presentation.serializers import LivroSerializer, UnidadeSerializer, LivroUnidadeSerializer

class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer

class LivroUnidadeViewSet(viewsets.ModelViewSet):
    queryset = LivroUnidade.objects.all()
    serializer_class = LivroUnidadeSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
