from rest_framework import serializers
from .models import CustomUser, Team
from .fields import *

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["username", "is_active", "first_name", "last_name"]


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = "__all__"