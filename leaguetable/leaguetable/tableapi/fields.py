from rest_framework import serializers
from .models import *

# class TeamListingField(serializers.RelatedField):
#     def to_representation(self, instance):
#         return instance.name


# class PointListingField(serializers.RelatedField):
#     def to_representation(self, instance):
#         points = (wins)*3 + ties
#         return points

#     def to_internal_value(self, data):
#         return Team.objects.get(points=data)

class PlayerListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.player_name

    def to_internal_value(self, data):
        return Player.objects.get(player_name=data)

class TeamListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.team_name

    def to_internal_value(self, data):
        return Team.objects.get(team_name=data)

class PositionListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.position

    def to_internal_value(self, data):
        return Position.objects.get(position=data)

class NationalityListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.nationality

    def to_internal_value(self, data):
        return Nationality.objects.get(nationality=data)

class VenueListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.venue

    def to_internal_value(self, data):
        return Venue.objects.get(venue=data)