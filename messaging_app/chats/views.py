from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
["status", "filters"]



"IsAuthenticated", "conversation_id", "Message.objects.filter", "HTTP_403_FORBIDDEN"