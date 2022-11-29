from django.shortcuts import render
from django.http.response import Http404
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

# Create your views here.
class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = Team_Points
    http_method_names = ['get', 'post', 'put', 'delete']

    # def points(self):
    #     points = (self.wins)*3 + self.ties
    #     points.save()
    # def games_played(self):
    #     games_played = self.wins +self.losses +self.ties
    #     return games_played

    # def save(self, *args, **kwargs):
    #     points = (self.wins *3) +self.ties
    #     games_played = self.wins +self.losses +self.ties
    #     super(Team, self).save(*args, **kwargs)
    #     return self.points, self.games_played

class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ['get', 'post', 'put', 'delete']