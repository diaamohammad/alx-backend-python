from django.shortcuts import render
from .models import User,Message,Conversation
from .serializers import UserSerializer,MessageSerializer,ConversationSerializer
from rest_framework import viewsets,permissions


class ConversationView(viewsets.ModelViewSet):

   
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        
        user = self.request.user
        return user.conversations.all().prefetch_related('participants', 'messages')
        
class MessageView(viewsets.ModelViewSet):

    
    serializer_class = MessageSerializer

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(conversation__participants=user)
    
    def perform_create(self, serializer):
        serializer.save(sender = self.request.user)




