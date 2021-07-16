# Generated by Django 3.1.3 on 2021-07-16 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0066_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='category',
            name='price',
            field=models.FloatField(default=None, null=True),
        ),
    ]
