from rest_framework import serializers
from .models import TranlastionObject


class TranlastionObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranlastionObject
        fields = '__all__'
        read_only_fields = ('FromUser',)