from django.shortcuts import render
from django.http.response import Http404
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *

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
    queryset = Team_Player.objects.all()
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