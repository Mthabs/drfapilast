from django.urls import path
from .views import FriendListCreateView, FriendUnfriendView

urlpatterns = [
    path('friends/', FriendListCreateView.as_view(), name='friend-list-create'),
    path('friends/<int:pk>/', FriendUnfriendView.as_view(), name='friend-Unfriend'),
]