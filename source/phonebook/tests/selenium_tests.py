from django.test import TestCase
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys


class LoginTest(TestCase):
    def setUp(self):
        self.driver = Chrome()

    def tearDown(self):
        self.driver.close()

    def test_log_in_as_admin(self):
        self.driver.get('http://localhost:8000/admin/')
        self.driver.find_element_by_name('username').send_keys('Администратор')
        input = self.driver.find_element_by_name('password')
        input.send_keys('Админ_123')
        input.send_keys(Keys.ENTER)
        assert self.driver.current_url == 'http://localhost:8000/admin/'

    def test_login_error(self):
        self.driver.get('http://localhost:8000/admin/')
        self.driver.find_element_by_name('username').send_keys('А')
        input = self.driver.find_element_by_name('password')
        input.send_keys('А')
        input.send_keys(Keys.ENTER)
        assert self.driver.current_url == 'http://localhost:8000/admin/login/?next=/admin/'
        error = self.driver.find_elements_by_class_name('errornote')[0]
        assert error.text == "Пожалуйста, введите корректные имя пользователя и" \
                             " пароль учётной записи. Оба поля могут быть чувствительны к регистру."
