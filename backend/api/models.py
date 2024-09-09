from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    data_nasc = models.DateField()
    cpf = models.CharField(max_length=11)
    sexo = models.CharField(max_length=1)
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
