import django_filters
from .models import User,Message

class MessageFilter(django_filters.filterset):

    sender = django_filters.ModelChoiceFilter(
        field_name = 'sender',
        queryset = User.objects.all(),
        label = 'filter messages by sender'
    )


    sent_at = django_filters.DateFromToRangeFilter(
        field_name= 'sent_at',
        label = 'filter message filter by sent date'

    )

    class Meta:
        model = Message
        fields = ['sender','sent_at']