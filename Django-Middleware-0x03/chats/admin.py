from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Conversation, Message 


class CustomUserAdmin(UserAdmin):
    
    model = User
    
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_staff', 'date_joined')
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'phone_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'phone_number')}),
    )


admin.site.register(User, CustomUserAdmin)
@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('conversation_id', 'created_at')
