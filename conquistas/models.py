from django.db import models
from django.contrib.auth.models import User

class Conquista(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='conquistas'
    )

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    data = models.DateField()
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
