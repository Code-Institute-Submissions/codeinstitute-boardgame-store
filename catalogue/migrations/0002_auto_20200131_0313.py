# Generated by Django 2.2.6 on 2020-01-31 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='perecent',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='stock_left',
            field=models.IntegerField(),
        ),
    ]
