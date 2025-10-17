from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import MessageView,ConversationView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

router = DefaultRouter()

router.register(r'conversations',ConversationView,basename='conversatios')
router.register(r'messages',MessageView,basename='message')


urlpatterns = [
    path('', include(router.urls)),
    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

