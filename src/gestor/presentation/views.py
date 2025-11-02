from rest_framework import viewsets
from gestor.domain.entities.livro import Livro
from gestor.domain.entities.unidade import Unidade
from gestor.domain.entities.livro_unidade import LivroUnidade
from gestor.domain.entities.genero import Genero
from gestor.domain.entities.tipo_obra import TipoObra
from gestor.presentation.serializers import LivroSerializer, UnidadeSerializer, LivroUnidadeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer

class LivroUnidadeViewSet(viewsets.ModelViewSet):
    queryset = LivroUnidade.objects.all()
    serializer_class = LivroUnidadeSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def get_queryset(self):
        """
        Aplica filtros baseados nos parâmetros de query recebidos.
        Suporta filtros por: titulo, autor, tipo_obra, editora, isbn, unidades
        """
        queryset = Livro.objects.all()
        
        # Filtro por título (busca parcial, case-insensitive)
        titulo = self.request.query_params.get('titulo', None)
        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)
        
        # Filtro por autor (busca parcial, case-insensitive)
        autor = self.request.query_params.get('autor', None)
        if autor:
            queryset = queryset.filter(autor__icontains=autor)
        
        # Filtro por tipo_obra (ID exato)
        tipo_obra = self.request.query_params.get('tipo_obra', None)
        if tipo_obra:
            queryset = queryset.filter(tipo_obra_id=tipo_obra)
        
        # Filtro por editora (busca parcial, case-insensitive)
        editora = self.request.query_params.get('editora', None)
        if editora:
            queryset = queryset.filter(editora__icontains=editora)
        
        # Filtro por ISBN (busca parcial)
        isbn = self.request.query_params.get('isbn', None)
        if isbn:
            queryset = queryset.filter(isbn__icontains=isbn)
        
        # Filtro por unidades (livros que têm exemplares nas unidades especificadas)
        unidades = self.request.query_params.get('unidades', None)
        if unidades:
            # Aceita lista de IDs separados por vírgula: ?unidades=1,2,3
            unidade_ids = [int(uid.strip()) for uid in unidades.split(',') if uid.strip().isdigit()]
            if unidade_ids:
                queryset = queryset.filter(unidades__in=unidade_ids).distinct()
        
        return queryset

@api_view(['GET'])
def dados_iniciais(request):
    generos = Genero.objects.all().values('id', 'nome')
    unidades = Unidade.objects.all().values('id', 'nome', 'endereco', 'telefone', 'email', 'site')
    tipos = TipoObra.objects.all().values('id', 'nome')
    return Response({
        'generos': list(generos),
        'unidades': list(unidades),
        'tipo_obras': list(tipos)
    })
