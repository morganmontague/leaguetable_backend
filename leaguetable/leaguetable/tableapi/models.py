from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Team(models.Model):
    team_name = models.CharField(max_length=200, default="New Team")
    team_grounp = models.PositiveIntegerField()
    user_id = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name="manager_name")
    # location_id
    created_at = models.DateTimeField(auto_now_add=True, null=True)  
    updated_at = models.DateTimeField(auto_now=True, null=True)
    wins = models.PositiveIntegerField()
    losses = models.PositiveIntegerField()
    ties = models.PositiveIntegerField()
    games_played = models.PositiveIntegerField()
    goals_scored = models.PositiveIntegerField()
    rank = models.PositiveIntegerField() 
    points = models.PositiveIntegerField()
    
    # def save(self, *args, **kwargs):
    #     self.points = (self.wins *3) +self.ties
    #     self.games_played = self.wins +self.losses +self.ties
    #     super(Team, self).save(*args, **kwargs)
    #     return self.points, self.games_played
    # def points(self):
    #     points = (self.wins)*3 + self.ties
    #     return points
    # def games_played(self):
    #     games_played = self.wins +self.losses +self.ties
    #     return games_played

    def __str__(self):
        return self.team_name