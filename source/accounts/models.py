from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='admin_user_pic', null=True, blank=True, verbose_name='Аватар')

    def image_img(self):
        if self.avatar:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="80"/></a>'.format(self.avatar.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Аватарка'
    image_img.allow_tags = True

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

