from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.shortcuts import render
from .models import Message

@cache_page(60)  # Cache for 60 seconds
def messages_list(request):
    messages = Message.objects.all().select_related('sender', 'receiver')
    return render(request, 'messages_list.html', {'messages': messages})

