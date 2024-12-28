# Generated by Django 5.1.4 on 2024-12-28 20:34

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_sv4ta9.jpg', storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to='images/'),
        ),
    ]
