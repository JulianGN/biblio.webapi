# src/gestor/presentation/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gestor.presentation.views import LivroViewSet, UnidadeViewSet, dados_iniciais

router = DefaultRouter()
router.register(r"livros", LivroViewSet, basename="livro")
router.register(r"unidades", UnidadeViewSet, basename="unidade")

urlpatterns = [
    # rotas geradas automaticamente pelos ViewSets
    path("", include(router.urls)),

    # endpoint adicional
    path("dados-iniciais/", dados_iniciais, name="dados-iniciais"),
]
