# Generated by Django 4.1.7 on 2023-04-06 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0007_alter_answer_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='discussion.community'),
        ),
    ]
