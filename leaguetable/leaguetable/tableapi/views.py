from django.shortcuts import render
from django.http.response import Http404
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.decorators import api_view

class ObtainTokenPairWithColorView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class PositionViewSet(ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class NationalityViewSet(ModelViewSet):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class Team_PlayersViewSet(ModelViewSet):
    queryset = Team_Players.objects.all()
    serializer_class = Team_PlayersSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class VenueViewSet(ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class Team_GamesViewSet(ModelViewSet):
    queryset = Team_Games.objects.all()
    serializer_class = Team_GamesSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

@api_view(['GET'])
def getUserTeam(request):
    print(request)
    # user = CustomUser.objects.get(id = request.user.id)
    teams = Team.objects.filter(user_id = request.user.id)
    print(teams)
    user_team = []
    for team in teams:
        try:
            # this_user = CustomUser.objects.get(id=customUser.id)
            # print(this_user)
            serializer = TeamSerializer(team)

            this_user.append(serializer.data)
        except:
            return Response(serializer.data)


    return Response(this_user)