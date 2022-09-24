# Generated by Django 4.1.1 on 2022-09-24 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_productcategory_product_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='product.productcategory'),
        ),
    ]