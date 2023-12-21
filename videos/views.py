from rest_framework import generics, permissions, filters
from drf_api.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer

class VideoListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'like_count',
        'comment_count',
        'likevideos__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class VideoDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer