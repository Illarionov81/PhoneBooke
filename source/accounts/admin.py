from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


def _(param):
    pass


class MyUserInline(UserAdmin):
    exclude = []
    list_display = ['image_img', "username", 'birth_date', ]
    readonly_fields = ['image_img', ]
    list_display_links = ['username']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined', 'image_img', 'avatar')}),
    )


admin.site.register(User, MyUserInline)
