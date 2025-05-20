from rest_framework import viewsets
from gestor.domain.entities.livro import Livro
from gestor.domain.entities.unidade import Unidade
from gestor.domain.entities.livro_unidade import LivroUnidade
from gestor.domain.entities.genero import Genero
from gestor.presentation.serializers import LivroSerializer, UnidadeSerializer, LivroUnidadeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer

class LivroUnidadeViewSet(viewsets.ModelViewSet):
    queryset = LivroUnidade.objects.all()
    serializer_class = LivroUnidadeSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

@api_view(['GET'])
def dados_iniciais(request):
    generos = Genero.objects.all().values('id', 'nome')
    unidades = Unidade.objects.all().values('id', 'nome', 'endereco', 'telefone', 'email', 'site')
    return Response({
        'generos': list(generos),
        'unidades': list(unidades)
    })
