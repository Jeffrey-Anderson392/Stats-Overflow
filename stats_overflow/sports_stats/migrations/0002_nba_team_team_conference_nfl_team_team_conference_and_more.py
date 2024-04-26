# Generated by Django 5.0.2 on 2024-04-25 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports_stats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nba_team',
            name='team_conference',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nfl_team',
            name='team_conference',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nhl_team',
            name='team_conference',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
    ]
