from django.contrib import admin

from phonebook.models import PhoneBook, Numbers, Category


class CategoryInline(admin.StackedInline):
    model = Category
    exclude = []


class NumbersInline(admin.StackedInline):
    model = Numbers
    exclude = []


class PhoneBookAdmin(admin.ModelAdmin):
    list_display_links = ['id', 'first_name']
    list_display = ['id', 'is_deleted', 'first_name', 'last_name', 'birth_date', 'address', 'numbers_num']
    list_filter = ['first_name']
    search_fields = ['first_name', 'patronymic', 'last_name']
    fields = ['first_name', 'patronymic', 'last_name', 'birth_date', 'address', 'is_deleted']
    inlines = [NumbersInline]


admin.site.register(PhoneBook, PhoneBookAdmin)
''' Можно отдельно добовлять номера телефонов и прикреплять их к уже существующим записям в телефонной книге'''
admin.site.register(Numbers)
admin.site.register(Category)
