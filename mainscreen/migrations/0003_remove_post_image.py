# Generated by Django 4.2.1 on 2023-06-06 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainscreen', '0002_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
