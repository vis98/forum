# Generated by Django 3.0.7 on 2020-07-07 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
