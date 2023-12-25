from rest_framework import serializers
from django.db import IntegrityError, transaction
from .models import Friend
from followers.models import Follower

class FriendSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    friend_name = serializers.ReadOnlyField(source='friend.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()
    
    class Meta:
        model = Friend
        fields = ['id', 'owner', 'created_at', 'following_id', 'friend', 'friend_name', 'followers_count', 'following_count', 'is_owner', 'status']

    

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"error" : "You are friends already."})

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
        
    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            
            return following.id if following else None
        return None