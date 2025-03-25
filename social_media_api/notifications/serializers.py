from rest_framework import serializers
from .models import Like
from .models import Notification


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']
        read_only_fields = ['user']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'timestamp', 'is_read']
        read_only_fields = ['recipient', 'actor', 'verb', 'timestamp']