from rest_framework import serializers
from .models import *

class TeamListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.name


class PointListingField(serializers.RelatedField):
    def to_representation(self, instance):
        points = (wins)*3 + ties
        return points

    def to_internal_value(self, data):
        return Team.objects.get(points=data)