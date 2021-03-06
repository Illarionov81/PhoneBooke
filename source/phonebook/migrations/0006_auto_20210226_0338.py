# Generated by Django 2.2.13 on 2021-02-26 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0005_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='numbers',
            name='categorys',
            field=models.ManyToManyField(blank=True, related_name='numbers', to='phonebook.Category'),
        ),
    ]
