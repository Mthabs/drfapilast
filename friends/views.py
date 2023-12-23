from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Friend
from .serializers import FriendSerializer


class FriendListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Friend.objects.annotate(
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = FriendSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__friend',
        'owner__followed__owner__friend',
    ]
    ordering_fields = [
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)   


class FriendUnfriendView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Friend.objects.annotate(
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = FriendSerializer
    
