# Generated by Django 4.1.5 on 2023-02-08 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myPantryApi', '0002_pantryitemcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='pantryitem',
            name='category',
            field=models.ForeignKey(default='ab183c1b-d1f9-454e-b3d6-f7d3060454d7', on_delete=django.db.models.deletion.CASCADE, to='myPantryApi.pantryitemcategory'),
            preserve_default=False,
        ),
    ]