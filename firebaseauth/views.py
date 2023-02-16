from rest_framework.decorators import api_view, authentication_classes
from rest_framework.exceptions import ValidationError
from .serializers import FireBaseSignUpSerializer
from .services.user import fireBaseSignUp

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