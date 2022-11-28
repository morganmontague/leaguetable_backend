from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'teams', TeamViewSet)
router.register(r'customusers', CustomUserViewSet)
# router.register(r'genres', GenreViewSet)
# router.register(r'artists', ArtistViewSet)
# router.register(r'albums', AlbumViewSet)
# router.register(r'playlists', PlaylistViewSet)
# router.register(r'shortsongs', ShortSongViewSet)



urlpatterns = [
# path('team/', TeamAPIView.as_view()),
# path('team/<str:pk>/', TeamAPIView.as_view()),
path('', include(router.urls))
]