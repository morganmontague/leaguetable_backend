from rest_framework import serializers
from .models import *

class TeamListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.name