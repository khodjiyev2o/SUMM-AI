from django.urls import include, path
from rest_framework import routers
from translation.views import TranslationObjectViewSet
from firebaseauth.views import SignUp
from django.conf import settings
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()
router.register(r'translation-objects', TranslationObjectViewSet, basename='translation-objects')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/signUp', SignUp, name='signUp' )
]
