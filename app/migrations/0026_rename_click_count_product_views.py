# Generated by Django 5.0 on 2024-04-10 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='click_count',
            new_name='views',
        ),
    ]
