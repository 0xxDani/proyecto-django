# Generated by Django 4.2.8 on 2023-12-17 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_rename_description_product_descripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='categoria',
        ),
    ]
