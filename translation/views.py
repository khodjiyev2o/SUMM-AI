from rest_framework import viewsets
from .models import TranlastionObject
from .serializers import TranlastionObjectSerializer


class TranslationObjectViewSet(viewsets.ModelViewSet):
    serializer_class = TranlastionObjectSerializer
    queryset = TranlastionObject.objects.all()
    
    def perform_create(self, serializer):
        return serializer.save(FromUser=self.request.user)
    




   
