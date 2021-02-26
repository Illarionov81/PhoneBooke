from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=30, verbose_name='Категория')

    def __str__(self):
        return "{}. {}".format(self.pk, self.category)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Numbers(models.Model):
    category = models.ForeignKey('phonebook.Category', related_name='numbers', on_delete=models.PROTECT,
                                 verbose_name='Категория')
    number = models.CharField(max_length=25, verbose_name='Номер')
    phone_book = models.ForeignKey('phonebook.PhoneBook', related_name='numbers',
                                   verbose_name='Чей номер', on_delete=models.CASCADE)

    def __str__(self):
        return "{}. {}".format(self.pk, self.number)

    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефона'


class PhoneBook(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, null=False, blank=False, verbose_name='Отчество')
    last_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Фамилия')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    is_deleted = models.BooleanField(default=False)

    def numbers_num(self):
        if self.numbers.all():
            return self.numbers.all()[0].number
        else:
            return 'нет номера телефона'

    numbers_num.short_description = 'Номер телефона'
    numbers_num.allow_tags = True

    def __str__(self):
        return "{}. {}".format(self.pk, self.first_name)

    class Meta:
        verbose_name = 'Запись в телефонном справочнике'
        verbose_name_plural = 'Записи в телефонном справочнике'
