# Generated by Django 3.2.3 on 2021-06-28 19:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20210627_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
