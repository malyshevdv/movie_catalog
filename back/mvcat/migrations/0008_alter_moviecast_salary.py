# Generated by Django 5.0.1 on 2024-01-16 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvcat', '0007_alter_actor_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviecast',
            name='salary',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=15, null=True),
        ),
    ]