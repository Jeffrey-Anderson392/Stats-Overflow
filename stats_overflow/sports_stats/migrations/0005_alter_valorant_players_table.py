# Generated by Django 5.0.2 on 2024-05-03 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports_stats', '0004_rename_acs_valorant_players_assists_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='valorant_players',
            table='sports_stats_valorant_player_stats',
        ),
    ]
