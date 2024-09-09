from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import PessoaSerializer
from .services import Service

class PessoaViewSet(viewsets.ModelViewSet):
    serializer_class = PessoaSerializer
    service = Service()
    
    def get_queryset(self):
        return self.service.list()
    
    
