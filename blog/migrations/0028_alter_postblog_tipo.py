# Generated by Django 4.1 on 2022-11-18 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_alter_postblog_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postblog',
            name='tipo',
            field=models.CharField(choices=[('Noticias', 'Noticias'), ('Juegos', 'Juegos'), ('Tecnología', 'Tecnología')], max_length=50),
        ),
    ]