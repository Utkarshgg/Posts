# Generated by Django 4.2.1 on 2023-06-04 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainscreen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=33333, upload_to='static/images'),
            preserve_default=False,
        ),
    ]
