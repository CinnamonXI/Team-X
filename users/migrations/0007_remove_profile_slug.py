# Generated by Django 4.1.7 on 2023-03-28 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_follower_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
    ]
