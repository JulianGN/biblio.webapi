from django.db import models

class Unidade(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.TextField(null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'gestor'
