# Generated by Django 3.2.15 on 2022-09-24 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_servicerequest_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to='serviceRequests'),
        ),
    ]
