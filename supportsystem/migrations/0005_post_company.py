# Generated by Django 2.1.7 on 2019-03-16 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supportsystem', '0004_auto_20190315_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='supportsystem.Company'),
            preserve_default=False,
        ),
    ]
