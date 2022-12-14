# Generated by Django 4.1 on 2022-11-19 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0033_cometarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cometarios',
            name='perfil',
        ),
        migrations.AddField(
            model_name='cometarios',
            name='data',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='cometarios',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cometarios',
            name='Post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.postblog'),
        ),
    ]
