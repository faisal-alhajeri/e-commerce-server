# Generated by Django 4.1.1 on 2022-09-22 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='quantity',
        ),
    ]