from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from phonebook.forms import SimpleSearchForm
from phonebook.models import PhoneBook


class PhoneBookeList(ListView):
    model = PhoneBook
    template_name = 'book.html'
    context_object_name = 'books'
    paginate_by = 5
    paginate_orphans = 2

# Create your views here.
