from .serializers import FireBaseSignUpSerializer
from .services.user import fireBaseSignUp, fireBaseToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class SignUpView(APIView):
    serializer_class = FireBaseSignUpSerializer
    @swagger_auto_schema(
        request_body=FireBaseSignUpSerializer,
        responses={
            status.HTTP_200_OK: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(type=openapi.TYPE_STRING),
                }
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING),
                }
            ),
        }
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            return fireBaseSignUp(email=email, password=password)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class getTokenView(APIView):
    serializer_class = FireBaseSignUpSerializer
    @swagger_auto_schema(
        request_body=FireBaseSignUpSerializer,
        responses={
            status.HTTP_200_OK: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'token': openapi.Schema(type=openapi.TYPE_STRING),
                }
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING),
                }
            ),
        }
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            return fireBaseToken(email=email, password=password)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
