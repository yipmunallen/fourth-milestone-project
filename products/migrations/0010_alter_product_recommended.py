# Generated by Django 3.2.3 on 2021-06-26 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_rename_recommend_product_recommended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='recommended',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
