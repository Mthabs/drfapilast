from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Friend
from .serializers import FriendSerializer


class FriendListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)   


class FriendUnfriendView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    
