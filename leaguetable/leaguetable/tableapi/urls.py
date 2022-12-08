from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from . import views

router = routers.SimpleRouter()
router.register(r'teams', TeamViewSet)
router.register(r'customusers', CustomUserViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'nationalities', NationalityViewSet)
router.register(r'team_players', Team_PlayersViewSet)
router.register(r'venues', VenueViewSet)
router.register(r'games', GameViewSet)
router.register(r'team_games', Team_GamesViewSet)



urlpatterns = [
# path('team/', TeamAPIView.as_view()),
# path('team/<str:pk>/', TeamAPIView.as_view()),
path('', include(router.urls)),
path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
path('user/create/', CustomUserCreate.as_view(), name="create_user"),
path('getUserTeam/', views.getUserTeam),

]