# Generated by Django 5.1.7 on 2025-04-15 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_product_media1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='media1',
            field=models.ImageField(blank=True, null=True, upload_to='product/media/'),
        ),
    ]
