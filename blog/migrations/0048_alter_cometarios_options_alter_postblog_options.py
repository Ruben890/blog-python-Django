# Generated by Django 4.1.3 on 2022-11-20 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0047_alter_postblog_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cometarios',
            options={'ordering': ['data']},
        ),
        migrations.AlterModelOptions(
            name='postblog',
            options={'ordering': ['data']},
        ),
    ]
