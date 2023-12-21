from django.urls import path
from .views import LikevideoCreateView, LikevideoUnlikeView 

urlpatterns = [
    path('likevideos/', LikevideoCreateView.as_view(), name='like-list-create'),
    path('likevideos/<int:pk>/', LikevideoUnlikeView.as_view(), name='like-unlike'),  
]