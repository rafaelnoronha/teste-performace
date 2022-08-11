from django.db import models


class Editora(models.Model):
    nome = models.CharField(
        max_length=150
    )

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['-id']
