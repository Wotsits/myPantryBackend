# Generated by Django 4.1.5 on 2023-02-08 18:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myPantryApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PantryItemCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
