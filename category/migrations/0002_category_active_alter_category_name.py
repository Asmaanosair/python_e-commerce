# Generated by Django 4.2.4 on 2024-06-03 14:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(50)]),
        ),
    ]