# Generated by Django 4.1 on 2022-11-13 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_bloguser_imagenuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagenuser',
            name='img',
        ),
        migrations.AddField(
            model_name='imagenuser',
            name='Img',
            field=models.ImageField(blank=True, null=True, upload_to='User'),
        ),
    ]
