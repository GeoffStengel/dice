# Generated by Django 5.1.1 on 2024-09-17 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_petprofile_delete_poochprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='petprofile',
            name='category',
            field=models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat'), ('bird', 'Bird')], default='other', max_length=10),
        ),
    ]
