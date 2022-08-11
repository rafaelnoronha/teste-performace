from django.db import models


class Escritor(models.Model):
    nome = models.CharField(
        max_length=150
    )

    def __string__(self):
        return self.nome

    class Meta:
        ordering = ['-id']
