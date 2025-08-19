from rest_framework import serializers
from .models import Chat, Message,Story

class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source='sender.username', read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'sender', 'sender_name', 'text', 'created_at')  


class ChatSerializer(serializers.ModelSerializer):
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        fields = ('id', 'title', 'last_message',)

    def get_last_message(self, obj):
        message = obj.message.last()
        if message:
            return MessageSerializer(message).data
        return None


class StorySerializer(serializers.ModelSerializer):
    is_active = serializers.ReadOnlyField()

    class Meta:
        model = Story
        fields = ["id", "user", "chat", "video", "image", "created_at", "is_active"]
