# Generated by Django 4.2.6 on 2023-11-06 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_account_is_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
