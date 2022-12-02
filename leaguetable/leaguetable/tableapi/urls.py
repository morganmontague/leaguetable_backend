from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'teams', TeamViewSet)
router.register(r'customusers', CustomUserViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'nationalities', NationalityViewSet)
router.register(r'team_players', Team_PlayersViewSet)
router.register(r'venues', VenueViewSet)



urlpatterns = [
# path('team/', TeamAPIView.as_view()),
# path('team/<str:pk>/', TeamAPIView.as_view()),
path('', include(router.urls))
]