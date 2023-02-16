from rest_framework import serializers


class FireBaseSignUpSerializer(serializers.Serializer):
    """ Data serialization from User
    """
    email = serializers.EmailField()
    password = serializers.CharField()
