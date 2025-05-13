from django.db import models
from gestor.domain.entities.livro import Livro
from gestor.domain.entities.unidade import Unidade

class LivroUnidade(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    exemplares = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('livro', 'unidade')
        app_label = 'gestor'

    def __str__(self):
        return f"{self.livro.titulo} - {self.unidade.nome} ({self.exemplares} exemplares)"
