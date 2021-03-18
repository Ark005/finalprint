# Generated by Django 3.0.6 on 2021-01-28 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0034_auto_20210128_0129'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoxSizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=80)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
