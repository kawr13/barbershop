# Generated by Django 4.2.7 on 2023-11-18 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barberapp', '0002_article_images_alter_master_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='master',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='barberapp.category'),
            preserve_default=False,
        ),
    ]