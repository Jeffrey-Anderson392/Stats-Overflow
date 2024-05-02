# Generated by Django 5.0.3 on 2024-05-02 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports_stats', '0003_nba_player_assists_stats_nba_player_blocks_stats_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='valorant_players',
            old_name='ACS',
            new_name='Assists',
        ),
        migrations.RenameField(
            model_name='valorant_players',
            old_name='Kills_per_round',
            new_name='AssistsPerRound',
        ),
        migrations.RenameField(
            model_name='valorant_players',
            old_name='deaths',
            new_name='AverageCombatScore',
        ),
        migrations.RenameField(
            model_name='valorant_players',
            old_name='kd',
            new_name='AverageDamagePerRound',
        ),
        migrations.RenameField(
            model_name='valorant_players',
            old_name='kills',
            new_name='ClutchSuccessRate',
        ),
        migrations.RenameField(
            model_name='valorant_players',
            old_name='fname',
            new_name='PlayerName',
        ),
        migrations.RemoveField(
            model_name='valorant_players',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='valorant_players',
            name='player_id',
        ),
        migrations.RemoveField(
            model_name='valorant_players',
            name='team_id',
        ),
        migrations.AddField(
            model_name='valorant_players',
            name='Deaths',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valorant_players',
            name='FirstDeathPerRound',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valorant_players',
            name='FirstDeaths',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valorant_players',
            name='FirstKills',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valorant_players',
            name='FirstKillsPerRound',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valorant_players',
            name='HeadShotPercentage',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valorant_players',
            name='KillAssistsPercentage',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valorant_players',
            name='KillPerRound',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valorant_players',
            name='Kills',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valorant_players',
            name='KillsToDeaths',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valorant_players',
            name='MaxKillsInAMap',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valorant_players',
            name='Rating',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valorant_players',
            name='RoundsPlayed',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valorant_players',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]