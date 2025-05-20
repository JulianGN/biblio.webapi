from rest_framework.routers import DefaultRouter
from django.urls import path
from gestor.presentation.views import LivroViewSet, UnidadeViewSet, dados_iniciais

router = DefaultRouter()
router.register(r'livros', LivroViewSet, basename='livro')
router.register(r'unidades', UnidadeViewSet, basename='unidade')

urlpatterns = router.urls

urlpatterns += [
    path('dados-iniciais/', dados_iniciais, name='dados-iniciais'),
]