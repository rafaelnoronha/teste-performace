from django.db import models
from escritor.models import Escritor
from editora.models import Editora


class Livro(models.Model):
    titulo = models.CharField(
        max_length=150
    )

    paginas = models.PositiveIntegerField(
        default=0
    )

    editora = models.ForeignKey(
        Editora,
        on_delete=models.PROTECT,
        null=True
    )

    escritor = models.ForeignKey(
        Escritor,
        on_delete=models.PROTECT,
        null=True
    )

    def __string__(self):
        return self.titulo

    class Meta:
        ordering = ['-id']
