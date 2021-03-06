# Generated by Django 3.2.3 on 2021-06-27 13:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_recommended'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='recommended',
        ),
        migrations.AddField(
            model_name='product',
            name='recommend_percentage',
            field=models.IntegerField(
                blank=True,
                default=0,
                null=True,
                validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100)]),
        ),
    ]
