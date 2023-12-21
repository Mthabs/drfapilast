from .models import Photo
from PIL import Image
from rest_framework import serializers
from .models import Likephoto
from photocomments.models import Photocomment
import cloudinary.uploader

class PhotoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    likephoto_id = serializers.SerializerMethodField()
    like_count = serializers.ReadOnlyField()
    comment_count = serializers.ReadOnlyField()

    class Meta:
        model = Photo
        fields = ['id', 'owner', 'image', 'caption', 'likephoto_id', 'created_at', 'updated_at', 'is_owner','like_count', 'comment_count']


    def validate_image(self, value):
        # Check file size
        max_size = 3 * 1024 * 1024  # Maximum size allowed (2MB)

        if value.size > max_size:
            raise serializers.ValidationError(f"File size too large. Max size is {max_size} bytes.")

        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_likephoto_id(self, obj):
        user = self.context['request'].user
        try:
            likephoto_instance = Likephoto.objects.get(owner=user, photo=obj)
            return likephoto_instance.id
        except Likephoto.DoesNotExist:
            return None
    
    def get_likephotos_count(self, obj):
        return obj.like_count

    def get_comment_count(self, obj):
        return obj.comment_count