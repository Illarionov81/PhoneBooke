from django.core.management import call_command
from django.template.response import TemplateResponse
from django.test import TestCase
from django.urls import reverse

from phonebook.models import PhoneBook


class CheckURL(TestCase):
    def test_get_url(self):
        redirect_url = reverse('book')
        response = self.client.get(reverse('book',))
        self.check_redirect(response, redirect_url)

    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)
        self.assertEqual('/', redirect_url)


class CheckSearch(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        call_command('loaddata', 'fixtures/auth.json', verbosity=0)
        call_command('loaddata', 'fixtures/dump.json', verbosity=0)

    def test_search(self):
        redirect_url = '/?search=М'
        response = self.client.get('/?search=М')
        self.check_redirect(response, redirect_url)

    def check_redirect(self, response, redirect_url):
        self.assertEqual(redirect_url, redirect_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)


class PhoneBookTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        call_command('loaddata', 'fixtures/auth.json', verbosity=0)
        call_command('loaddata', 'fixtures/dump.json', verbosity=0)

    def setUp(self) -> None:
        self.phonebooks = PhoneBook.objects.all()

    def test_book_mast_have_fields(self):
        for phonebook in self.phonebooks:
            self.assertTrue(phonebook.first_name, True)
            self.assertTrue(phonebook.patronymic, True)
            self.assertTrue(phonebook.last_name, True)
            self.assertTrue(phonebook.address, True)

