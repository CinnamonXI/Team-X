# Generated by Django 4.1.7 on 2023-03-27 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_personal_experience'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
    ]
