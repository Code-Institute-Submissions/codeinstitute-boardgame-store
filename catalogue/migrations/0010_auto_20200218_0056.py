# Generated by Django 2.2.6 on 2020-02-18 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0009_auto_20200217_0741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='available',
        ),
        migrations.RemoveField(
            model_name='game',
            name='stock_left',
        ),
    ]
