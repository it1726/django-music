# Generated by Django 3.1.1 on 2020-10-06 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20201006_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='mp3',
            field=models.FileField(default=1, upload_to='mp3'),
            preserve_default=False,
        ),
    ]