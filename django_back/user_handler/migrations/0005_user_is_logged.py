# Generated by Django 4.1.7 on 2023-03-17 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_handler", "0004_alter_user_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_logged",
            field=models.BooleanField(default=False),
        ),
    ]
