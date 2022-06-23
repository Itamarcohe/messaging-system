from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .serializers import MessageSerializer, CreateMessageSerializer
from chat.models import Message
from django.shortcuts import get_object_or_404, Http404

User = get_user_model()


class CreateMessageAPIView(generics.CreateAPIView):

    """

    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreateMessageSerializer
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class MessageAPIView(generics.ListAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MessageSerializer

    def get_queryset(self):
        user = self.request.user
        qs = Message.objects.filter(Q(sender=user) | Q(receiver=user)).order_by("-created_at").distinct()
        return qs


class UnReadMessageAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MessageSerializer

    def get_queryset(self):
        user = self.request.user
        msgs = Message.objects.filter(Q(Q(receiver=user) & Q(is_read=False))).order_by("-created_at").distinct()
        return msgs

        
class MessageDetailsAPIView(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MessageSerializer

    def get_object(self, *args, **kwargs):
        user = self.request.user
        message_id = self.kwargs.get("id")
        message = get_object_or_404(Message, id=message_id)

        if message.receiver != user and message.sender != user:
            raise Http404
        else:
            if not message.is_read and message.receiver == user:
                message.is_read = True
                message.save()
            
            return message
