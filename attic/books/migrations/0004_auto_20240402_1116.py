# Generated by Django 2.2.19 on 2024-04-02 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20230606_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_year',
            field=models.IntegerField(help_text='Год издания', max_length=4, verbose_name='Год издания'),
        ),
    ]
