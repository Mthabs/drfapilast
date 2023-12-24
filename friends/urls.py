from django.urls import path
from .views import FriendListCreateView, FriendUnfriendView, FriendRequestsView

urlpatterns = [
    path('friends/', FriendListCreateView.as_view(), name='friend-list-create'),
    path('friends/<int:pk>/', FriendUnfriendView.as_view(), name='friend-Unfriend'),
    path('friend-requests/', FriendRequestsView.as_view(), name='friend-requests'),
]