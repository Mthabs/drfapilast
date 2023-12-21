from rest_framework import serializers
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError as DjangoValidationError
from .models import Video
from .models import Likevideo

class VideoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    likevideo_id = serializers.SerializerMethodField()
    like_count = serializers.ReadOnlyField()
    comment_count = serializers.ReadOnlyField()

    class Meta:
        model = Video
        fields = ['id', 'owner', 'title', 'video_file', 'description', 'created_at', 'updated_at', 'is_owner','likevideo_id','like_count','comment_count']


    def validate_video_file(self, value):
        # Check file extension
        valid_extensions = ['mp4', 'avi', 'mkv', 'mp3']  
        extension_validator = FileExtensionValidator(allowed_extensions=valid_extensions)
        
        try:
            extension_validator(value.name)
        except DjangoValidationError as e:
            raise serializers.ValidationError(str(e))

        # Check file size
        max_size = 50 * 1024 * 1024  
        if value.size > max_size:
            raise serializers.ValidationError(f"File size too large. Max size is {max_size} bytes.")

        return value 

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.owner


    def get_likevideo_id(self, obj):
        user = self.context['request'].user
        try:
            likevideo_instance = Likevideo.objects.get(owner=user, video=obj)
            return likevideo_instance.id
        except Likevideo.DoesNotExist:
            return None

    def get_likevideo_count(self, obj):
        return obj.like_count
    
    def get_comment_count(self, obj):
        return obj.comment_count