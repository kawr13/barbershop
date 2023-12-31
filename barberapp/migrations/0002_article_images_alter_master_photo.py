# Generated by Django 4.2.7 on 2023-11-17 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barberapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='images',
            field=models.ImageField(default=1, upload_to='articles/articles_images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='master',
            name='photo',
            field=models.ImageField(upload_to='masters/masters_photos'),
        ),
    ]
