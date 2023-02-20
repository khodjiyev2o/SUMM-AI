from rest_framework import viewsets
from .models import TranlastionObject
from .serializers import TranlastionObjectSerializer
from firebaseauth.authentication import FirebaseAuthentication

class TranslationObjectViewSet(viewsets.ModelViewSet):
    serializer_class = TranlastionObjectSerializer
    queryset = TranlastionObject.objects.all()
    authentication_classes = [FirebaseAuthentication]
    
    def perform_create(self, serializer):
        return serializer.save(FromUser=self.request.user)
    




   
