# swap_app/admin.py
from django.contrib import admin
from .models import Perfil, Feed, ConteudoSwap, Troca, Recomendacao

admin.site.register(Perfil)
admin.site.register(Feed)
admin.site.register(ConteudoSwap)
admin.site.register(Troca)
admin.site.register(Recomendacao)
