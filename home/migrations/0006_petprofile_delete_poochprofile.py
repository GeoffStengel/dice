# Generated by Django 5.1.1 on 2024-09-17 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_poochprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('located', models.CharField(max_length=50)),
                ('pet_prof_img', models.ImageField(default='ppi/pet_default.jpg', upload_to='ppi/')),
            ],
        ),
        migrations.DeleteModel(
            name='PoochProfile',
        ),
    ]
