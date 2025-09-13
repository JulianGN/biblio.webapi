from django.db import models


class TipoObra(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        app_label = 'gestor'

    def __str__(self):
        return self.nome
