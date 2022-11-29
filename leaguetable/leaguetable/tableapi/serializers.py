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

    def to_representation(self, data):
        data = super(TeamSerializer, self).to_representation(data)
        data['points'] = 0 if data.get('wins' + 'losses' + 'ties') == 0 else (data.get('wins')*3 + data.get('ties'))
        data['games_played'] = 0 if data.get('wins' + 'losses' + 'ties') == 0 else (data.get('wins') + data.get('ties') + data.get('losses')) 
        return data

class PositionSerializer(serializers.ModelSerializer):
    # points = PointListingField(queryset=Team.objects.all())
    class Meta:
        model = Position
        fields = ["position"]


class PlayerSerializer(serializers.ModelSerializer):
    position = PositionListingField(read_only=True)
    
    class Meta:
        model = Player
        fields = "__all__"
