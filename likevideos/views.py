from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Likevideo
from .serializers import LikevideoSerializer

class LikevideoCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Likevideo.objects.all()
    serializer_class = LikevideoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikevideoUnlikeView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Likevideo.objects.all()
    serializer_class = LikevideoSerializer