# Generated by Django 3.1.1 on 2020-10-06 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201006_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='like',
        ),
    ]
