from rest_framework import serializers
from .models import CustomUser, Team
from .fields import *

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["username", "is_active", "first_name", "last_name"]


class TeamSerializer(serializers.ModelSerializer):
    # points = PointListingField(queryset=Team.objects.all())

    class Meta:
        model = Team
        fields = "__all__"

    # def save(self, *args, **kwargs):
    #     self.points = (self.wins *3) +self.ties
    #     self.games_played = self.wins +self.losses +self.ties
    #     super(Team, self).save(*args, **kwargs)
    #     return self.points, self.games_played

    # def points(self):
    #     points = (self.wins)*3 + self.ties
    #     points.save()
    # def games_played(self):
    #     games_played = self.wins +self.losses +self.ties
    #     return games_played