# Generated by Django 5.0 on 2024-04-01 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='detail',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
