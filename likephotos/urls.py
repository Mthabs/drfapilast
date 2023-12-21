from django.urls import path
from .views import LikephotoCreateView, LikephotoUnlikeView  

urlpatterns = [
    path('likephotos/', LikephotoCreateView.as_view(), name='like-list-create'), 
    path('likephotos/<int:pk>/', LikephotoUnlikeView.as_view(), name='like-unlike'),
]