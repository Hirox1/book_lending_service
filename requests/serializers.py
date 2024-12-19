from rest_framework import serializers
from .models import Request


class RequestSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.full_name')
    receiver = serializers.ReadOnlyField(source='receiver.full_name')

    class Meta:
        model = Request
        fields = ['id', 'sender', 'receiver', 'message', 'created_at', 'status']
