from rest_framework.decorators import api_view, authentication_classes
from rest_framework.exceptions import ValidationError
from .serializers import FireBaseSignUpSerializer
from .services.user import fireBaseSignUp, fireBaseToken
from rest_framework.response import Response

@api_view(["POST"])
@authentication_classes([])
def SignUp(request):
    """ User SignUp 
    """
    user_data = FireBaseSignUpSerializer(data=request.data)
    if user_data.is_valid():
        email = user_data.validated_data['email']
        password = user_data.validated_data['password']
        return fireBaseSignUp(email=email, password=password)
    else:
        raise ValidationError(
            code=400, 
            detail='Wrong credentials provided')


@api_view(["POST"])
@authentication_classes([])
def getToken(request):
    """ getting token with email and password  
    """
    if request.method == "POST":
        user_data = FireBaseSignUpSerializer(data=request.data)
        if user_data.is_valid():
            email = user_data.validated_data['email']
            password = user_data.validated_data['password']
            return fireBaseToken(email=email, password=password)
        else:
            raise ValidationError(
                code=400, 
                detail='Wrong credentials provided')
   
