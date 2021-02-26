from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=30, verbose_name='Категория')

    def __str__(self):
        return "{}. {}".format(self.pk, self.category)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Numbers(models.Model):
    category = models.ForeignKey('phonebook.Category', related_name='numbers', blank=True,
                                 on_delete=models.SET_DEFAULT, default='', verbose_name='Категория')
    number = models.CharField(max_length=25, null=True, blank=True, verbose_name='Номер')
    phone_book = models.ForeignKey('phonebook.PhoneBook', null=True, blank=True, related_name='numbers',
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
    avatar = models.ImageField(upload_to='admin_user_pic', null=True, blank=True, verbose_name='Аватар')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    is_deleted = models.BooleanField(default=False)

    def image_img(self):
        if self.avatar:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="60"/></a>'.format(self.avatar.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Аватарка'
    image_img.allow_tags = True

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
