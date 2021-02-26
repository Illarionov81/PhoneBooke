# Generated by Django 2.2.13 on 2021-02-25 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='admin_user_pic', verbose_name='Аватар')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Numbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, verbose_name='Категория')),
                ('number', models.CharField(blank=True, max_length=25, null=True, verbose_name='Номер')),
                ('phone_book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='numbers', to='phonebook.PhoneBook', verbose_name='Номера')),
            ],
        ),
    ]