# swap_app/models.py
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    PERFIL_CHOICES = [
        ('MODERADOR', 'Moderador'),
        ('CLIENTE', 'Cliente')
    ]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    foto_perfil = models.URLField(blank=True, null=True)
    fundo_perfil = models.URLField(blank=True, null=True)
    interesses = models.TextField(blank=True, null=True)
    gosta_de = models.TextField(blank=True, null=True)
    quer_aprender = models.TextField(blank=True, null=True)
    perfil = models.CharField(max_length=20, choices=PERFIL_CHOICES)
    data_cadastro = models.DateTimeField(auto_now_add=True)

class Feed(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feeds")
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    tipo = models.CharField(max_length=50)  # e.g., "RECOMENDACAO", "EM_ALTA"
    data_publicacao = models.DateTimeField(auto_now_add=True)

class ConteudoSwap(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="conteudos_swap")
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    bonus = models.IntegerField(default=0)

class Troca(models.Model):
    conteudo = models.ForeignKey(ConteudoSwap, on_delete=models.CASCADE, related_name="trocas")
    usuario_ofertante = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ofertas_realizadas")
    usuario_recebedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ofertas_recebidas")
    data_troca = models.DateTimeField(auto_now_add=True)
    bonus_recebido = models.IntegerField()

class Recomendacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recomendacoes")
    conteudo = models.ForeignKey(ConteudoSwap, on_delete=models.CASCADE, related_name="recomendacoes")
    data_recomendacao = models.DateTimeField(auto_now_add=True)
