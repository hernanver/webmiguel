# Generated by Django 4.0.5 on 2022-08-01 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default='DEFAULT VALUE', max_length=10, verbose_name='Precio'),
        ),
    ]
