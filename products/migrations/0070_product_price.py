# Generated by Django 3.2.9 on 2022-10-17 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0069_toy'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=None, null=True),
        ),
    ]
