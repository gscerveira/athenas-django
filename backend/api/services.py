from .models import Pessoa
from .crud import Task

class Service:
    def __init__(self):
        self.task = Task(Pessoa)
        
    def __getattr__(self, name):
        return getattr(self.task, name)
    
    def calcular_peso_ideal(self, id):
        pessoa = self.task.get(id)
        return pessoa.calcular_peso_ideal() if pessoa else None