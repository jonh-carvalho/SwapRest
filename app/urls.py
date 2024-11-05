# swap_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'perfis', views.PerfilViewSet, basename='perfil')
router.register(r'feeds', views.FeedViewSet, basename='feed')
router.register(r'conteudos_swap', views.ConteudoSwapViewSet, basename='conteudo_swap')
router.register(r'trocas', views.TrocaViewSet, basename='troca')
router.register(r'recomendacoes', views.RecomendacaoViewSet, basename='recomendacao')

urlpatterns = [
    path('', include(router.urls)),
]
