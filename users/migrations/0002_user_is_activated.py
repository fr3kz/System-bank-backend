# Generated by Django 4.2.6 on 2023-11-06 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_Activated',
            field=models.BooleanField(default=False),
        ),
    ]
