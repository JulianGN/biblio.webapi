from django.db import models

class Editora(models.Model):
    nome = models.CharField(max_length=255)

    class Meta:
        app_label = 'gestor'

    def __str__(self):
        return self.nome
