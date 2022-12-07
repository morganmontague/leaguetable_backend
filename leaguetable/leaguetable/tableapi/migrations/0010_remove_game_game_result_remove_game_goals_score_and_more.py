# Generated by Django 4.1.3 on 2022-12-07 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableapi', '0009_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='game_result',
        ),
        migrations.RemoveField(
            model_name='game',
            name='goals_score',
        ),
        migrations.AddField(
            model_name='game',
            name='goal_conceded',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='goals_scored',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
