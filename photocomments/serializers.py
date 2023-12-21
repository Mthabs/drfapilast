from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Photocomment


class PhotocommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.userprofile.id')
    profile_picture = serializers.ReadOnlyField(source='owner.userprofile.profile_picture_url')
    is_owner = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Photocomment
        fields = ['id', 'profile_id', 'owner', 'photo', 'content', 'created_at', 'updated_at', 'profile_picture', 'is_owner']

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.owner
        
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
    
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

class PhotocommentDetailSerializer(PhotocommentSerializer):
    photo = serializers.ReadOnlyField(source='photo.id')