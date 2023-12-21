from django.urls import path
from .views import VideocommentListCreateView, VideocommentDetailView

urlpatterns = [
    path('videocomments/', VideocommentListCreateView.as_view(), name='videocomment-list-create'),
    path('videocomments/<int:pk>/', VideocommentDetailView .as_view(), name='videocomment-detail'),
]