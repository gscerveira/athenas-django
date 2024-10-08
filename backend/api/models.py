from django.db import models
from decimal import Decimal

class Pessoa(models.Model):
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    
    nome = models.CharField(max_length=100)
    data_nasc = models.DateField()
    cpf = models.CharField(max_length=11, unique=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    
    def calcular_peso_ideal(self):
        if self.sexo == 'M':
            return (Decimal('72.7') * self.altura) - Decimal('58')
        if self.sexo == 'F':
            return (Decimal('62.1') * self.altura) - Decimal('44.7')
        
