from rest_framework import serializers
from .models import User,Message,Conversation



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','first_name','last_name','role','email','phone_number']



class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    class Meta:
        model = Message
        fields = ['message_id','sender','message_body','sent_at','conversation']
        extra_kwargs={'conversation': {'write_only':True}}


class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(read_only=True,many=True)
    users = UserSerializer(read_only=True,many=True)
    class Meta:
        model = Conversation
        fields = ['conversation_id','participants','created_at','messages']
