# 📁 src/gestor/presentation/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gestor.presentation.views import (
    LivroViewSet,
    UnidadeViewSet,
    LivroUnidadeViewSet,
    dados_iniciais,
)

# ---------- Roteador padrão DRF ----------
router = DefaultRouter()
router.register(r"livros", LivroViewSet, basename="livro")
router.register(r"unidades", UnidadeViewSet, basename="unidade")
router.register(r"livro-unidades", LivroUnidadeViewSet, basename="livro-unidade")

# ---------- URLs principais ----------
urlpatterns = [
    path("", include(router.urls)),
    path("dados-iniciais/", dados_iniciais, name="dados-iniciais"),
]
