# Generated by Django 4.1.7 on 2023-03-25 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_name_category_title_rename_name_tag_title'),
        ('resources', '0002_alter_document_tags_alter_video_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='core.tag'),
        ),
    ]