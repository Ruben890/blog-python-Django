# Generated by Django 4.1.3 on 2022-11-16 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_alter_postblog_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfiles',
            name='imagen',
            field=models.ImageField(default='buo.jpg', upload_to=''),
        ),
    ]
