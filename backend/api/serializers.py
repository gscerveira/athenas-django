from rest_framework import serializers
from .models import Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'data_nasc', 'cpf', 'sexo', 'altura', 'peso']
        
    def validate_cpf(self, value):
        if len(value) != 11:
            raise serializers.ValidationError('O CPF deve ter 11 dígitos')
        return value
    
    def validate_sexo(self, value):
        if value not in ['M', 'F']:
            raise serializers.ValidationError('Sexo inválido')
        return value