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

    def get_context_data(self, *, object_list=None, **kwargs):
        form = SimpleSearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            kwargs['search'] = search
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        data = PhoneBook.objects.all().filter(is_deleted=False).order_by('first_name')
        form = SimpleSearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            if search:
                data = data.filter(Q(first_name__icontains=search) | Q(numbers__number__icontains=search))
        return data
