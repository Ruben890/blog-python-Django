# Generated by Django 4.1.3 on 2022-11-19 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0042_cometarios_post_alter_postblog_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cometarios',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.postblog'),
            preserve_default=False,
        ),
    ]
