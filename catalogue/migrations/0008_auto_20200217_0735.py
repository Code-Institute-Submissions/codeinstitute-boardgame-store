# Generated by Django 2.2.6 on 2020-02-17 07:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_auto_20200217_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='stock_left',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
