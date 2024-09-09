from django.core.exceptions import ObjectDoesNotExist

class Task:
    def __init__(self, model):
        self.model = model
        
    def create(self, data):
        return self.model.objects.create(**data)
    
    def get(self, id):
        try:
            return self.model.objects.get(id=id)
        except ObjectDoesNotExist:
            return None        
    
    def update(self, id, data):
        obj = self.get(id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            return obj
        return None
    
    def delete(self, id):
        obj = self.get(id)
        if obj:
            obj.delete()
            return True
        return False
    
    def list(self):
        return self.model.objects.all()
    
    def search(self, **kwargs):
        return self.model.objects.filter(**kwargs)