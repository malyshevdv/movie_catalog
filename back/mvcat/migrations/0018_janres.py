# Generated by Django 4.2.9 on 2024-02-04 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvcat', '0017_alter_actor_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Janres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picturePath', models.CharField(max_length=150)),
            ],
        ),
    ]