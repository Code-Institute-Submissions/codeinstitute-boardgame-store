# Generated by Django 2.2.6 on 2020-02-17 07:28

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charge',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
