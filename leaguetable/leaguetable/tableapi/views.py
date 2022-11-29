from django.shortcuts import render
from django.http.response import Http404
from rest_framework.viewsets import ModelViewSet
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