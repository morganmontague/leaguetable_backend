from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Team(models.Model):
    team_name = models.CharField(max_length=200, default="New Team")
    team_grounp = models.PositiveIntegerField()
    games_played = models.PositiveIntegerField()
    user_id = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name="manager_name")
    # location_id
    created_at = models.DateTimeField(auto_now_add=True, null=True)  
    updated_at = models.DateTimeField(auto_now=True, null=True)
    wins = models.PositiveIntegerField()
    losses = models.PositiveIntegerField()
    ties = models.PositiveIntegerField()
    goals_scored = models.PositiveIntegerField()
    rank = models.PositiveIntegerField()
    points =models.PositiveIntegerField()

    def __str__(self):
        return self.team_name