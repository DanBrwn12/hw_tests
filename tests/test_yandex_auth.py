import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

from auth_data import TEST_LOGIN


class TestYandexAuth(unittest.TestCase):
    """Тест авторизации на Яндекс"""

    def setUp(self):
        """Настройка перед каждым тестом"""
        self.driver = webdriver.Chrome()
        self.base_url = "https://passport.yandex.ru/auth/"
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        """Очистка после каждого теста"""
        self.driver.quit()

    def test_auth_page_loads(self):
        """Тест загрузки страницы авторизации"""
        self.driver.get(self.base_url)

        # Проверяем заголовок страницы
        self.assertIn("Авторизация", self.driver.title)

        # Проверяем наличие поля для ввода номера телефона
        try:
            login_field = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[id='passp-field-phone']"))
            )
            self.assertTrue(login_field.is_displayed())
            time.sleep(3)
        except TimeoutException:
            self.fail("Поле ввода номера телефона не найдено на странице")

    def test_successful_auth(self):
        """Тест успешной авторизации через логин с паролем"""
        self.driver.get("https://passport.yandex.ru/auth/")

        # Находим и нажимаем на кнопку других вариантов входа
        btn_other_variable = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='passp:exp-register']"))
        )
        btn_other_variable.click()
        time.sleep(3)
        btn_auth_for_login = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//ul[@class='RegistrationButtonPopup-list']/li[3]//button"))
        )
        btn_auth_for_login.click()
        time.sleep(3)
        login_field = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='passp-field-login']"))
        )
        login_field.send_keys(TEST_LOGIN)


        btn_enter = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='passp:sign-in']"))
        )
        btn_enter.click()
        time.sleep(3)


    def test_auth_with_invalid_credentials(self):
        """Тест авторизации с неверными данными"""
        self.driver.get(self.base_url)

        # Вводим неверный формат ввода
        login_field = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[id='passp-field-phone']"))
        )
        login_field.send_keys("900000000")
        time.sleep(3)

        # Нажимаем кнопку "Войти"
        login_button = self.driver.find_element(By.CSS_SELECTOR, "[id='passp:sign-in']")
        login_button.click()
        time.sleep(3)

        # Проверяем наличие сообщения об ошибке
        try:
            error_message = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[id='field:input-phone:hint']"))
            )
            self.assertTrue(error_message.is_displayed())
            self.assertIn("Недопустимый формат номера", error_message.text)
            time.sleep(3)
        except TimeoutException:
            self.fail("Сообщение об ошибке не появилось")

    def test_auth_form_elements_present(self):
        """Тест наличия всех необходимых элементов формы"""
        self.driver.get(self.base_url)

        elements_to_check = [
            ("[id='passp-field-phone']", "Поле логина"),
            ("[id='passp:sign-in']", "Кнопка входа"),
        ]

        for element_id, description in elements_to_check:
            with self.subTest(element=description):
                try:
                    element = self.driver.find_element(By.CSS_SELECTOR, element_id)
                    self.assertTrue(element.is_displayed(),
                                    f"Элемент {description} не отображается")
                    time.sleep(3)
                except NoSuchElementException:
                    self.fail(f"Элемент {description} не найден")

    def test_switch_to_qr_auth(self):
        """Тест переключения на QR-авторизацию"""
        self.driver.get(self.base_url)

        # Находим и нажимаем на кнопку с QR-авторизацией
        try:
            qr_tab = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-t='button:pseudo:qr-button']"))
            )
            qr_tab.click()
            time.sleep(3)

            # Проверяем, что появился QR-код
            qr_code = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[class='MagicField-qr']"))
            )
            self.assertTrue(qr_code.is_displayed())
            time.sleep(3)

        except TimeoutException:
            self.fail("Не удалось переключиться на QR-авторизацию")



