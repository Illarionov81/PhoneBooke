# Generated by Django 2.2.13 on 2021-02-26 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0008_auto_20210226_0340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='numbers',
            old_name='category',
            new_name='categorys',
        ),
    ]
