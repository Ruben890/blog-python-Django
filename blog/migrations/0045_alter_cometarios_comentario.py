# Generated by Django 4.1.3 on 2022-11-19 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0044_alter_cometarios_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cometarios',
            name='comentario',
            field=models.TextField(),
        ),
    ]