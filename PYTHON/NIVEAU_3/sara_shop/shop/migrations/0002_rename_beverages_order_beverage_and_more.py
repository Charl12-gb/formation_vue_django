# Generated by Django 4.2 on 2023-08-23 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='beverages',
            new_name='beverage',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='dishes',
            new_name='dish',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='sauces',
            new_name='sauce',
        ),
    ]
