from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Videocomment
from .serializers import VideocommentSerializer

class VideocommentListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Videocomment.objects.all()
    serializer_class = VideocommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['video']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class VideocommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Videocomment.objects.all()
    serializer_class = VideocommentSerializer
