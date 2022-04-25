# Generated by Django 4.0.4 on 2022-04-23 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pis_product', '0017_stockout_purchased_item'),
        ('pis_sales', '0010_auto_20190622_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleshistory',
            name='extra_items',
            field=models.ManyToManyField(blank=True, max_length=200, to='pis_product.extraitems'),
        ),
        migrations.AlterField(
            model_name='saleshistory',
            name='purchased_items',
            field=models.ManyToManyField(blank=True, max_length=100, to='pis_product.purchasedproduct'),
        ),
    ]
