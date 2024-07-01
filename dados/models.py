from django.db import models

class Dado(models.Model):
    situacao = models.DateField()
    codigo = models.CharField(max_length=32, unique=True)
    nome = models.CharField(max_length=155)
    sobrenome = models.CharField(max_length=100)
    rnm = models.CharField(max_length=16)
    data_nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=64)

    def __str__(self):
        return self.nome