from django.shortcuts import render
from .models import User,Message,Conversation
from .serializers import UserSerializer,MessageSerializer,ConversationSerializer
from rest_framework import viewsets,permissions
from .permissions import IsParticipantOfConversation
from .pagination import ResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MessageFilter



class ConversationView(viewsets.ModelViewSet):

   
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated, IsParticipantOfConversation]


    def get_queryset(self):
        
        user = self.request.user
        return user.conversations.all().prefetch_related('participants', 'messages')
    

        
class MessageView(viewsets.ModelViewSet):

    
    serializer_class = MessageSerializer
    pagination_class = ResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = MessageFilter

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(conversation__participants=user)
    
    def perform_create(self, serializer):
        serializer.save(sender = self.request.user)




