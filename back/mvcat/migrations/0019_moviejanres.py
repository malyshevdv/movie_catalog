# Generated by Django 4.2.9 on 2024-02-04 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mvcat', '0018_janres'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieJanres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('janre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvcat.janres')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvcat.movie')),
            ],
        ),
    ]