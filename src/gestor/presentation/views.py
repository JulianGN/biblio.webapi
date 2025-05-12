from rest_framework import viewsets
from gestor.domain.entities.livro import Livro
from gestor.presentation.serializers import LivroSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
