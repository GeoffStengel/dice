# Generated by Django 5.1.1 on 2024-09-17 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_banner', models.CharField(max_length=100)),
                ('body_text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
