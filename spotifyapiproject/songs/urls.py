from django.urls import path
from .views import SongListCreateView, SongRetrieveUpdateDestroyView

urlpatterns = [
    path('songs/', SongListCreateView.as_view(), name="song-list"),
    path('songs/<int:pk>/', SongRetrieveUpdateDestroyView.as_view(), name="song-detail")
]