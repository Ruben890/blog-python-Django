# Generated by Django 4.1.3 on 2022-11-23 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0052_rename_aser_cometarios_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cometarios',
            old_name='user',
            new_name='author',
        ),
    ]