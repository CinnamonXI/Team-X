# Generated by Django 4.1.7 on 2023-04-06 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_tag_followers'),
        ('discussion', '0010_alter_question_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='questions', to='core.tag'),
        ),
    ]
