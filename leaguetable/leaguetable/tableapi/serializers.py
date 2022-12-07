from rest_framework import serializers
from .models import CustomUser, Team
from .fields import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        return token


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', "is_active", "first_name", "last_name")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

# class CustomUserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = CustomUser
#         fields = ["username", "is_active", "first_name", "last_name"]
class Team_GamesSerializer(serializers.ModelSerializer):
    game = GameListingField(many=True, read_only=True)
    team = TeamListingField(many=True, read_only=True)
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Team_Players
        fields = "__all__"



class Team_PlayersSerializer(serializers.ModelSerializer):
    player = PlayerListingField(many=True, read_only=True)
    team = TeamListingField(many=True, read_only=True)
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Team_Players
        fields = "__all__"



class PositionSerializer(serializers.ModelSerializer):
    # points = PointListingField(queryset=Team.objects.all())
    class Meta:
        model = Position
        fields = ["position"]


class NationalitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Nationality
        fields =["nationality"]

class PlayerSerializer(serializers.ModelSerializer):
    position = PositionListingField(read_only=True)
    nationality = NationalityListingField(read_only=True)

    
    class Meta:
        model = Player
        fields = "__all__"

class TeamSerializer(serializers.ModelSerializer):
    players = serializers.SerializerMethodField()
    games = serializers.SerializerMethodField()
    
    def get_players(self, obj):
        team = obj.id
        players = Team_Players.objects.filter(team=team)
        team_players = []
        for player in players:
            team_players.append(f"{player.player}")
        return team_players

    def get_games(self, obj):
        team = obj.id
        games = Team_Games.objects.filter(team=team)
        team_games = []
        for game in games:
            team_games.append(f"{game.game}")
        return team_games

    class Meta:
        model = Team
        fields = "__all__"

    def to_representation(self, data):
        data = super(TeamSerializer, self).to_representation(data)
        data['points'] = 0 if data.get('wins' + 'losses' + 'ties') == 0 else (data.get('wins')*3 + data.get('ties'))
        data['games_played'] = 0 if data.get('wins' + 'losses' + 'ties') == 0 else (data.get('wins') + data.get('ties') + data.get('losses')) 
        return data

class VenueSerializer(serializers.ModelSerializer):
    venue = VenueListingField(read_only=True)

    class Meta:
        model = Venue
        fields = "__all__"

class GameSerializer(serializers.ModelSerializer):
    game = GameListingField(read_only=True)

    class Meta:
        model = Game
        fields = "__all__"