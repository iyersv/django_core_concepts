# Generated by Django 3.2.10 on 2021-12-12 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]