import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://149.255.118.78:7080")
    yield driver
    driver.close()


#верные email и пароль
def test1(driver):
    # шаг 1
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='loginEmail']")))
    login.send_keys("test@protei.ru")

    # шаг 2
    password = driver.find_element(By.XPATH, "//*[@id='loginPassword']")
    password.send_keys("test")

    # шаг 3
    enter = driver.find_element(By.XPATH, "//*[@id='authButton']")
    enter.click()

    # ожидаемый результат
    main_title = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "h3")))
    assert main_title.is_displayed()
    assert main_title.get_attribute("class") == "uk-card-title"
    assert main_title.text == "Добро пожаловать!"


#валидные, но не верные email и пароль
def test2(driver):  # /^[^-]+?@.+?$/ email
    # шаг 1
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("nottest@protei.ru")

    # шаг 2
    password = driver.find_element(By.ID, "loginPassword")
    password.send_keys("nottest")

    # шаг 3
    enter = driver.find_element(By.ID, "authButton")
    enter.click()

    # ожидаемый результат
    warning_frame = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "KEKEKEKEKEKKEKE")))
    assert warning_frame.is_displayed()
    assert warning_frame.get_attribute("class") == "uk-alert uk-alert-danger"

    p_text = driver.find_element(By.CSS_SELECTOR, "#KEKEKEKEKEKKEKE p")
    assert p_text.text == "Неверный E-Mail или пароль"


#пустая форма
def test3(driver):
    # шаг 1
    enter = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "button[type]")))
    enter.click()

    # ожидаемый результат
    warning_frame = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".uk-alert.uk-alert-danger")))
    assert warning_frame.is_displayed()

    p_text = driver.find_element(By.CSS_SELECTOR, "#emailFormatError > p")
    assert p_text.text == "Неверный формат E-Mail"


#невалидный email
def test4(driver):
    # шаг 1
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("@protei.ru")

    # шаг 2
    password = driver.find_element(By.ID, "loginPassword")
    password.send_keys("test")

    # шаг 3
    enter = driver.find_element(By.ID, "authButton")
    enter.click()

    # ожидаемый результат
    warning_frame = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "emailFormatError")))

    assert warning_frame.is_displayed()
    assert warning_frame.get_attribute("class") == "uk-alert uk-alert-danger"

    p_text = driver.find_element(By.CSS_SELECTOR, "#emailFormatError p")
    assert p_text.text == "Неверный формат E-Mail"


#неверный пароль
def test5(driver):
    # шаг 1
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']")))
    login.send_keys("test@protei.ru")

    # шаг 2
    password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    password.send_keys("tesd")

    # шаг 3
    enter = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    enter.click()

    # ожидаемый результат
    warning_frame = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "KEKEKEKEKEKKEKE")))
    assert warning_frame.is_displayed()
    assert warning_frame.get_attribute("class") == "uk-alert uk-alert-danger"

    p_text = driver.find_element(By.CSS_SELECTOR, "#KEKEKEKEKEKKEKE p")
    assert p_text.text == "Неверный E-Mail или пароль"