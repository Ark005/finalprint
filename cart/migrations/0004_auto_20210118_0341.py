# Generated by Django 3.0.6 on 2021-01-18 00:41

import cart.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=cart.models.user_directory_path),
        ),
    ]
