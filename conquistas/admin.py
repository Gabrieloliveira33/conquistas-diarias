from django.contrib import admin
from .models import Conquista


@admin.register(Conquista)
class ConquistaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'concluida')
    list_filter = ('concluida', 'data')
    search_fields = ('titulo',)
