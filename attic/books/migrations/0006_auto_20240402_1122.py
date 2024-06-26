# Generated by Django 2.2.19 on 2024-04-02 11:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20240402_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_year',
            field=models.PositiveIntegerField(help_text='Год издания', validators=[django.core.validators.MaxValueValidator(3000), django.core.validators.MinValueValidator(1000)], verbose_name='Год издания'),
        ),
    ]
