from gestor.domain.entities.genero import Genero
from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True, blank=True)
    editora = models.CharField(max_length=255, null=True, blank=True)
    data_publicacao = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    paginas = models.IntegerField(null=True, blank=True)
    capa = models.CharField(max_length=255, null=True, blank=True)
    idioma = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        app_label = 'gestor'

    def __str__(self):
        return self.titulo
