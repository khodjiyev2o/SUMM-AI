import pyrebase
from django.conf import settings
from rest_framework.response import Response

firebase=pyrebase.initialize_app(settings.CONFIG)
auth = firebase.auth()

def fireBaseSignUp(email: str, password: str) -> Response:
   try:
        # creating a user with the given email and password
        user = auth.create_user_with_email_and_password(email=email, password=password)
        return Response({'message': f'User {email} successfull created '})
   except:
      return Response({'message': 'User already exists'})
   


