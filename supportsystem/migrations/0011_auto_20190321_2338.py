# Generated by Django 2.1.7 on 2019-03-21 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supportsystem', '0010_auto_20190321_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='commentmedia',
        ),
        migrations.RemoveField(
            model_name='post',
            name='postmedia',
        ),
    ]
