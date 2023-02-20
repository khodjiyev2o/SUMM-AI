from django.urls import include, path
from rest_framework import routers
from translation.views import TranslationObjectViewSet
from firebaseauth.views import SignUpView, getTokenView
from django.contrib import admin
from .yasg import swaggerurlpatterns


router = routers.DefaultRouter()
router.register(r'translation-objects', TranslationObjectViewSet, basename='translation-objects')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/signUp', SignUpView.as_view(), name='signUp' ),
    path('api/token', getTokenView.as_view(), name='token' )
]

urlpatterns += swaggerurlpatterns
