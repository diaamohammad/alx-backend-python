from rest_framework import routers
from django.urls import path,include
from .views import MessageView,ConversationView

router = routers.DefaultRouter

router.register(r'conversations',ConversationView,basename='conversatios')
router.register(r'messages',MessageView,basename='message')


urlpatterns = [
    path('', include(router.urls)),
]

