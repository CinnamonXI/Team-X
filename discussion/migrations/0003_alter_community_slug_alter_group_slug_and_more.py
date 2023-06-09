# Generated by Django 4.1.7 on 2023-04-06 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0002_remove_group_image_community_slug_group_cover_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
