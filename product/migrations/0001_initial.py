# Generated by Django 4.1.1 on 2022-09-16 12:01

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created at')),
                ('modified_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='modified at')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Product Name')),
                ('price', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Product Price')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
