from rest_framework.views import APIView
from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from .models import Friend
from .serializers import FriendSerializer
from rest_framework import status


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

    def get_queryset(self):
        friend_requests = Friend.objects.filter(friend=self.request.user, status='pending')
        return friend_requests

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class FriendUnfriendView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Friend.objects.annotate(
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = FriendSerializer
    
    def perform_destroy(self, instance):
        if instance.status == 'pending':
            instance.delete()
        else:
            instance.status = 'pending'
            instance.save()

class FriendRequestsView(APIView):
    def get(self, request):
        friend_requests = Friend.objects.filter(friend=request.user, status='pending')
        serializer = FriendSerializer(friend_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)