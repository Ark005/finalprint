# Generated by Django 3.1.3 on 2021-01-19 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='FolderType1',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('products.product',),
        ),
        migrations.AlterField(
            model_name='product',
            name='box_size',
            field=models.CharField(choices=[('50х50х35', '50х50х35'), ('60х60х40', '60х60х40'), ('60х60х40-P', '60х60х40-P'), ('80х80х40', '80х80х40'), ('80х80х40-P', '80х80х40-P'), ('240х185х120', '240х185х120'), ('270х220х70', '270х220х70')], default='80х80х40', max_length=50),
        ),
    ]
