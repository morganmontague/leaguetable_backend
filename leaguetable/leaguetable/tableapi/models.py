from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Team(models.Model):
    team_name = models.CharField(max_length=200, default="New Team")
    team_grounp = models.PositiveIntegerField()
    user_id = models.ForeignKey('CustomUser', on_delete=models.PROTECT, related_name="manager_name")
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


    def __str__(self):
        return f"{self.team_name}"

class Player(models.Model):
    player_name = models.CharField(max_length=200, default="new guy")
    # team_id 
    jersey_no = models.PositiveIntegerField(validators= [MaxValueValidator(99)])
    nationality_id = models.ForeignKey('nationality', on_delete=models.PROTECT, related_name="player_nation", null=True)
    position_id = models.ForeignKey('position', on_delete=models.PROTECT, related_name="player_position", null=True)
    injured = models.BooleanField()
    age = models.PositiveIntegerField(validators= [MinValueValidator(16), MaxValueValidator(45)])

    def __str__(self):
        return f"Player: {self.player_name}, Position {self.position_id}. "

class Position(models.Model):
    position = models.CharField(max_length=100, default='Soccer Player')

    def __str__(self):
        return f"{self.position}"

class Nationality(models.Model):
    nationality = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return self.nationality

class Team_Players(models.Model):
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)

class Venue(models.Model):
    venue_name = models.CharField(max_length=200, default="Stadium")
    address = models.CharField(max_length=200, default="Doha, Qatar")

    def __str__(self):
        return self.venue_name

class Game(models.Model):
    date_of_match = models.DateTimeField(auto_now=True, null=True)
    goals_scored = models.PositiveIntegerField(default = 0)
    goal_conceded = models.PositiveIntegerField(default = 0)
    venue_id = models.ForeignKey(Venue, on_delete=models.PROTECT)

    def __str__(self):
        return f"Goals Scored {self.goals_scored} and Goals Conceded {self.goal_conceded}"

class Team_Games(models.Model):
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)


# class Goal_detail(models.Model):
#   game_id = models.ForeignKey(Game, on_delete)
#   player_id
#   team_id
#   goal_time
#   goal_half

    