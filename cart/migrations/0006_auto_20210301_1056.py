# Generated by Django 3.1.3 on 2021-03-01 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20210301_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]
