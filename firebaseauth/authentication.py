import pyrebase
from rest_framework import authentication
from .exceptions import *
from django.conf import settings


firebase = pyrebase.initialize_app(settings.CONFIG)
auth = firebase.auth()

class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        email = request.headers.get('email')
        password = request.headers.get('password')
        if not email or not password:
            raise NoAuthToken("No authentication credentials provided ")
        try:
            user = auth.sign_in_with_email_and_password(email,password)
        except Exception:
            raise InvalidCredentials(f"invalid crediantials ")
        return user, None

    
     
