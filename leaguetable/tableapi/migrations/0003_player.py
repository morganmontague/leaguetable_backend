# Generated by Django 4.1.3 on 2022-11-29 14:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableapi', '0002_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(default='new guy', max_length=200)),
                ('jersey_no', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99)])),
                ('injured', models.BooleanField()),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(45)])),
            ],
        ),
    ]
