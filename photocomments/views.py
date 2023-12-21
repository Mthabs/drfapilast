from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Photocomment
from .serializers import PhotocommentSerializer

class PhotocommentListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Photocomment.objects.all()
    serializer_class = PhotocommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['photo']
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PhotocommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Photocomment.objects.all()
    serializer_class = PhotocommentSerializer