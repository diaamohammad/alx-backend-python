from django.db.models.signals import post_save, pre_save,post_delete
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory
from django.contrib.auth.models import User

@receiver(post_save, sender= Message)
def create_notifcation(sender, instance, created,**kwargs):

    if created:

        reciver_user=instance.receiver

        Notification.objects.create(user=reciver_user,
                message=instance,
                )
        print(f"A new notifcatin has been created for user {reciver_user.username}")



@receiver(pre_save, sender=Message)
def save_old_message(sender, instance,**kwargs):

    if instance.pk:

        try:
          old_message = Message.objects.get(pk=instance.pk)
          old_content = old_message.content

          if old_content != instance.content :
              
             MessageHistory.objetcs.create(old_content=old_content,
             message=instance)

             instance.edited = True
        except sender.DoesNotExit:
            pass
   


@receiver(post_delete, sender=User)
def cleanup_related_data(sender, instance, **kwargs):

    user_id = instance.id
    username = instance.username

    print(f'The automatic cleaning process for user-related data has been completed:{username } (ID :{user_id})')

