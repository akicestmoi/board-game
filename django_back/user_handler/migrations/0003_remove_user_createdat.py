# Generated by Django 4.1.7 on 2023-03-17 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_handler", "0002_alter_user_options_alter_user_managers_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="createdAt",
        ),
    ]
