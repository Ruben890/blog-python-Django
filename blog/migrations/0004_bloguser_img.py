# Generated by Django 4.1 on 2022-11-13 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_postblog_img_bloguser'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='User', verbose_name='image'),
        ),
    ]
