# Generated by Django 5.1.4 on 2025-01-03 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='birdset',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
            preserve_default=False,
        ),
    ]
