# Generated by Django 4.2.4 on 2024-07-07 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
