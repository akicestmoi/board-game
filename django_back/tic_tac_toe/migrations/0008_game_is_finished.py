# Generated by Django 4.1.7 on 2023-03-16 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tic_tac_toe", "0007_game_draw_alter_game_board_size"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="is_finished",
            field=models.BooleanField(default=False),
        ),
    ]
