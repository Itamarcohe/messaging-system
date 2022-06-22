from django.urls import path
from .views import (    MessageAPIView,
                        CreateMessageAPIView,
                        MessageDetailsAPIView,
                        UnReadMessageAPIView)

app_name='chat'

urlpatterns = [
    path('', MessageAPIView.as_view(), name='messages'),
    path('unread/', UnReadMessageAPIView.as_view(), name='unread_messages'),
    path('<int:id>/', MessageDetailsAPIView.as_view(), name='message_details'),
    path('write/', CreateMessageAPIView.as_view(), name='write_message'),
]

#messages/          -       All messages for the current user
#messages/unread/   -       All unread messages for the current user
#messages/<int:id>  -       Messsage details by a specific ID
#messages/write/    -       To write a new message