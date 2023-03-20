# Generated by Django 4.1.6 on 2023-03-08 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Profiles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="is_driver",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="profile",
            name="is_verified",
            field=models.BooleanField(default=True),
        ),
    ]
