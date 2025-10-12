

# Create your views here.
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from messaging.models import Message

@cache_page(60)
def messages_list(request):
    messages = Message.objects.select_related('sender', 'receiver').all()
    return render(request, 'messages_list.html', {'messages': messages})
