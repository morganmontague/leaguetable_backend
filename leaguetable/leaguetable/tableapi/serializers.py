from rest_framework import serializers
from .models import CustomUser, Team
from .fields import *

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["username", "is_active", "first_name", "last_name"]


class TeamSerializer(serializers.ModelSerializer):
    # points = PointListingField(queryset=Team.objects.all())
    def games_played(self):
        w = int('0' + self.wins)
        l = int('0' + self.losses)
        t = int('0' + self.ties)
        games_played = w + l + t
        return games_played

    class Meta:
        model = Team
        fields = "__all__"

    # def save(self, *args, **kwargs):
    #     self.points = (self.wins *3) +self.ties
    #     self.games_played = self.wins +self.losses +self.ties
    #     super(Team, self).save(*args, **kwargs)
    #     return self.points, self.games_played

    def points(self):
        points = (self.wins)*3 + self.ties
        points.save()
        return points

class Team_Points(serializers.ModelSerializer):

    # points = serializers.SerializerMethodField()

    # def get_points(self, obj):
    #     if obj.wins > 0 or obj.losses > 0 or obj.ties > 0:
    #         return "slow"
    #     else:
    #         return "fast"

    class Meta:
        model = Team
        fields = "__all__"

    def to_representation(self, data):
        data = super(Team_Points, self).to_representation(data)
        data['points'] = 0 if data.get('wins' and 'loses' and 'ties') == 0 else (data.get('wins')*3 + data.get('ties'))
        data['games_played'] = 0 if data.get('wins' and 'loses' and 'ties') == 0 else (data.get('wins') + data.get('ties') + data.get('losses')) 
        return data