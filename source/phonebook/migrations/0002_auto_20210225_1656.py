# Generated by Django 2.2.13 on 2021-02-25 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='numbers',
            options={'verbose_name': 'Номер телефона', 'verbose_name_plural': 'Номера телефона'},
        ),
        migrations.AlterModelOptions(
            name='phonebook',
            options={'verbose_name': 'Телефонная книга', 'verbose_name_plural': 'Телефонные книги'},
        ),
    ]
