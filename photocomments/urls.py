from django.urls import path
from .views import PhotocommentListCreateView, PhotocommentDetailView

urlpatterns = [
    path('photocomments/', PhotocommentListCreateView.as_view(), name='photocomment-list-create'),
    path('photocomments/<int:pk>/', PhotocommentDetailView.as_view(), name='photocomment-detail'),
]