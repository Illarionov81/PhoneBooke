from behave import given, when, then


@given(u'Я открыл сайт по адресу "{url}"')
def open_page(context, url):
    context.browser.get(url)


@then(u"Я вижу поле для поиска")
def see_form(context):
    search_form = context.browser.find_element_by_id('search_form')
    assert search_form


@then(u'Я ввожу текст "{text}" в поле "{name}"')
def enter_text(context, text, name):
    context.browser.find_element_by_id(name).send_keys(text)


@then(u'Я отправляю форму')
def submit_form(context):
    context.browser.find_element_by_id('submit_search').click()


@then("Я должен видеть результат поиска")
def get_result(context):
    column = context.browser.find_elements_by_class_name('col')
    assert column


@when(u"Я вижу ссулку на вход в админку")
def step_impl(context):
    link = context.browser.find_element_by_id('admin')
    assert link


@then(u'Я нажимаю на ссылку админ')
def submit_form(context):
    context.browser.find_element_by_id('admin').click()


@then(u"Я должен видеть поле для ввода имени")
def get_result(context):
    username = context.browser.find_element_by_id('id_username')
    assert username


@then(u"Я должен видеть поле для ввода пароля")
def get_result(context):
    password = context.browser.find_element_by_name('password')
    assert password
