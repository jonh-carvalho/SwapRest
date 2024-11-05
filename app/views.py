# swap_app/views.py
from rest_framework import viewsets
from .models import Perfil, Feed, ConteudoSwap, Troca, Recomendacao
from .serializers import PerfilSerializer, FeedSerializer, ConteudoSwapSerializer, TrocaSerializer, RecomendacaoSerializer
from rest_framework.permissions import IsAuthenticated

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    permission_classes = [IsAuthenticated]

class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [IsAuthenticated]

class ConteudoSwapViewSet(viewsets.ModelViewSet):
    queryset = ConteudoSwap.objects.all()
    serializer_class = ConteudoSwapSerializer
    permission_classes = [IsAuthenticated]

class TrocaViewSet(viewsets.ModelViewSet):
    queryset = Troca.objects.all()
    serializer_class = TrocaSerializer
    permission_classes = [IsAuthenticated]

class RecomendacaoViewSet(viewsets.ModelViewSet):
    queryset = Recomendacao.objects.all()
    serializer_class = RecomendacaoSerializer
    permission_classes = [IsAuthenticated]
