# Generated by Django 4.1.5 on 2023-02-14 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myPantryApi', '0004_pantryitem_imagesrc'),
    ]

    operations = [
        migrations.AddField(
            model_name='pantryitemcategory',
            name='icon',
            field=models.CharField(default='question', max_length=100),
        ),
        migrations.AlterField(
            model_name='pantryitem',
            name='imageSrc',
            field=models.URLField(blank=True, null=True),
        ),
    ]
