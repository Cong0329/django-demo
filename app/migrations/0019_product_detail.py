# Generated by Django 5.0 on 2024-04-01 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_remove_product_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='detail',
            field=models.CharField(max_length=500, null=True),
        ),
    ]