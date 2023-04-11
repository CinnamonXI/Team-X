# Generated by Django 4.1.7 on 2023-04-11 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_tag_followers'),
        ('discussion', '0013_question_views_alter_question_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='core.category'),
        ),
    ]
