from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Message, Notification, MessageHistory

# إنشاء Notification عند إرسال رسالة جديدة
@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.receiver,
            message=instance,
            text=f"You received a new message from {instance.sender.username}"
        )

# تسجيل الرسائل القديمة قبل التعديل
@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.id:
        old = Message.objects.get(id=instance.id)
        if old.content != instance.content:
            MessageHistory.objects.create(
                message=old,
                old_content=old.content
            )
            instance.edited = True

# حذف البيانات المرتبطة عند حذف المستخدم
@receiver(post_delete, sender=User)
def delete_related_data(sender, instance, **kwargs):
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()
    Notification.objects.filter(user=instance).delete()
    MessageHistory.objects.filter(message__sender=instance).delete()
