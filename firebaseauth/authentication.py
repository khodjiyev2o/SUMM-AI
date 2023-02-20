import pyrebase
from rest_framework import authentication
from .exceptions import *
from django.conf import settings


firebase = pyrebase.initialize_app(settings.CONFIG)
auth = firebase.auth()

class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
            token = request.headers.get('token')
            if not token :
                raise NoAuthToken("No authentication credentials provided ")
            try:
                user_info = auth.get_account_info(token)
                user =  user_info['users'][0]['email'] 
            except Exception:
                raise InvalidCredentials(f"invalid crediantials ")
            return user, None

    
     
