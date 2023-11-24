from Jedi.AuthPageObject import SearchHelper

#верные email и пароль
def test1(browser):
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.enter_login("test@protei.ru")
    auth_page.enter_password("test")
    auth_page.click_button()
    main_title = auth_page.check_title()
    assert main_title.is_displayed()
    assert main_title.get_attribute("class") == "uk-card-title"
    assert main_title.text == "Добро пожаловать!"


#валидные, но не верные email и пароль
def test2(browser):
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.enter_login("nottest@protei.ru")
    auth_page.enter_password("nottest")
    auth_page.click_button()
    warning_frame = auth_page.check_fast_warning()
    warning_text = auth_page.read_text_fast()
    assert warning_frame.is_displayed()
    assert warning_frame.get_attribute("class") == "uk-alert uk-alert-danger"
    assert warning_text.text == "Неверный E-Mail или пароль"


#пустая форма
def test3(browser):
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.click_button()
    warning_frame = auth_page.check_warning()
    warning_text = auth_page.read_text_usual()
    assert warning_frame.is_displayed()
    assert warning_text.text == "Неверный формат E-Mail"


#невалидный email
def test4(browser):
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.enter_login("@protei.ru")
    auth_page.enter_password("test")
    auth_page.click_button()
    warning_frame = auth_page.check_email_warning()
    warning_text = auth_page.read_text_usual()
    assert warning_frame.is_displayed()
    assert warning_frame.get_attribute("class") == "uk-alert uk-alert-danger"
    assert warning_text.text == "Неверный формат E-Mail"


#неверный пароль
def test5(browser):
    auth_page = SearchHelper(browser)
    auth_page.go_to_site()
    auth_page.enter_login("test@protei.ru")
    auth_page.enter_password("tesd")
    auth_page.click_button()
    warning_frame = auth_page.check_fast_warning()
    warning_text = auth_page.read_text_fast()
    assert warning_frame.is_displayed()
    assert warning_frame.get_attribute("class") == "uk-alert uk-alert-danger"
    assert warning_text.text == "Неверный E-Mail или пароль"