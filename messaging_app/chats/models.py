
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    
    ROLE_CHOICES = [
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin'),
    ]
   
    
    email = models.EmailField(unique=True) 
    phone_number = models.CharField(max_length=20, null=True, blank=True) 
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='guest')
    USERNAME_FIELD = 'username'

   

    def __str__(self):
        return self.email


class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Conversation {self.conversation_id}"


class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True) 
    class Meta:
        ordering = ['sent_at'] 

    def __str__(self):
        return f"Message from {self.sender} in Conversation {self.conversation.conversation_id}"