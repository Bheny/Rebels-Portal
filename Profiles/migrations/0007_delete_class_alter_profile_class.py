# Generated by Django 4.1.7 on 2023-03-20 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Class', '0001_initial'),
        ('Profiles', '0006_rename_driver_application_application_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.AlterField(
            model_name='profile',
            name='Class',
            field=models.ManyToManyField(blank=True, to='Class.class'),
        ),
    ]
