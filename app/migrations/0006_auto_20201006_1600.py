# Generated by Django 3.1.1 on 2020-10-06 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200930_2247'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ['author', 'title']},
        ),
        migrations.AddField(
            model_name='song',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
