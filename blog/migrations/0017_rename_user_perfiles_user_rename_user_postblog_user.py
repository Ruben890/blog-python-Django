# Generated by Django 4.1 on 2022-11-15 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_perfiles_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfiles',
            old_name='User',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='postblog',
            old_name='User',
            new_name='user',
        ),
    ]