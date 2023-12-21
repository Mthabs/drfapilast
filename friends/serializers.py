from rest_framework import serializers
from django.db import IntegrityError, transaction
from .models import Friend

class FriendSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    friend_name = serializers.ReadOnlyField(source='friend.username')

    class Meta:
        model = Friend
        fields = ['id', 'owner', 'created_at', 'friend', 'friend_name']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"error" : "You are friends already."})