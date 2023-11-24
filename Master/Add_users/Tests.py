from Master.Add_users.Add_usersPageObject import SearchHelper


def test1(browser):
    add_page = SearchHelper(browser)
    add_page.go_to_site()
    add_page.enter_email("new@protei.ru")
    add_page.enter_password("new")
    add_page.enter_name("Ivan")
    add_page.add_user()
    modal_window = add_page.check_window()
    assert modal_window.is_displayed()
    assert modal_window.text == "Данные добавлены."


def test2(browser):
    add_page = SearchHelper(browser)
    add_page.go_to_site()
    add_page.enter_email("new@protei.ru")
    add_page.enter_password("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    add_page.enter_name("IvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvan")
    add_page.add_user()
    modal_window = add_page.check_window()
    assert modal_window.is_displayed()
    assert modal_window.text == "ОШИБКА! FAIL"


def test3(browser):
    add_page = SearchHelper(browser)
    add_page.go_to_site()
    add_page.enter_email("new@protei.ru")
    add_page.enter_password("")
    add_page.enter_name("")
    add_page.add_user()
    warning_frame = add_page.check_warning()
    warning_text = add_page.check_warning_text()
    assert warning_frame.is_displayed()
    assert warning_text.text == "Поле Имя не может быть пустым"


def test4(browser):
    add_page = SearchHelper(browser)
    add_page.go_to_site()
    add_page.enter_email("@protei.ru")
    add_page.enter_password("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    add_page.enter_name("")
    add_page.add_user()
    error_frame = add_page.check_email_error()
    error_text = add_page.check_error_text()
    assert error_frame.is_displayed()
    assert error_text.text == "Неверный формат E-Mail"


def test5(browser):
    add_page = SearchHelper(browser)
    add_page.go_to_site()
    add_page.enter_email("@protei.ru")
    add_page.enter_password("")
    add_page.enter_name("Ivan")
    add_page.add_user()
    error_frame = add_page.check_email_error()
    error_text = add_page.check_error_text()
    assert error_frame.is_displayed()
    assert error_text.text == "Неверный формат E-Mail"


def test6(browser):
    add_page = SearchHelper(browser)
    add_page.go_to_site()
    add_page.enter_email("@protei.ru")
    add_page.enter_password("12345678")
    add_page.enter_name("IvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvan")
    add_page.add_user()
    error_frame = add_page.check_email_error()
    error_text = add_page.check_error_text()
    assert error_frame.is_displayed()
    assert error_text.text == "Неверный формат E-Mail"


def test7(browser):
    add_page = SearchHelper(browser)
    add_page.go_to_site()
    add_page.enter_email("")
    add_page.enter_password("")
    add_page.enter_name("IvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvan")
    add_page.add_user()
    error_frame = add_page.check_email_error()
    error_text = add_page.check_error_text()
    assert error_frame.is_displayed()
    assert error_text.text == "Неверный формат E-Mail"


def test8(browser):
    add_page = SearchHelper(browser)
    add_page.go_to_site()
    add_page.enter_email("")
    add_page.enter_password("12345678")
    add_page.enter_name("")
    add_page.add_user()
    error_frame = add_page.check_email_error()
    error_text = add_page.check_error_text()
    assert error_frame.is_displayed()
    assert error_text.text == "Неверный формат E-Mail"


def test9(browser):
    add_page = SearchHelper(browser)
    add_page.go_to_site()
    add_page.enter_email("")
    add_page.enter_password("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    add_page.enter_name("Ivan")
    add_page.add_user()
    error_frame = add_page.check_email_error()
    error_text = add_page.check_error_text()
    assert error_frame.is_displayed()
    assert error_text.text == "Неверный формат E-Mail"