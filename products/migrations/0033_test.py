# Generated by Django 3.0.6 on 2021-01-27 19:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('products', '0032_auto_20210120_0131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('box_size', models.CharField(choices=[('50х50х35', '50х50х35'), ('60х60х40', '60х60х40'), ('60х60х40-P', '60х60х40-P'), ('80х80х40', '80х80х40'), ('80х80х40-P', '80х80х40-P'), ('240х185х120', '240х185х120'), ('270х220х70', '270х220х70')], default='80х80х40', max_length=50)),
                ('int_list', models.CharField(max_length=100, validators=[django.core.validators.int_list_validator])),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_products.test_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
    ]
