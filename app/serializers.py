# swap_app/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Perfil, Feed, ConteudoSwap, Troca, Recomendacao

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class PerfilSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)
    
    class Meta:
        model = Perfil
        fields = ['usuario', 'foto_perfil', 'fundo_perfil', 'interesses', 'gosta_de', 'quer_aprender', 'perfil', 'data_cadastro']

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ['id', 'usuario', 'titulo', 'descricao', 'tipo', 'data_publicacao']

class ConteudoSwapSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConteudoSwap
        fields = ['id', 'usuario', 'titulo', 'descricao', 'data_criacao', 'bonus']

class TrocaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Troca
        fields = ['id', 'conteudo', 'usuario_ofertante', 'usuario_recebedor', 'data_troca', 'bonus_recebido']

class RecomendacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recomendacao
        fields = ['id', 'usuario', 'conteudo', 'data_recomendacao']
