# Generated by Django 5.1.1 on 2024-09-17 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_header_remove_homepage_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='lrg_banner',
            field=models.ImageField(default='banners/default.jpg', upload_to='banners/'),
        ),
    ]
