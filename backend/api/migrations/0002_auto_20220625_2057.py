# Generated by Django 3.1 on 2022-06-25 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='assigned_to',
            field=models.ManyToManyField(related_name='members', to='api.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rank',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, related_name='profileranks', to='api.rank'),
        ),
    ]
