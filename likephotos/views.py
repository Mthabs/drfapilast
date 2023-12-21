from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Likephoto
from .serializers import LikephotoSerializer

class LikephotoCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Likephoto.objects.all()
    serializer_class = LikephotoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikephotoUnlikeView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Likephoto.objects.all()
    serializer_class = LikephotoSerializer
    
