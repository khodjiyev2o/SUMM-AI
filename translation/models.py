from django.db import models

class TranlastionObject(models.Model):
    InputText =  models.CharField(max_length=100)
    OutputText =  models.CharField(max_length=100)
    FromUser = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.pk)
    