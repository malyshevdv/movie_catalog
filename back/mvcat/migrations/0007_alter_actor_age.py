# Generated by Django 5.0.1 on 2024-01-16 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvcat', '0006_alter_movie_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='age',
            field=models.CharField(default=0, max_length=150),
        ),
    ]
