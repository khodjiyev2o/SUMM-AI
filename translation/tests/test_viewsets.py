import json
import requests
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from translation.models import TranlastionObject
from translation.serializers import TranlastionObjectSerializer

schema = 'http://127.0.0.1:8000'

class TranslationObjectViewSetTest(APITestCase):
    def setUp(self):
        # Authenticate with Firebase Authentication
        # Replace `YOUR_FIREBASE_ID_TOKEN` with your actual Firebase ID token
        self.email = 'samandarkhodjiyev@gmail.com'
        self.password = '2249735s'
        self.headers = {
            'password': f'{self.password}',
            'email': f'{self.email}',
        }

    def test_create_translation_object(self):
        url = schema + reverse('translation-objects-list')
        data = {'InputText': 'Hello', 'OutputText': 'Hola'}
        response = requests.post(url, headers=self.headers, json=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        

    def test_list_translation_objects(self):
        TranlastionObject.objects.create(InputText='Hello', OutputText='Hola')
        url = schema + reverse('translation-objects-list')
        response = requests.get(url, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.text)
        self.assertEqual(response_data[0]['InputText'], 'Hello')
        self.assertEqual(response_data[0]['OutputText'], 'Hola')
        self.assertEqual(response_data[0]['FromUser'], 'samandarkhodjiyev@gmail.com')
