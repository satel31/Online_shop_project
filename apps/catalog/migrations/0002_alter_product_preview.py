# Generated by Django 4.0.4 on 2023-06-01 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='media/products/', verbose_name='Preview'),
        ),
    ]