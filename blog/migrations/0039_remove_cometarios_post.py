# Generated by Django 4.1.3 on 2022-11-19 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0038_rename_title_cometarios_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cometarios',
            name='post',
        ),
    ]