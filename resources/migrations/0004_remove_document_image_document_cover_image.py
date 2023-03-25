# Generated by Django 4.1.7 on 2023-03-25 14:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_alter_article_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='image',
        ),
        migrations.AddField(
            model_name='document',
            name='cover_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='resource/documents/images/'),
            preserve_default=False,
        ),
    ]
