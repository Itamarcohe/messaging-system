from rest_framework import serializers
from chat.models import Message


class CreateMessageSerializer(serializers.ModelSerializer):
    """
    Serializer for writing (post) a message
    """

    sender_username = serializers.CharField(source='sender.username', read_only=True)
    receiver_username = serializers.CharField(source='receiver.username', read_only=True)

    class Meta:
        model = Message
        fields = ['receiver', 'subject', 'content', 'sender_username', 'receiver_username']


class MessageSerializer(serializers.ModelSerializer):

    """
    Serializer for retrieving message
    """

    sender_username = serializers.CharField(source='sender.username', read_only=True)
    receiver_username = serializers.CharField(source='receiver.username', read_only=True)

    class Meta:
        model = Message
        fields = ['receiver', 'created_at', 'subject', 'id', 'is_read', 'sender', 'content', 'sender_username', 'receiver_username']


    