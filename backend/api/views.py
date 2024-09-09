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
    
    def perform_create(self, serializer):
        return self.service.create(serializer.validated_data)
    
    def perform_update(self, serializer):
        return self.service.update(serializer.instance.id, serializer.validated_data)
    
    def perform_destroy(self, instance):
        return self.service.delete(instance.id)
    
    @action(detail=True)
    def peso_ideal(self, request, pk=None):
        peso_ideal = self.service.calcular_peso_ideal(pk)
        if peso_ideal is not None:
            return Response({'peso_ideal': peso_ideal})
        return Response(status=status.HTTP_404_NOT_FOUND)
