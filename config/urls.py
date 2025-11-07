# config/urls.py
from django.contrib import admin
from django.http import JsonResponse, HttpResponse
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

def api_root(_request):
    """Resposta simples para evitar erro 404 na raiz."""
    return JsonResponse({
        "name": "Biblio Web API",
        "version": "v1",
        "endpoints": {
            "health": "/healthz",
            "schema": "/api/schema/",
            "swagger": "/api/docs/",
            "redoc": "/api/redoc/",
            "gestor": "/gestor/",
        },
    })

urlpatterns = [
    # raiz e healthcheck
    path("", api_root, name="root"),
    path("healthz", lambda r: HttpResponse(status=204)),

    # painel admin
    path("admin/", admin.site.urls),

    # rotas principais
    path("gestor/", include("src.gestor.presentation.urls")),

    # documentação
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
