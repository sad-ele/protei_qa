from Master.Navigation_tests.NavigationPageObject import SearchHelper

# переход на страницу авторизации
def test1(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.go_to_auth()
    title = main_page.check_auth()
    assert title.is_displayed()
    assert title.get_attribute("class") == "uk-legend"
    assert title.text == "Привет с демо-сайта для автотестов!"


# переход на главную страницв
def test2(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.go_to_main()
    title = main_page.check_main()
    assert title.is_displayed()
    assert title.get_attribute("class") == "uk-card-title"
    assert title.text == "Добро пожаловать!"


# переход на страницу пользователей
def test3(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.go_to_users()
    table = main_page.check_users()
    assert table.is_displayed()
    assert table.get_attribute("id") == "dataTable"


# переход на страницу пользователей (выпадающий список)
def test3_1(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.go_to_users_dropdown()
    table = main_page.check_users()
    assert table.is_displayed()
    assert table.get_attribute("id") == "dataTable"


# переход на страницу добавленияпользователей (выпадающий список)
def test3_2(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.go_to_add_dropdown()
    title = main_page.check_add()
    assert title.is_displayed()
    assert title.get_attribute("class") == "uk-legend"
    assert title.text == "Добавление пользователя"


# переход на страницу вариантов
def test4(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.go_to_variants()
    title = main_page.check_variants()
    assert title.is_displayed()
    assert title.get_attribute("class") == "uk-card-title"
    assert title.text == "НТЦ ПРОТЕЙ"

#только для страницы пользователей, кнопка "добавить пользователя"
def test5(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.add_button()
    title = main_page.check_add()
    assert title.is_displayed()
    assert title.get_attribute("class") == "uk-legend"
    assert title.text == "Добавление пользователя"