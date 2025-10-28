from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from .models import Message



def delete_user(request):

     if not request.user.is_authenticated :
         return redirect ('login')  

     user_to_delete = request.user

     try:
        username = user_to_delete.username

        user_to_delete.delete()
        logout(request)
        return redirect('/')

     except Exception as e:
         print(f'faild in deleting acount user{user_to_delete.id} :{e}')











@cache_page(60)  # Cache for 60 seconds
def messages_list(request):
    messages = Message.objects.all().select_related('sender', 'receiver')
    return render(request, 'messages_list.html', {'messages': messages})

