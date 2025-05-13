from rest_framework.routers import DefaultRouter
from gestor.presentation.views import LivroViewSet, UnidadeViewSet

router = DefaultRouter()
router.register(r'livros', LivroViewSet, basename='livro')
router.register(r'unidades', UnidadeViewSet, basename='unidade')

urlpatterns = router.urls