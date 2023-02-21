import pyrebase
from .exceptions import *
from django.conf import settings
from rest_framework import authentication, exceptions

firebase = pyrebase.initialize_app(settings.CONFIG)
auth = firebase.auth()

class FirebaseAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'
    def authenticate(self, request):
        auth_header = authentication.get_authorization_header(request).split()
        if not auth_header or auth_header[0].lower() != b'token':
            raise exceptions.AuthenticationFailed('Invalid token header. No credential provided.')
        if len(auth_header) == 1:
            raise exceptions.AuthenticationFailed('Invalid token header. No credential provided.')
        elif len(auth_header) > 2:
            raise exceptions.AuthenticationFailed(
                'Invalid token header. Token string should not contain spaces'
            )
        try:
            token = auth_header[1].decode('utf-8')
        except UnicodeError:
            raise exceptions.AuthenticationFailed(
                'Invalid token header. Token string should not contain invalid characters.'
            )
        return self.authenticate_credential(token)

    def authenticate_credential(self, token) -> tuple:
        try:
            user_info = auth.get_account_info(token)
            user =  user_info['users'][0]['email'] 
        except Exception:
            raise InvalidCredentials(f"invalid crediantials ")
        return user, None

    
     
